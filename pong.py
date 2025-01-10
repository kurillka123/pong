import pygame
import sys
import random

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
ball_radius = 15
paddle_width, paddle_height = 10, 100
left_paddle_pos = [30, height // 2 - paddle_height // 2]
right_paddle_pos = [width - 30 - paddle_width, height // 2 - paddle_height // 2]
ball_pos = [width // 2, height // 2]

# Функция отрисовки меню
def draw_menu():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    title_text = font.render("Пинг-Понг", True, WHITE)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 50))

    font = pygame.font.Font(None, 36)

    # Кнопка "Начать игру"
    play_button = font.render("Начать игру", True, WHITE)
    play_button_rect = play_button.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(play_button, play_button_rect)

    # Кнопка "Авто игра"
    auto_button = font.render("Авто игра", True, WHITE)
    auto_button_rect = auto_button.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(auto_button, auto_button_rect)

    pygame.display.flip()
    return play_button_rect, auto_button_rect

# Основная игра
def main_game(auto=False):
    global ball_pos, ball_speed, left_paddle_pos, right_paddle_pos
    ball_pos = [width // 2, height // 2]
    ball_speed = [5, 5]
    left_paddle_pos[1] = height // 2 - paddle_height // 2
    right_paddle_pos[1] = height // 2 - paddle_height // 2
    
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Управление левой ракеткой (игрок)
        if keys[pygame.K_w] and left_paddle_pos[1] > 0:
            left_paddle_pos[1] -= 10
        if keys[pygame.K_s] and left_paddle_pos[1] < height - paddle_height:
            left_paddle_pos[1] += 10

        # Автоигра для правой ракетки
        if auto:
            if ball_pos[1] < right_paddle_pos[1]:
                right_paddle_pos[1] -= 5
            if ball_pos[1] > right_paddle_pos[1] + paddle_height:
                right_paddle_pos[1] += 5

        # Движение мяча
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # Отскок от верхней и нижней границ
        if ball_pos[1] <= ball_radius or ball_pos[1] >= height - ball_radius:
            ball_speed[1] = -ball_speed[1]

        # Отскок от ракеток
        if (left_paddle_pos[0] < ball_pos[0] < left_paddle_pos[0] + paddle_width and
            left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[1] + paddle_height) or (
            right_paddle_pos[0] < ball_pos[0] < right_paddle_pos[0] + paddle_width and
            right_paddle_pos[1] < ball_pos[1] < right_paddle_pos[1] + paddle_height):
            ball_speed[0] = -ball_speed[0]

        # Если мяч уходит за границы
        if ball_pos[0] < 0 or ball_pos[0] > width:
            ball_pos = [width // 2, height // 2]  # Сброс мяча в центр
            ball_speed[0] = -ball_speed[0]  # Сброс скорости мяча
        
        # Отображение
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (*left_paddle_pos, paddle_width, paddle_height))
        pygame.draw.rect(screen, WHITE, (*right_paddle_pos, paddle_width, paddle_height))
        pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

        pygame.display.flip()
        clock.tick(60)

# Главная функция
def main():
    play_button_rect, auto_button_rect = draw_menu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_button_rect.collidepoint(mouse_pos):
                    main_game(auto=False)
                elif auto_button_rect.collidepoint(mouse_pos):
                    main_game(auto=True)

if __name__ == "__main__":
    main()