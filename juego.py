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
asset_sound = resource_path('assets/images/background_music.mp3')
background = pygame.image.load(asset_sound)

#Cargar imagen del jugador
asset_playerimg = resource_path('assets/images/space-invaders.png')
playerimg = pygame.image.load(asset_playering)

#Cargar imagen del bala 
asset_bulletimg = resource_path('assets/images/bullet.png')
bulletimg = pygame.image.load(asset_bulletimg)


#Cargar fuente para texto  de game over 
asset_over_font = resource_path('assets/fonts/RAVIE.TTF')
over_font= pygame.font.Font(asset_over_font)

#Cargar fuente para texto de puntaje 
asset_font = resource_path('assets/fonts/comicbd.ttf')
font = pygame.font.Font(asset_font)

#Establecer titulo de ventana
pygame.display.set_caption("Space Invader")

#Establecer icono de la ventana 
pygame.mixer.musicplay(-1)

#Crear reloj para controlar la velocidad del juego 
clock = pygame.time.Clock()

#Posicion inicial del jugador
playerX = 370
playerY = 470
player_change = 0
player_change = 0

#Lista para almacenar posiciones del enemigo 
enemyimg=[]
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

#Se inicializa las variables para guaradar las posiciones del enemigo
for i in range(no_of_enemies):

    #Se carga la imagen del enemigo 1 
    enemy1 = resource_path('assets/images/enemy1.png')
    enemyimg.append(pygame.image.load(enemy1))

    #Se carga la imagen del enemigo 2 
    enemy2 = resource_path('assets/images/enemy2.png')
    enemyimg.append(pygame.image.load(enemy2))

    #Se asigna una posición aleatoria en X y Y para el enemigo
    enemyX.append(random.randit(0,736))
    enemyX.append(random.randit(0,150))

    #Se establece la velocidad de movimiento del enemigo en X y Y 
    enemyX_change.append(5)
    enemyY_change.append(20)

    #Se inicializa la puntuacion en 0 
    score = 0 

    #funcion para mostar la puntuación en la pantalla 
    def show_score():
        score_value = font.render("SCORE " + str(score), True, (255, 255, 255))
        screen.blit(score_value, (10,10))
    
    #funcion para dibujar el jugador en la pantalla 
    def player(x ,y):
        screen.blit(playerimg, (x ,y))
    
    #funcion para dibujar el jugador enemigo en la pantalla 
    def player(x ,y):
        screen.blit(playerimg[i], (x ,y))

   #funcion para disparar la bala
   def fire_bullet(x,y):
    global bullet_state

    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y + 10))
  
  #funcion para observar si ha habido una colisión entre la bala y el enemigo 
  def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyx - enemyY, 2)) +
                         (math.pow(enemyY-enemyX)))
    if distance < 27:
        return True
    else:
        return False
    

       
    


    
    

