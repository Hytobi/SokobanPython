#PLOUVIN Patrice NEUMAN Marine GUEVORTE Flavien
#Date :  29/11/2017
#L’implémentation des scénarios (niveaux du jeu)


#Import de Pygame
import pygame

#Autres import
from couleur import *
import grilles
import avatar
import caisse

#Constante
T_GRILLE = 30
QUITTER = 0         # Quitter le jeu.
RECOMMENCER = 1     # Recommencer le scénario.
CONTINUER = 2       # Continue.

#Légende:
DEST   = '.'   # Destination     
BOITE  = '$'   # Caisse          
MUR    = '#'   # Mur             
PERSO  = '@'   # Personnage      
VIDE   = ' '


#Initialisation
def init(num):
    '''Fonction qui initialise un niveau
       Argument : int
       Retour : dict'''
    #Dictionnaire des attributs du scénario
    att={}
    
    #L’avatar du joueur       
    att['joueur'] = None
    
    #La liste de caisses du scénario
    liste_caisses = []
    att['caisses'] = liste_caisses

    #Limiter les déplacements
    att['murs'] = []
    att['cible'] = []
    #une liste de listes de caractères.
    #Le caractère (i,j) de la grille doit correspondre
    #à un objet immobile du scénario (murs et destinations)
    att['grille'] = []
    att['grille'].append([])
    l = 0
    c = 0
    for elements in grilles.GRILLES[num]:
        if elements == '\n':
            att['grille'].append([])
            l += 1
            c = 0
        else:
            #Mur ou Destination:
            if elements == MUR:
                att['grille'][l].append(elements)
                att['murs'].append([l,c])
            elif elements == DEST:
                att['grille'][l].append(elements)
                att['cible'].append([l,c])
            #Personnage
            elif elements == PERSO:
                att['grille'][l].append(elements)
                att['joueur']=avatar.init(l, c, 0, att)
            #Caisse
            elif elements == BOITE:
                att['grille'][l].append(elements)
                ca = caisse.init(l, c)
                liste_caisses += [ca]                
            #Si c'est vide
            else:
                att['grille'][l].append(' ')
            c += 1
    
    return att



def dessine(surface, scen):
    '''Dessine le scénario.
       Arguments : surface, dict
       Retour : None'''
    # Reset de l'écrant
    surface.fill(NOIR)
    # Dessine la grille.
    l = 0
    #Pour chaque elements dans la grille
    for elem in scen['grille']:
        c = 0
        for j in elem:
            #Dessiner un mur
            if j == MUR:
                dessine_mur(surface, l, c)
            #Dessiner une cible
            elif j == DEST:
                dessine_cible(surface, l, c)
            #Dessiner une boite
            elif j == BOITE:
                for boite in range(len(scen['caisses'])):
                    caisse.dessine(scen['caisses'][boite], surface)
            #Dessiner le personnage
            elif j == PERSO:
                avatar.dessine(scen['joueur'], surface)
            c += 1
        l += 1



def dessine_mur(surface, l, c):
    '''Fonction qui dessine les murs
       Argument : surface, int, int
       Retour : None'''
    pygame.draw.rect(surface, MARRON, (c*T_GRILLE, l*T_GRILLE, T_GRILLE, T_GRILLE))



def dessine_cible(surface, l, c):
    '''Fonction qui dessine les cibles
       Argument : surface, int, int
       Retour : None'''
    pygame.draw.line(surface, GRIS, (c*T_GRILLE+2, l*T_GRILLE+2), (c*T_GRILLE+T_GRILLE-4, l*T_GRILLE+T_GRILLE-4), 2)
    pygame.draw.line(surface, GRIS, (c*T_GRILLE+T_GRILLE-4, l*T_GRILLE+2),(c*T_GRILLE+2, l*T_GRILLE+T_GRILLE-4), 2)



def traite_evt(scen):
    '''Traite les évènements.
       Arguments : dict
       Retour : int'''
    # Pour chaque évènement:
    for event in pygame.event.get():

        #L'utilisateur choisi de quitter
        if event.type == pygame.QUIT:
            pygame.quit()

        # Si une touche est appuyée:    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return QUITTER
            if event.key == pygame.K_r:
                return RECOMMENCER
            if event.key == pygame.K_RETURN:
                return CONTINUER
    return CONTINUER



#Est-ce que j’ai gagné ?
def caisses_sur_cible(caisse, cible):
    '''Fonction qui determiner si le niveau est fini
       Argument : dict dict
       Retour : bool'''
    caisse_place = 0
    for i in range(len(cible)):
        for j in range(len(caisse)):
            if cible[i][0]==caisse[j]['pos_l'] and cible[i][1]==caisse[j]['pos_c']:
                caisse_place += 1
    if caisse_place == len(cible):
        return True
    return False

def execute(scen):
    '''Exécute le scénario.
       Arguments : dict 
       Retour : int'''
    # Initialise l'horloge.
    horloge = pygame.time.Clock()
    
    # Boucle principale du scénario:
    result = CONTINUER
    terminer = False
    while not terminer:
                        
        #Faire bouger l'avatar
        avatar.update(scen['joueur'], scen['caisses'], scen['murs'])

        #Faire bouger la caisse
        caisse.update(scen['caisses'])
        
        result = traite_evt(scen)
        
##        # Si le joueur a décidé de quitter:
##        if result == QUITTER:
##            terminer = True
##
##        # Traite les évènements.
##        result = traite_evt(scen)
##        
##        if result == RECOMMENCER:
##            #Faire bouger l'avatar
##            avatar.update(scen['joueur'], scen['caisses'], scen['murs'])
##
##            #Faire bouger la caisse
##            caisse.update(scen['caisses'])
##        
            
        #Si niveau fini
        if caisses_sur_cible(scen['caisses'], scen['cible']):
            terminer = True
            
        # Dessine le scénario.
        surface = pygame.display.get_surface()
        dessine(surface, scen)
        
        # Met à jour l'écran.
        pygame.display.update()

        # Actualise l'horloge.
        horloge.tick(30)


    return result






    
