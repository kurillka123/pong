import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Пинг-Понг")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Параметры игры
ball_speed = [5, 5]
ball_radius = 20
paddle_width, paddle_height = 10, 100
left_paddle_pos = [30, height // 2 - paddle_height // 2]
right_paddle_pos = [width - 30 - paddle_width, height // 2 - paddle_height // 2]
ball_pos = [width // 2, height // 2]

# Функция для отображения меню
def show_menu():
    font = pygame.font.Font(None, 74)
    title = font.render("Пинг-Понг", True, WHITE)
    start_text = font.render("Начать", True, WHITE)

    while True:
        screen.fill(BLACK)
        screen.blit(title, (width // 2 - title.get_width() // 2, height // 2 - 100))
        screen.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Нажмите Enter для начала игры
                    return

        pygame.display.flip()

# Основная игра
def main_game():
    global ball_pos, ball_speed, left_paddle_pos, right_paddle_pos

    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        
        # Управление левой ракеткой
        if keys[pygame.K_w] and left_paddle_pos[1] > 0:
            left_paddle_pos[1] -= 10
        if keys[pygame.K_s] and left_paddle_pos[1] < height - paddle_height:
            left_paddle_pos[1] += 10

        # Управление правой ракеткой
        if keys[pygame.K_UP] and right_paddle_pos[1] > 0:
            right_paddle_pos[1] -= 10
        if keys[pygame.K_DOWN] and right_paddle_pos[1] < height - paddle_height:
            right_paddle_pos[1] += 10

        # Движение мяча
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # Отскок от верхней и нижней границ
        if ball_pos[1] <= ball_radius or ball_pos[1] >= height - ball_radius:
            ball_speed[1] = -ball_speed[1]

        # Отскок от ракеток
        if (left_paddle_pos[0] < ball_pos[0] < left_paddle_pos[0] + paddle_width and
                left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[1] + paddle_height) or \
           (right_paddle_pos[0] < ball_pos[0] < right_paddle_pos[0] + paddle_width and
                right_paddle_pos[1] < ball_pos[1] < right_paddle_pos[1] + paddle_height):
            ball_speed[0] = -ball_speed[0]

        # Если мяч уходит за границы
        if ball_pos[0] < 0 or ball_pos[0] > width:
            ball_pos = [width // 2, height // 2]  # Сброс мяча в центр

        # Отображение
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (*left_paddle_pos, paddle_width, paddle_height))
        pygame.draw.rect(screen, WHITE, (*right_paddle_pos, paddle_width, paddle_height))
        pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

        pygame.display.flip()
        clock.tick(60)

# Главный цикл
while True:
    show_menu()
    main_game()