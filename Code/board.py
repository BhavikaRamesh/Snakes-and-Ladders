import pygame
import random
import time

pygame.init()

pygame.display.set_caption("Snakes and Ladders")

white = (255, 0, 255) 
  
X = 1500
Y = 800
display_surface = pygame.display.set_mode((X, Y )) 
Board = pygame.image.load("C:/Users/Harshini R/Desktop/dice/sl.png")

while True : 
        display_surface.fill(white) 
        display_surface.blit(Board, (0, 0))
                    
        for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                        pygame.quit()  
                        quit() 
                pygame.display.update()  
