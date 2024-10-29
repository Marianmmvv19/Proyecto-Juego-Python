import pygame
import random
import math
import sys
import os

# Inicializar pygame
pygame.init()

# Establecer tamaño de pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Definir preguntas y respuestas
questions = [
    {"question": "¿Cómo declarar una lista en Python?", "options": ["1. list = []", "2. list = {}", "3. list = ()"], "answer": 1},
    {"question": "¿Cómo agregar un elemento a una lista?", "options": ["1. list.append(elemento)", "2. list.add(elemento)", "3. list.insert(elemento)"], "answer": 1},
    {"question": "¿Cuál es el bucle para iterar una lista?", "options": ["1. while", "2. for", "3. foreach"], "answer": 2},
]
current_question = None
show_question = False

# Función para mostrar pregunta y opciones
def display_question():
    question_font = pygame.font.Font(None, 28)
    question_text = question_font.render(current_question["question"], True, (255, 255, 255))
    screen.blit(question_text, (50, 50))

    for i, option in enumerate(current_question["options"]):
        option_text = question_font.render(option, True, (255, 255, 255))
        screen.blit(option_text, (50, 100 + i * 30))

# Función para verificar respuesta
def check_answer(selected_option):
    global show_question, current_question, score
    if selected_option == current_question["answer"]:
        score += 5  # Añadir puntos si es correcto
    show_question = False
    current_question = None

# Función para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Cargar imagen de fondo
background = pygame.image.load(resource_path('./images/background.png'))

# Cargar icono de ventana
icon = pygame.image.load(resource_path('./images/ufo.png'))
pygame.display.set_icon(icon)

# Cargar sonido de fondo
pygame.mixer.music.load(resource_path('./audios/background_music.mp3'))
pygame.mixer.music.play(-1)  # Reproducir en bucle

# Cargar imagen del jugador
playerimg = pygame.image.load(resource_path('./images/space-invaders.png'))

# Cargar imagen de la bala
bulletimg = pygame.image.load(resource_path('./images/bullet.png'))

# Cargar fuente para texto de puntaje
font = pygame.font.Font(None, 32)

# Variables del jugador y balas
playerX = 370
playerY = 470
playerX_change = 0
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

# Variables del enemigo
enemyimg = [pygame.image.load(resource_path('./images/enemy1.png')) for _ in range(5)]
enemyX = [random.randint(0, 736) for _ in range(5)]
enemyY = [random.randint(50, 150) for _ in range(5)]
enemyX_change = [5] * 5
enemyY_change = [20] * 5

# Puntuación inicial
score = 0

# Función para mostrar la puntuación en pantalla
def show_score():
    score_value = font.render("SCORE " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (10, 10))

# Función para dibujar al jugador
def player(x, y):
    screen.blit(playerimg, (x, y))

# Función para dibujar al enemigo
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

# Función para disparar la bala
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

# Función para detectar colisión
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    return distance < 27

# Función principal del juego
def game_loop():
    global playerX, playerX_change, bulletX, bulletY, bullet_state, score, show_question, current_question

    in_game = True
    while in_game:
        # Limpiar pantalla
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not show_question:
                    if event.key == pygame.K_LEFT:
                        playerX_change = -5
                    if event.key == pygame.K_RIGHT:
                        playerX_change = 5
                    if event.key == pygame.K_SPACE and bullet_state == "ready":
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                else:
                    # Responder pregunta
                    if event.key == pygame.K_1:
                        check_answer(1)
                    elif event.key == pygame.K_2:
                        check_answer(2)
                    elif event.key == pygame.K_3:
                        check_answer(3)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Actualizar posición del jugador
        playerX += playerX_change
        playerX = max(0, min(playerX, 736))

        # Movimiento enemigo
        for i in range(len(enemyimg)):
            if enemyY[i] > 440:
                return  # Termina el juego si un enemigo llega a la parte inferior

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -5
                enemyY[i] += enemyY_change[i]

            # Colisión
            if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
                bulletY = 480
                bullet_state = "ready"
                score += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

                # Mostrar pregunta aleatoria
                current_question = random.choice(questions)
                show_question = True
            
            enemy(enemyX[i], enemyY[i], i)

        # Movimiento de la bala
        if bulletY < 0:
            bulletY = 480
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        # Dibujar jugador y mostrar puntuación
        player(playerX, playerY)
        show_score()

        # Mostrar pregunta si está activa
        if show_question:
            display_question()

        # Actualizar pantalla
        pygame.display.update()
        pygame.time.Clock().tick(60)

game_loop()