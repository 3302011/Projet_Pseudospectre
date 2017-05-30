function fin()

disp('Bonjour Monsieur et bienvenue dans la fonction Pseudospectre qui correspond au programme de Gershgorin:')

%%% Variables %%%

n = 3; %Taille de la matrice qu'il sera possible de changer 
A=ones(n,n);
eps=10; 

%%% Fonctions %%%
% 1. Premiere fonction Random
% Fonction qui va donner un nombre aleatoire pour les nombres reels
% et les nombres imaginaires 

j = sqrt(-1);
A = rand(n) + j*rand(n);
%2. Fonction qui va tracer le disque de Gershgorin

[X,Y] = gershdisc(A,eps)

%3. Fonction SVD qui va nous servir pour GRID
[U,S,V]=svd(A); 

%4. Fonction GRID
disp('sigmin:')
sigmin = grid1(A,X,Y,eps);

figure(1)
gershdisc(A,eps)
figure(2)
grid1(A,X,Y,eps)

end 

%%% Appel de fonctions %%%

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

function sigmin=grid1(A,X,Y,eps)

% X et Y contiennent la limite du rectangle

N=100; 
i=sqrt(-1); 
pasX = (X(2)-X(1))/(N-1);
pasY = (Y(2)-Y(1))/(N-1);
x = X(1):pasX:X(2);
y = Y(1):pasY:Y(2);
sigmin = zeros(N,N);

for k=1:N
    for j=1:N
        sigmin(j,k)=min(svd((x(k)+y(j)*i)*eye(size(A,1))-A)); 
    end 
end 
 
ev=eig(A);
hold on
for i=1:size(ev)
    rev=plot(real(ev(i)),imag(ev(i)),'ro');
end
contour(x,y,sigmin,[eps eps])
hold off

end 

