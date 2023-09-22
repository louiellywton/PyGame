import pygame
import random

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

snake_color = (0, 128, 0)
food_color = (255, 0, 0)
snake_block_size = 20
snake_speed = 15

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 40)


def display_score(score):
    score_text = score_font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(score_text, [10, 10])


def game_loop():
    game_over = False
    game_exit = False

    snake_x = window_width / 2
    snake_y = window_height / 2
    snake_x_change = 0
    snake_y_change = 0

    snake_body = []
    snake_length = 1

    food_x = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
    food_y = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size

    score = 0

    while not game_exit:
        while game_over:
            window.fill((255, 255, 255))
            game_over_text = font_style.render("Game Over!", True, (255, 0, 0))
            window.blit(game_over_text, [window_width / 2 - 100, window_height / 2 - 50])
            score_text = font_style.render("Final Score: " + str(score), True, (0, 0, 0))
            window.blit(score_text, [window_width / 2 - 80, window_height / 2])
            play_again_text = font_style.render("Press P to Play Again or Q to Quit", True, (0, 0, 0))
            window.blit(play_again_text, [window_width / 2 - 180, window_height / 2 + 50])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block_size
                    snake_x_change = 0

        snake_x += snake_x_change
        snake_y += snake_y_change

        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_over = True

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over = True

        window.fill((255, 255, 255))
        pygame.draw.rect(window, food_color, [food_x, food_y, snake_block_size, snake_block_size])

        for segment in snake_body:
            pygame.draw.rect(window, snake_color, [segment[0], segment[1], snake_block_size, snake_block_size])

        display_score(score)

        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
            food_y = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size
            snake_length += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
