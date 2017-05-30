from tkinter import *
import subprocess as sp
from easygui import *
import os
import sys
from math import * #pour la barre de progression
import time 


######## PRESENTATION #######
msgbox("Bonjour et bienvenue dans la modélisation des pseudospectres crée par Alexia ZOUNIAS-SIRABELLA, Inès BENZENATI et Fatine BENTIRES ALJ. Deux méthodes de représentation sont disponibles: GRID et Prédiction-Correction.")

####### GRID OU PREDICTION CORRECTION #######
choices=["Voir GRID","Voir la partie Prédiction-correction"]
reply=buttonbox(image="pho.gif",msg="Que voulez vous faire?",title="Pseudospectre d'une matrice",choices=choices)


################# GRID ####################

if reply==choices[0]:
    
    msgbox("Bienvenue dans la partie GRID!")
    choices=["Lire la documentation","Lancer le programme !", "Exit"]
    reply=buttonbox(image="homer.gif",msg="ET maintenant?",title="Pseudospectre d'une matrice",choices=choices)


########## choix 1 = lire la doc #############

    
    if reply=="Lire la documentation":
        os.system("Open Ps.pdf")

        choix=["Oui","Exit"]
        reponse=choicebox("On va quand même pas s'arrêter là... on lance le programme?",choices=choix)
        
        if reponse==choix[0]:
            cho=["Python","Matlab"]
            reply=buttonbox(image="now.gif",msg="Plutôt Python ou plutôt Matlab?",title="Va falloir se décider",choices=cho)
            
            if(reply==cho[1]):
                os.system("open -a fin.m")
            
            else:
                fields=["Taille de la matrice","Epsilon","Nombre de points"]
                msgbox("Un bon exemple serait de choisir une matrice de taille 10 avec un Epsilon égal à 5 et 100 points. Vous pouvez zoomer avec la loupe.")
                n=multenterbox(msg="Afin de personnaliser votre pseudospectre",title="Variables pour lancer le programme",fields=fields,values=())
                os.system("Python3 gersh.py"+" "+n[0]+" "+n[1]+" "+n[2])
            
                msgbox("Pour choisir de nouveau toutes les valeurs tapez sur Relancer, pour ne choisir que le nombre de points tapez sur Retracer. Si vous voulez quitter le programme tapez sur Exit.")
                fields=["Relancer","Retracer de façon plus précise","Exit"]
                res=buttonbox(image="stay.gif",msg="Décidemment, on veut pas vous lâcher !",title="Toujours plus!",choices=fields)
               
                while res==fields[0] or res==fields[1]:
                    
                    fields=["Relancer","Retracer de façon plus précise","Exit"]
                    res=buttonbox(image="stay.gif",msg="Décidemment, on veut pas vous lâcher !",title="Toujours plus!",choices=fields)

                    if res==fields[0]:
                        f=["Taille de la matrice","Epsilon","Nombre de points"]
                        n=multenterbox(msg="Afin de personnaliser votre pseudospectre",title="Variables pour lancer le programme",fields=f,values=())
                        os.system("Python3 gersh.py"+" "+n[0]+" "+n[1]+" "+n[2])

                    if res==fields[1]:
                        s=enterbox(msg="Donnez le nombre de points",title="",default="")
                        os.system("Python3 gersh.py" + " " + n[0] + " "+ n[1] + " " + s)
                    
                if res=="Exit":
                    c=["Exit"]
                    buttonbox(image="done.gif",msg="",choices=c)

######### choix 2 : lancer le programme ###########

    if reply==choices[1]:
 
        choic=["Python","Matlab"]
        reply=buttonbox(image="now.gif",msg="Plutôt Python ou plutôt Matlab?",title="Va falloir se décider",choices=choic)
        

######## si Matlab ##########

        if(reply==choic[1]):
            os.system("open -a MATLAB_R2016b")
            
####### si Python #############

        else:    
            msgbox("Un bon exemple serait de choisir une matrice de taille 10 avec un Epsilon égal à 5 et 100 points. Vous pouvez zoomer avec la loupe.")
            fields=["Taille de la matrice","Epsilon","Nombre de points"]
            n=multenterbox(msg="Afin de personnaliser votre pseudospectre",title="Variables pour lancer le programme",fields=fields,values=())
            os.system("Python3 gersh.py"+" "+n[0]+" "+n[1]+" "+n[2])

            msgbox("Pour choisir de nouveau toutes les valeurs tapez sur Relancer. Si vous voulez quitter le programme tapez sur Exit.")
            fields=["Relancer","Exit"]
            res=buttonbox(image="stay.gif",msg="Décidemment, on veut pas vous lâcher !",title="Toujours plus!",choices=fields)
            
            while res==fields[0]:
                fields=["Relancer","Exit"]
                res=buttonbox(image="stay.gif",msg="Décidemment, on veut pas vous lâcher !",title="Toujours plus!",choices=fields)

                if res==fields[0]:
                    fie=["Taille de la matrice","Epsilon","Nombre de points"]
                    n=multenterbox(msg="Afin de personnaliser votre pseudospectre",title="Variables pour lancer le programme",fields=fie,values=())
                    os.system("Python3 gersh.py"+" "+n[0]+" "+n[1]+" "+n[2])
            
            if res=="Exit":
                c=["Exit"]
                buttonbox(image="done.gif",msg="",choices=c)
    

    else:
        c=["Exit"]
        buttonbox(image="done.gif",msg="",choices=c)



