import pygame
from pygame.locals import *
import random
import time
 #initialising pygame
pygame.init()
clock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((width, height))
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]
#defualt snake position
snake_position = [100, 50]
#initial score
score = 0

my_font = pygame.font.SysFont('times new roman', 50)
#default direction
change_to = 'RIGHT'
#positioning the snake_food
food_position = [random.randrange(1, 50) * 10,
                random.randrange(1, 50) * 10]
# method to check for collision
def check_collision():
    if (snake_position[0] < 0 or snake_position[0] > width) or (snake_position[1] < 0 or snake_position[1] > height):
        return True
    for segment in snake_body[1:]:
        if snake_body[0] == segment:
            return True
    return False
# Gameover method
def game_over():
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width/2, height/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    quit()


#game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                change_to = 'UP'
            if event.key == K_DOWN:
                change_to = 'DOWN'
            if event.key == K_LEFT:
                change_to = 'LEFT'
            if event.key == K_RIGHT:
                change_to = 'RIGHT'
    
    # this should not be nested in input handling
    # moving the snake
    if change_to == 'UP':
        snake_position[1] -= 10
    if change_to == 'DOWN':
        snake_position[1] += 10
    if change_to == 'LEFT':
        snake_position[0] -= 10
    if change_to == 'RIGHT':
        snake_position[0] += 10  # not snake_body
    
    snake_body.insert(0, list(snake_position))  # list to avoid mutabilities issues
    # increasing the lenght of the snake as it eat
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        score += 10
        snake_body.append((0, 0))
    if snake_position[0] != food_position[0]:
        snake_body.pop()

    screen.fill((0, 0, 0))  # fill the screen with black before drawing, as if erasing previous drawing
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), Rect(pos[0], pos[1], 10, 10))
    
    
    if check_collision():
        game_over()

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(food_position[0], food_position[1], 10, 10))
    pygame.display.update()
    clock.tick(5)