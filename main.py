import random
import pygame
import math

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")

screen_width = 800
screen_height = 600
block_size = 20

apple_color = (214, 21, 21)
snake_color = (0, 117, 14)

screen = pygame.display.set_mode((screen_width, screen_height))

snake = [
    [block_size * 3, screen_height / 2],
    [block_size * 2, screen_height / 2],
    [block_size, screen_height / 2]
]

apple_x = 0
apple_y = 0


def reset_apple():
    global apple_x, apple_y
    apple_x = random.randint(0, screen_width - block_size)
    apple_y = random.randint(0, screen_height - block_size)


reset_apple()

xChange = block_size
yChange = 0


def draw_snake():
    for block in snake:
        pygame.draw.rect(screen, snake_color, (block[0], block[1], block_size, block_size))


def draw_apple():
    pygame.draw.rect(screen, apple_color, (apple_x, apple_y, block_size, block_size))


# Go through each element of snake starting from the end and copy the element preceding the current one
def move_snake():
    i = len(snake) - 1
    while i > 0:
        snake[i] = snake[i - 1].copy()
        i -= 1


# Check for collisions with walls or self
def check_collisions():
    i = 1
    if snake[0][0] >= screen_width or snake[0][0] <= 0 or snake[0][1] <= 0 or snake[0][1] >= screen_height:
        return True
    while i < len(snake):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            return True
        i += 1
    return False


# Check for collisions with apple
def check_apple():
    if math.sqrt(math.pow((snake[0][0] - apple_x), 2) + math.pow((snake[0][1] - apple_y), 2)) <= block_size:
        return True
    return False


def grow_snake():
    global apple_x, apple_y
    snake.append([apple_x, apple_y])
    reset_apple()
    move_snake()


# Main game loop
running = True

# variable to prevent two keys being pressed at the same time
key_pressed = False
while running:
    clock.tick(block_size)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if not key_pressed:
                key_pressed = True
                if event.key == pygame.K_UP:
                    if yChange == 0:
                        xChange = 0
                        yChange = -block_size
                elif event.key == pygame.K_DOWN:
                    if yChange == 0:
                        xChange = 0
                        yChange = block_size
                elif event.key == pygame.K_LEFT:
                    if xChange == 0:
                        yChange = 0
                        xChange = -block_size
                elif event.key == pygame.K_RIGHT:
                    if xChange == 0:
                        yChange = 0
                        xChange = block_size
        elif event.type == pygame.QUIT:
            running = False
    key_pressed = False

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
