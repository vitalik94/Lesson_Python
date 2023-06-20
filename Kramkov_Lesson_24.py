# ДЗ на понедельник (Ivanov_Lesson_23.py)
# 1. Увеличить змейку после поедания каждого яблока
# 2. Увеличить очки после каждого съеденного яблока
# 3. Усложнять игру по мере поедания яблок
# 4. Добавить препятствия
# 5. Игра заканчивается, если змейка врежется в свой хвост
# 6. Добавить звуки поедания яблок и game over
import random
import pygame

pygame.init()

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Змейка')

game_over = False

window_size = pygame.display.get_window_size()

x_1 = 100
y_1 = 400
len_snake = [[x_1, y_1]]
x_1_change = 0
y_1_change = 0
num = 1
apple_x = random.randrange(0, window_size[0], 10)
apple_y = random.randrange(0, window_size[1], 10)

let_x = random.randrange(0, window_size[0], 10)
let_y = random.randrange(0, window_size[0], 10)

clock = pygame.time.Clock()

score = 0
speed = 20
font = pygame.font.Font(None, 36)

lets = []

eating_sound = pygame.mixer.Sound('eating.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_1_change = -10
                y_1_change = 0
            if event.key == pygame.K_RIGHT:
                x_1_change = 10
                y_1_change = 0
            if event.key == pygame.K_UP:
                y_1_change = -10
                x_1_change = 0
            if event.key == pygame.K_DOWN:
                y_1_change = 10
                x_1_change = 0

    if x_1 >= window_size[0] or y_1 >= window_size[1] or x_1 <= 0 or y_1 <= 0:
        game_over_sound.play()
        clock.tick(1)
        game_over = True

    x_1 += x_1_change
    y_1 += y_1_change

    for let in lets:
        if pygame.Rect(x_1, y_1, 10, 10).colliderect(pygame.Rect(let[0], let[1], 20, 20)):
            game_over_sound.play()
            clock.tick(1)
            game_over = True
            break

    dis.fill(white)
    nadpis = font.render('Очки: ' + str(score), True, red)
    dis.blit(nadpis, (10, 10))
    len_snake.append([x_1, y_1])

    if len(len_snake) > num:
        del len_snake[0]

    for x_y in len_snake:
        pygame.draw.rect(dis, blue, [x_y[0], x_y[1], 10, 10])

    pygame.draw.rect(dis, red, [apple_x, apple_y, 10, 10])

    for let in lets:
        pygame.draw.rect(dis, green, [let[0], let[1], 20, 20])

    pygame.display.update()

    if x_1 == apple_x and y_1 == apple_y:
        eating_sound.play()
        print('Съел!')
        num += 1
        apple_x = random.randrange(0, window_size[0], 10)
        apple_y = random.randrange(0, window_size[1], 10)
        score += 1
        speed += 1
        if len(lets) < 1000:
            let_x = random.randrange(0, window_size[0], 20)
            let_y = random.randrange(0, window_size[1], 20)

    lets.append([let_x, let_y])
    clock.tick(speed)

pygame = quit()
quit()