##################### PREDICTION CORRECTION #################################

if reply=="Voir la partie Prédiction-correction":
    msgbox("Bienvenue dans la partie prediction-correction!")
    choices=["Lire la documentation","Lancer le programme !", "Exit"]
    reply=buttonbox(image="homer.gif",msg="ET maintenant?",title="Pseudospectre d'une matrice",choices=choices)


########## choix 1 = lire la doc #############                                                                                                                            

    if reply=="Lire la documentation":
        os.system("Open Ps.pdf")

        choix=["Oui","Exit"]
        reponse=choicebox("On va quand même pas s'arrêter là... on lance le programme?",choices=choix)

        if reponse==choix[0]:
            cho=["Python","Matlab"]
            reply=buttonbox(image="now.gif",msg="Plutôt Python ou plutôt Matlab?",title="Va falloir se décider",choices=cho)

            if(reply==cho[1]):
                os.system("open -a friend.m")

            else:
                fields=["Taille de la matrice","Epsilon","Différence entre les valeurs propres"]
                msgbox("Un bon exemple serait de choisir une matrice de taille 3 avec un Epsilon égal à 0.1. Vous pouvez zoomer avec la loupe.")
                n=multenterbox(msg="Afin de personnaliser votre pseudospectre",title="Variables pour lancer le programme",fields=fields,values=())
                os.system("Python3 prog.py"+" "+n[0]+" "+n[1]+" "+str(1)+" "+n[2])
                
                f=["Relancer après zoom","Exit"]
                res=buttonbox(msg="Relancer après zoom?",title="Zoom",choices=f)

                if res==f[0]:
                    os.system("Python3 prog.py"+" "+n[0]+" "+n[1]+" "+str(0)+" "+n[2])#on relance 
                
                fields=["Relancer","Exit"]
                res=buttonbox(image="stay.gif",msg="Décidemment, on veut pas vous lâcher !",title="Toujours plus!",choices=fields)

                while res==fields[0]:
                    
                    f=["Taille de la matrice","Epsilon","Différence entre les valeurs propres"]
                    n=multenterbox(msg="Afin de personnaliser votre pseudospectre",title="Variables pour lancer le programme",fields=f,values=())
                    os.system("Python3 prog.py"+" "+n[0]+" "+n[1]+" "+str(1)+" "+n[2])

                    
                if res=="Exit":
                    c=["Exit"]
                    buttonbox(image="done.gif",msg="",choices=c)

######### choix 2 : lancer le programme ###########             

    if reply==choices[1]:

        choic=["Python","Matlab"]
        reply=buttonbox(image="now.gif",msg="Plutôt Python ou plutôt Matlab?",title="Va falloir se décider",choices=choic)


######## si Matlab ##########                                                                                                                                                                           

        if(reply==choic[1]):
            os.system("open -a MATLAB_R2016b")

####### si Python #############                                                                                                                                                                         

        else:
            msgbox("Un bon exemple serait de choisir une matrice de taille 3 avec un Epsilon égal à 0.1. Vous pouvez zoomer avec la loupe.")
            fields=["Taille de la matrice","Epsilon","Différence entre les valeurs propres"]
            n=multenterbox(msg="Afin de personnaliser votre pseudospectre",title="Variables pour lancer le programme",fields=fields,values=())
            
            f=["Lancer avec possibilité de relancer après le zoom","Lancer sans option zoom","Exit"]
            res=buttonbox(msg="Dilemme, avec ou sans zoom? Telle est la question",title="Zoom",choices=f)

            if res==f[0]:
                os.system("Python3 prog.py"+" "+n[0]+" "+n[1]+" "+str(0)+" "+n[2])            

                msgbox("Pour choisir de nouveau toutes les valeurs tapez sur Relancer. Si vous voulez quitter le programme tapez sur Exit.")
                fields=["Relancer","Exit"]
                res=buttonbox(image="stay.gif",msg="Décidemment, on veut pas vous lâcher !",title="Toujours plus!",choices=fields)
                while res==fields[0]:
                    
                    fie=["Taille de la matrice","Epsilon"]
                    n=multenterbox(msg="Afin de personnaliser votre pseudospectre",title="Variables pour lancer le programme",fields=fie,values=())
                    os.system("Python3 prog.py"+" "+n[0]+" "+n[1]+" "+str(1)+" "+n[2])

                    if res=="Exit":
                        c=["Exit"]
                        buttonbox(image="done.gif",msg="",choices=c)
            
            if res==f[1]:            
                os.system("Python3 prog.py"+" "+n[0]+" "+n[1]+" "+str(1)+" "+n[2]) #matrice, epsilon, on

            else:
                c=["Exit"]
                buttonbox(image="done.gif",msg="",choices=c)
                        
                        




############ choix 3 : quitter le programme ################                                                                                                                                            

    elif reply==choices[2]:
        c=["Exit"]
        buttonbox(image="done.gif",msg="",choices=c)




