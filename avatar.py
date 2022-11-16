#PLOUVIN Patrice, NEUMAN Marine, GUEVORTE Flavien
#Date :
#L’implémentation de l’avatar du joueur


#Import de Pygame
import pygame

#Autres import
import scenario
from couleur import *

#Initialisation
def init(l, c, d, scen):
    '''Fonction qui initialise l'avatar
       Argument : int int int dict
       Retour : dict'''
    #Dictionnaire
    att={}

    #Ligne où se trouve l’avatar
    att['pos_l'] = l
    
    #Colonne où se trouve l’avatar
    att['pos_c'] = c

    #Direction
    #Ou il regarde 0 = haut, 1 = droite, 2 = bas et 3 = gauche
    att['direc'] = d

    #Vitesse de déplacement ligne
    att['vit_l'] = 1

    #Vitesse de déplacement colonne
    att['vit_c'] = 1

    #Dictionnaire des attributs d'un scenario
    att['scen'] = scen
    
    return att


#Dessin avatar
def dessine(att, surface):
    '''Fonction qui dessine le personnage
       Argument : dict, surface
       Retour : None'''
    pygame.draw.rect(surface, BLANC, (30*att['pos_c']+10, 30*att['pos_l']+10, 10, 10))
    
#Mise à jour de l'avatar
def update(perso, caisse, mur):
    '''Fonction qui met a jour le scénario
       Argument : dict dict
       Retour : None'''
    perso = avatar_evt(perso, caisse, mur)




def avatar_evt(perso, caisse, mur):
    '''Fonction qui traite le déplacement
       Argument : dict
       Retour : dict'''
    # Pour chaque évènement:
    for event in pygame.event.get():
        
##        #Si quit pygame
##        if event.type == pygame.QUIT:
##            pygame.quit()
        
        # Si une touche est appuyée:    
        if event.type == pygame.KEYDOWN:
            
            #Flèche gauche
            if event.key == pygame.K_LEFT:
                
                #Mouvement
                perso['pos_c'] -= perso['vit_l']
                perso['direc'] = 3
                
                #Si l'avatar est sur un mur
                if est_sur_mur(perso['pos_l'], perso['pos_c'], mur):
                    perso['pos_c'] += perso['vit_l']
                    
                for i in range(len(caisse)):
                                            
                    #Perso a droite de caisse
                    if perso['pos_c'] == caisse[i]['pos_c'] and perso['pos_l'] == caisse[i]['pos_l']:
                        caisse[i]['pos_c']-=1

                        #Si caisse n'est pas sur caisse
                        if est_sur_caisse(caisse[i]['pos_l'], caisse[i]['pos_c'], i, caisse) or est_sur_mur(caisse[i]['pos_l'], caisse[i]['pos_c'], mur):
                            #Empeche la caisse d'avancer
                            caisse[i]['pos_c']+=1
                            #Empeche le perso d'avancer
                            perso['pos_c'] += perso['vit_l']

                        
            #Flèche droite
            if event.key == pygame.K_RIGHT:

                #Mouvement
                perso['pos_c'] += perso['vit_l']
                perso['direc'] = 1
                
                #Si avatar est sur un mur
                if est_sur_mur(perso['pos_l'], perso['pos_c'], mur):
                    perso['pos_c'] -= perso['vit_l']
                    
                for i in range(len(caisse)):
                  #Perso a droite de caisse
                    if perso['pos_c'] == caisse[i]['pos_c'] and perso['pos_l'] == caisse[i]['pos_l']:
                        caisse[i]['pos_c']+=1

                        #Si caisse n'est pas sur caisse
                        if est_sur_caisse(caisse[i]['pos_l'], caisse[i]['pos_c'], i, caisse) or est_sur_mur(caisse[i]['pos_l'], caisse[i]['pos_c'], mur):
                            #Empeche la caisse d'avancer
                            caisse[i]['pos_c']-=1
                            #Empeche le perso d'avancer
                            perso['pos_c'] -= perso['vit_l']
                        
            #Flèche haut
            if event.key == pygame.K_UP:
                
                #Mouvement
                perso['pos_l'] -= perso['vit_c']
                perso['direc'] = 0
                
                #Si avatar est sur un mur
                if est_sur_mur(perso['pos_l'], perso['pos_c'], mur):
                    perso['pos_l'] += perso['vit_c']
                    
                for i in range(len(caisse)):
                    #Perso en dessous
                    if perso['pos_c'] == caisse[i]['pos_c'] and perso['pos_l'] == caisse[i]['pos_l']:
                        caisse[i]['pos_l']-=1

                        #Si caisse n'est pas sur caisse
                        if est_sur_caisse(caisse[i]['pos_l'], caisse[i]['pos_c'], i, caisse) or est_sur_mur(caisse[i]['pos_l'], caisse[i]['pos_c'], mur):
                            #Empeche la caisse d'avancer
                            caisse[i]['pos_l']+=1
                            #Empeche le perso d'avancer
                            perso['pos_l'] += perso['vit_c']

                            
            #Flèche bas
            if event.key == pygame.K_DOWN:
                #Mouvement
                perso['pos_l'] += perso['vit_c']
                perso['direc'] = 2
                
                #Si avatar est sur un mur
                if est_sur_mur(perso['pos_l'], perso['pos_c'], mur):
                    perso['pos_l'] -= perso['vit_c']
                    
                for i in range(len(caisse)):
                    #Perso au dessus
                    if perso['pos_c'] == caisse[i]['pos_c'] and perso['pos_l'] == caisse[i]['pos_l']:
                        caisse[i]['pos_l']+=1

                        #Si caisse n'est pas sur caisse
                        if est_sur_caisse(caisse[i]['pos_l'], caisse[i]['pos_c'], i, caisse) or est_sur_mur(caisse[i]['pos_l'], caisse[i]['pos_c'], mur):
                            #Empeche la caisse d'avancer
                            caisse[i]['pos_l']-=1
                            #Empeche le perso d'avancer
                            perso['pos_l'] -= perso['vit_c']
    return perso




#Limiter les déplacements
def est_sur_mur(l, c, scen):
    '''Fonction qui determine si a la position (l, c) il y à un mur
       Argument : int int dict
       Retour : bool'''
    int(l)
    int(c)
    for coor in range(len(scen)):
        if scen[coor][0]==l and scen[coor][1]==c :
            return True
    return False

def est_sur_caisse(l, c, valeur_interdite, scen):
    '''Fonction qui determine si a la position (l, c) il y à un mur
       Argument : int int int dict
       Retour : bool'''
    int(l)
    int(c)
    for coor in range(len(scen)):
        if scen[coor]['pos_l']==l and scen[coor]['pos_c']==c and valeur_interdite!=coor:
            return True
    return False
















    
