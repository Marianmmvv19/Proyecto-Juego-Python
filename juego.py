import pygame
import random 
import math 
import sys
import os

#Inicializar pygame
pygame.init()

#Establece el tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#Función para obtener la ruta de los recursos 
def resource_path(relative_path):
    try:
        base_path = sys._MIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
#Cargar imagen de fondo
asset_background = resource_path('assets/images/background.png')
background = pygame.image.load(asset_background)

    
#Cargar icono de ventana  
asset_icon = resource_path('assets/images/ufo.png')
background = pygame.image.load(asset_icon)

    
#Cargar sonido de fondo
asset_sound = resource_path('assets/images/background_music.png')
background = pygame.image.load(asset_sound)

#Cargar imagen del jugador
asset_playering = resource_path('assets/images/space-invaders.png')
background = pygame.image.load(asset_playering)

#Cargar imagen del bala 
asset_background = resource_path('assets/images/bullet.png')
background = pygame.image.load(asset_bulletimg)


#Cargar fuente para texto  de game over 
asset_over_font = resource_path('assets/fonts/RAVIE.TTF')
background = pygame.font.Font(asset_bulletimg)