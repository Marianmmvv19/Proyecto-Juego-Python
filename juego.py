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
playerimg = pygame.image.load(asset_playerimg)

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
playerX_change = 0
playerY_change = 0

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

    #Se inicializan las varibles para guardar la posicion de la bala
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state= "ready"

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
    distance = math.sqrt((math.pow(enemyX - enemyY, 2)) +
                         (math.pow(enemyY-enemyX)))
    if distance < 27:
        return True
    else:
        return False
    
    #funcion para mostar el texto de game over en pantalla 
    def game_over_text():
    over_text= over_font.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(
        center=(int(screen_width/2), int(screen_height/2)))
    screen.blit(over_text, text_rect)
  
    #Función principl del Juego
    def gameloop():
    
    #Declarar variables globales
        global score
        global playerX
        global playerX_change
        global bulletX
        global bulletY
        global Collision
        global bullet_state

    in_game = True 
    while in_game:
        #Maneja eventos, actualiza y renderiza el juego 
        #Limpia la pantalla 
        screen.fill(0,0,0)
        screen.blit(background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False 
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOM:
                #Maneja el movimiento del jugador y el disparo 
                if event.key == pygame.K_LEFT:
                    playerX_change = -5

                if event.key == pygame.K_RIGHT:
                    playerY_change = 5
                
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                
                if event.type == pygame.KEYUP:
                    playerX_change = 0

        #Aquí se está actualizando la posicion del jugador 
        playerX +=  playerX_change
        if playerX <= 0:
           playerX = 0
        elif playerX >= 736:
            playerX = 736 
        
        #Aquí se está actualizando la posicion del jugador 
        playerX +=  playerX_change
        if playerX <= 0:
           playerX = 0
        elif playerX >= 736:
        
        #Bucle que se ejecuta para cada enemigo 
        for i in range(no_of_enemies):
            if enemyY[i] > 440:
                for j in range(no_of_enemies):
                    enemyY[j]=2000
                game_over_text()
            
            enemyX[i] += enemyX_change[i]

            if enemyX[i] <= 0:
                enemyX_change[i] = 5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -5 
                enemyY[i] += enemyY_change[i]
        
            #Aqui se comprueba si ha habido una colisión entre enemigo y una bala

            isCollision = isCollision(enemyX[i],enemyY[i], bulletX)
            if collison:
                bulletY=454
                bullet_state="ready"
                score += 1
                enemyX[i] = random.radiant(0,736)
                enemyY[i] = random.radiante(0, 150)
            enemy(enemyX[i], enemyY[i],i)

        if bulletY < 0:
            bulletY=454
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
        
        player(playerX, playerY)
        show_score()

        pygame.display.update()
        clock.tick(120)

gameloop()