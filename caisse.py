#PLOUVIN Patrice, NEUMAN Marine, GUEVORTE Flavien
#Date : 09/12/2017
#L’implémentation d’une caisse


#Import de Pygame
import pygame

#Autres import
import scenario
from couleur import *

#Initialisation
def init(l, c):
    '''Fonction qui initialise la caisse
       Argument : int int 
       Retour : dict'''
    #Dictionnaire
    att={}

    #Ligne où se trouve la caisse
    att['pos_l'] = int(l)
    
    #Colonne où se trouve la caisse
    att['pos_c'] = int(c)

    #Vitesse de déplacement ligne
    att['vit_l'] = -1

    #Vitesse de déplacement colonne
    att['vit_c'] = 0

    return att


#Dessin caisse
def dessine(att, surface):
    '''Fonction qui dessine les caisses
       Argument : dict, surface
       Retour : None'''
    pygame.draw.rect(surface, BLEU, (30*att['pos_c']+2, 30*att['pos_l']+2, 26, 26))
    

#Mise à jour
def update(liste):
    '''Met à jour les caisses
       Argument : liste de dict
       Retour : liste de dict'''
    for i in range(len(liste)):
        if liste[i]['vit_c'] == 0:
            liste[i]['pos_c']+=1
        elif liste[i]['vit_l']== -1:
            liste[i]['pos_l']-=1

        if liste[i]['vit_l']==1:
            liste[i]['pos_l']+=1
        elif liste[i]['vit_l']==-1:
           liste[i]['pos_c']-=1



    



    
