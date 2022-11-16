#PLOUVIN Patrice, GUEVORTE Flavien, NEUMAN Marine
#Date : 29/11/2017
#La fonction principale du programme

#Import de pygame
import pygame

#Autre import
import ouverture
import scenario
import grilles
import avatar
import caisse
from couleur import *

#Constante
N_SCENARIOS = len(grilles.GRILLES)
def main():
    '''Fonction principale du programme
       Argument : None
       Retour : None'''
    #1 Initialise Pygame
    pygame.init()

    #2 Ouvre la fenêtre de l'application
    surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Sokoban')

    #3 Exécute l’ouverture du jeu
    continuer = ouverture.execute(surface)
    #if not continuer:
        #return
    if continuer == False:
        pygame.quit()
    # Tant que le programme n’est pas terminé :
    terminer = False
    num_niveau = 0
    while not terminer :

            
        # Init le scénario
        scen = scenario.init(num_niveau)  #num_niveau

        # Exécution du scénario
        res = scenario.execute(scen)
            
        # Niveau suivant
        num_niveau += 1
            
        # Si c'est le dernier niveau
        if num_niveau >= N_SCENARIOS:
            terminer = True


    #5 Termine Pygame.
    pygame.quit()

# Appel à la fonction principale.
if __name__ == '__main__':
    main()
