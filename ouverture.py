#PLOUVIN Patrice, NEUMAN Marine, GUEVORTE Flavien
#Date : 29/11/2017
#L’implémentation de l’ouverture du jeu



#Import de pygame
import pygame

#Autre import
from couleur import *


#5 Module Ouverture
def execute(surface) :
    '''Fonction qui execute l’ouverture du jeu.
       Argument : surface
       Retour : bool.'''
    #1) Dessiner l’ouverture du jeu
    dessine(surface)
    
    #2) Met à jour l'écran.
    pygame.display.update()
    
    #3) Tant que l’ouverture n’est pas terminée:
    terminer = False
    continuer = False
    while not terminer:
        #a)Traite les événements de l’utilisateur (par la boucle habituelle)
        for event in pygame.event.get() :
        #b) Si le joueur clique sur quitter.
            if event.type == pygame.QUIT :
                continuer = False
                terminer = True
        #Si une touche est préssée
            if event.type == pygame.KEYDOWN:
        #c) Si le joueur appuie sur ESC.
                if event.key == pygame.K_ESCAPE :
                    continuer = False
                    terminer = True
        #d) Si le joueur appuie sur ENTRER.
                if event.key == pygame.K_RETURN :
                    continuer = True
                    terminer = True
    return continuer



def dessine(surface):
    '''Fonction qui dessine l’écrant d'ouverture du jeu.
       Argument : surface
       Retour : None'''
    #Titre du jeu en grandes lettres.
    police = pygame.font.Font(None, 130)
    police1 = pygame.font.Font(None, 130)
    texte = police.render('Sokoban', True, BLANC)
    texte2 = police1.render('Sokoban', True, ROUGE)
    surface.blit(texte, [250, 150])
    surface.blit(texte2, [255, 150])
    
    #Date de création du jeu.
    police_0 = pygame.font.Font(None, 25)
    texte = police_0.render('jeu créé le : 27/11/2017', True, BLANC)
    surface.blit(texte, [355, 320])
    
    #Noms des auteurs.
    police_1 = pygame.font.Font(None, 30)
    texte = police_1.render('NEUMAN Marine, PLOUVIN Patrice, GUEVORTE Flavien', True, BLANC)
    surface.blit(texte, [200, 340])
    
    #Discipline.
    police_2 = pygame.font.Font(None, 25)
    texte = police_2.render('Algorithme et programmation 1', True, BLANC)
    surface.blit(texte, [320, 360])
    
    #Institution.
    police_3 = pygame.font.Font(None, 25)
    texte = police_3.render('Université d’Artois', True, BLANC)
    surface.blit(texte, [360, 380])
    
    #Item Instructions pour le joueur.
    police_4 = pygame.font.Font(None, 20)
    texte = police_4.render('ENTRER pour commencer, ESC pour quitter', True, BLANC)
    surface.blit(texte, [290, 450])
