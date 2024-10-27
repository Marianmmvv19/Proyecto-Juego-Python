import pygame
import random
import sys
import os

# Inicializar pygame
pygame.init()

# Tamaño de pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Función para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Ruta y carga de recursos gráficos y sonidos
background = pygame.image.load(resource_path('./images/background.png'))
icon = pygame.image.load(resource_path('./images/ufo.png'))
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invader")
pygame.mixer.music.load(resource_path('./audios/background_music.mp3'))
pygame.mixer.music.play(-1)

# Fuentes para texto
font = pygame.font.Font(resource_path('./fonts/comicbd.ttf'), 32)
over_font = pygame.font.Font(resource_path('./fonts/RAVIE.TTF'), 60)

# Configuración del jugador
playerimg = pygame.image.load(resource_path('./images/space-invaders.png'))
bulletimg = pygame.image.load(resource_path('./images/bullet.png'))
enemyimg = pygame.image.load(resource_path('./images/enemy1.png'))

playerX, playerY = 370, 480
playerX_change = 0
bulletX, bulletY, bullet_state = 0, 480, "ready"
score = 0

# Configuración de enemigos
num_of_enemies = 6
enemies = []
for i in range(num_of_enemies):
    enemies.append({
        "img": enemyimg,
        "x": random.randint(0, screen_width - 64),
        "y": random.randint(50, 150),
        "x_change": 2,  # Reducir velocidad de los enemigos
        "y_change": 40
    })

# Preguntas y respuestas para mostrar en colisión
questions = [
    {
        "question": "¿Cómo creas una lista en Python?",
        "options": ["lista = {}", "lista = []", "lista = ()", "lista = <>"],
        "answer": "lista = []"
    },
    {
        "question": "¿Cómo agregas un elemento a una lista?",
        "options": ["lista.push()", "lista.add()", "lista.append()", "lista.insert()"],
        "answer": "lista.append()"
    },
    {
        "question": "¿Cuál es la función para obtener la longitud de una lista?",
        "options": ["count()", "len()", "size()", "length()"],
        "answer": "len()"
    },
    # Agrega más preguntas si deseas
]

# Función para mostrar preguntas aleatorias en tarjeta oscura
def show_question():
    question_data = random.choice(questions)
    question = question_data["question"]
    options = question_data["options"]
    correct_answer = question_data["answer"]

    # Mezcla las opciones
    random.shuffle(options)
    
    # Fondo oscuro para la tarjeta
    pygame.draw.rect(screen, (0, 0, 0), (100, 100, 600, 400))
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 600, 400), 2)
    
    # Mostrar pregunta
    question_text = font.render(question, True, (255, 255, 255))
    screen.blit(question_text, (120, 140))

    # Mostrar opciones
    for i, option in enumerate(options):
        option_text = font.render(f"{i + 1}. {option}", True, (255, 255, 255))
        screen.blit(option_text, (120, 200 + i * 40))

    return question_data

# Función para comprobar la respuesta
def check_answer(selected_option, correct_answer):
    global score
    if selected_option == correct_answer:
        score += 10  # Ajusta los puntos a tu preferencia
    else:
        score -= 5  # Penalización si es incorrecta

# Función para mostrar puntuación
def show_score():
    score_value = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (10, 10))

# Función para detectar colisión
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = ((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2) ** 0.5
    return distance < 27

# Función principal del juego
def game_loop():
    global playerX, playerX_change, bulletX, bulletY, bullet_state, score

    in_game = True
    show_question_card = False
    selected_question = None
    question_shown = False  # Bandera para asegurarse de que solo se muestre una pregunta
    answered_question = False  # Bandera para asegurarse de que solo se responda una pregunta

    while in_game:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bulletX = playerX
                    bullet_state = "fire"
            if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change = 0

            # Eventos para responder preguntas
            if show_question_card and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_option = selected_question["options"][0]
                elif event.key == pygame.K_2:
                    selected_option = selected_question["options"][1]
                elif event.key == pygame.K_3:
                    selected_option = selected_question["options"][2]
                elif event.key == pygame.K_4:
                    selected_option = selected_question["options"][3]
                else:
                    continue
                
                check_answer(selected_option, selected_question["answer"])
                show_question_card = False
                answered_question = True  # Marcar que la pregunta ha sido respondida

        # Actualizar posición del jugador y bala
        playerX += playerX_change
        playerX = max(0, min(playerX, 736))

        if bulletY < 0:
            bulletY, bullet_state = 480, "ready"

        if bullet_state == "fire":
            bulletY -= 10
            screen.blit(bulletimg, (bulletX + 16, bulletY + 10))

        # Enemigos
        for enemy in enemies:
            # Movimiento enemigo
            enemy['x'] += enemy['x_change']
            if enemy['x'] <= 0 or enemy['x'] >= screen_width - 64:
                enemy['x_change'] *= -1
                enemy['y'] += enemy['y_change']

            # Detectar colisión
            collision = is_collision(enemy['x'], enemy['y'], bulletX, bulletY)
            if collision and not question_shown and not answered_question:  # Solo mostrar una pregunta por colisión y una vez
                bulletY, bullet_state = 480, "ready"
                score += 1
                show_question_card = True
                selected_question = show_question()
                question_shown = True  # Marcar que se ha mostrado una pregunta

            screen.blit(enemy['img'], (enemy['x'], enemy['y']))

        # Mostrar puntuación y jugador
        show_score()
        screen.blit(playerimg, (playerX, playerY))

        # Mostrar tarjeta de pregunta si hay colisión
        if show_question_card and not answered_question:
            show_question()

        # Reiniciar después de responder
        if answered_question:
            question_shown = False  # Se puede mostrar una nueva pregunta
            answered_question = False  # Esperar una nueva colisión

        pygame.display.update()

game_loop()
