function friend()

n = 10;
L = valeurs(n,1);
A = zeros(n,n);
A(1,:) = ones(1,n);
%A =choix_matrice(n,L);
disp(A)
epsi = 0.1;
%stop = 100;
tol = 0.1;
machin = 0.1;
%[X,Y] = gershdisc(A,0.01)
predcor(A,epsi,tol,machin);
end

function M = choix_matrice(n,vp)                  
    D = eye(n).*vp; % D est la mat diagonale contenant les vp                
    P= zeros(n,n);
    for i = 1:n
        for j = 1:n
            P(i,j)=rand(1);
        end
    end
    % On crée une matrice aléatoire                                             
    while(det(P) == 0)
        for i = 0:n
            for j = 0:n
                P(i,j)=rand(1); % On recalcule P dans ce cas   
            end
        end
    end  
    M = P*D; %On calcule M grâce à la formule mathématique              
    M = mtimes(M,inv(P));
    %M a les bonnes valeurs propres                                            

end

function Liste = valeurs(n,lambda0)
    Liste=zeros(n,1);
    for i = 1:n % on cree des valeurs propres separees par 2                     
        Liste(i) = lambda0;
        lambda0=lambda0+2;
    end
end


function [X,Y] = gershdisc(A,eps)

%1ere etape: si la matrice n'est pas carree -> erreur 

if size(A,1) ~= size(A,2)
    error('La matrice que vous avez choisi n est pas carrée');
    return;
end

%2nd etape: creation du grillage avec elements imaginaires et reels 
n=size(A,1);  
X = [0,0]; % X = [xmin,xmax]
Y = [0,0]; % Y = [ymin,ymax]

for i=1:size(A,1)
    h=real(A(i,i));
    k=imag(A(i,i)); %Nombres imaginaires et reels 
    r=0;
    for j=1:size(A,1)
       if i ~= j 
           r=r+(norm(A(i,j))); %Calcul du rayon qui est la somme des normes pour i!=j
       end
    
    end 
    r = r + sqrt(size(A,1))*eps;

%3eme etape: Trace des elements 

%A. Le cercle 

    N=256; 
    t=(0:N)*2*pi/N;
    if ((h+r) > X(2))
        X(2) = h+r;
    end
    if ((k+r) > Y(2))
        Y(2) = k+r;
    end
    if ((h-r)<X(1))
        X(1) = h-r;
    end
    if ((k-r)<Y(1))
        Y(1) = k-r;
    end
%B. Le vecteur

    %plot( r*cos(t)+h, r*sin(t)+k ,'-');
    
%C. Le centre du cercle 

    %hold on;
    %plot( h, k,'+');
end

%D. Pour avoir des axes egaux

%axis equal;

%E. Valeurs propres 

ev=eig(A);
%for i=1:size(ev)
    %rev=plot(real(ev(i)),imag(ev(i)),'ro');
    %title('Cercle de Gershgorin')
    %xlabel('Axe reel')
    %ylabel('Axe Imaginaire')
%end
%hold off;
%legend(rev,'Valeurs propres');

end




function z =predcor(A,epsi,tol,machin)

    n = size(A,1);
    I = eye(n); %matrice identite 
    N = 1000; % Nombre d'itérations maxi
    z=zeros(N,1);
    vecteur = eig(A);
    j = sqrt(-1);
    hold on
    
    for k=1:length(eig(A))
    
        vp=vecteur(k);
        disp(vp)
        %%z = zeros(N,1);
        r = zeros(N,1);
        tau = zeros(N,1);

    
    %1ere etape, on determine z 
        z(1)=vp+sqrt(-1)*epsi; %on choisit une valeur propre de depart à laquelle on ajoute l'erreur   
        while((abs(svds((z(1)*I-A),1,'smallest')-epsi)/epsi)>tol)
 
            [umin,sigmin,vmin]=svds((z(1)*I-A),1,'smallest');           
            z(1)=z(1) -(sigmin-epsi)/(umin'*vmin); 
            
        end 
        
        flag = 1;
        i = 2;
    %2nd etape, on determine tous les zk et g(k)
        while(flag == 1 && i <N) 

            [umin,sigmin,vmin]=svds((z(i-1)*I-A),1,'smallest');
           if (i==2)
            disp(z(1))
            disp(umin)
            disp(vmin)
            disp(sigmin)
           end
    %3 eme etape, les rk qui correpondent à la direction de la trajectoire
            r(i)=(sqrt(-1)*vmin'*umin)/(abs(vmin'*umin)); 
            if (i==2)
            disp(r(i))
            end
    %4eme etape: on determine tau pour trouver le z final
            tau(i)=min(machin,abs(z(i-1)-vp)/2);
            z(i)=z(i-1)+(tau(i)*r(i));
            while((abs(svds((z(i)*I-A),1,'smallest')-epsi)/epsi)>tol)      
                
                [umin,sigmin,vmin]=svds((z(i)*I-A),1,'smallest'); 
                z(i)= z(i) -(sigmin-epsi)/(umin'*vmin);               
            end
            plot(real(z(i)),imag(z(i)),'x')
            if(abs(z(i)-z(1))<0.001*z(1))
                flag = 0;
            end
           
            i = i+1;
        end
    end
    axis('equal')
 hold off
end
    

