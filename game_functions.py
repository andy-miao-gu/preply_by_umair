import sys

import pygame
def check_events(ship):
     """Respond to keypresses and mouse events."""
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()
             
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
                 # Move the ship to the right.
                 ship.rect.centerx += 3    
             if event.key == pygame.K_LEFT:
                 # Move the ship to the right.
                 ship.rect.centerx -= 3            
                 
                 
                 
                 
def update_screen(ai_settings, screen, ship):
     pygame.display.flip()
     screen.fill(ai_settings.bg_color)
     ship.blitme()