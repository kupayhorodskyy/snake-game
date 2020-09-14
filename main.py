import random
import pygame
import math

pygame.init()
pygame.display.set_caption("Snake")


clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))

snake = [
    [60, 300],
    [40, 300],
    [20, 300]
]

apple_color = (214, 21, 21)
apple_x = random.randint(0, 780)
apple_y = random.randint(0, 580)

snake_color = (0, 117, 14)
xChange = 0
yChange = 0


def draw_snake():
    for block in snake:
        pygame.draw.rect(screen, snake_color, (block[0], block[1], 20, 20))


def draw_apple():
    pygame.draw.rect(screen, apple_color, (apple_x, apple_y, 20, 20))


# Go through each element of snake starting from the end and copy the element preceding the current one
def move_snake():
    i = len(snake) - 1
    while i > 0:
        snake[i] = snake[i - 1].copy()
        i -= 1


# Check for collisions with walls or self
def check_collisions():
    i = 1
    while i < len(snake):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            return True
        elif snake[0][0] >= 780 or snake[0][0] <= 0 or snake[0][1] <= 0 or snake[0][1] >= 580:
            return True
        i += 1
    return False


# Check for collisions with apple
def check_apple():
    if math.sqrt(math.pow((snake[0][0] - apple_x), 2) + math.pow((snake[0][1] - apple_y), 2)) <= 20:
        return True
    return False


def grow_snake():
    global apple_x, apple_y
    snake.append([apple_x, apple_y])
    apple_x = random.randint(0, 780)
    apple_y = random.randint(0, 580)
    move_snake()


# Main game loop
running = True
while running:
    clock.tick(20)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if yChange == 0:
                    xChange = 0
                    yChange = -20
            elif event.key == pygame.K_DOWN:
                if yChange == 0:
                    xChange = 0
                    yChange = 20
            elif event.key == pygame.K_LEFT:
                if xChange == 0:
                    yChange = 0
                    xChange = -20
            elif event.key == pygame.K_RIGHT:
                if xChange == 0:
                    yChange = 0
                    xChange = 20
        elif event.type == pygame.QUIT:
            running = False

    if xChange != 0 or yChange != 0:
        move_snake()
        snake[0][0] += xChange
        snake[0][1] += yChange

    if check_apple():
        grow_snake()
    elif check_collisions():
        running = False
    draw_snake()
    draw_apple()

    pygame.display.update()
