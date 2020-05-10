import tensorflow as tf 
import numpy as np
from keras.models import load_model
import random 
import pygame
from settings import * 

pygame.init()
model = load_model('flappy_bird_AI3.h5')

class Pipes: 
    def __init__(self, x, h):
        pygame.draw.rect(window, black, [x, 0, 10, h])
        pygame.draw.rect(window, black, [x, h+gap, 10, window_len])


class Sprite:
    def __init__(self, y):
        pygame.draw.rect(window, black, [x, y, 10, 10])


def graphics():
    window.fill(white)
    Sprite(y)
    Pipes(px, h)
    pygame.display.update()
    clock.tick(fps)

def jump():
    global velocity_y, output
    velocity_y = 8
    output = 1

def key_strokes():
    global run_game, velocity_y

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run_game = False
        # if event.type is pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         jump()

def collision(y):
    if int(y+20) >= int(window_len) or y <= 0: 
        return True
    if x+10 >= px and x <= px+10:
        if y <= h or y >= h+gap:
            return True
    return False

def reset_func():
    global px, y, run_game, x, h, velocity_y, reset

    x = 100
    y = 100
    px = window_wd
    h = random.randint(20, window_len-gap-20)
    velocity_y = -2     # resets the acceleration
    reset = True

def game_logic():
    global px, h, velocity_y, y

    y -= velocity_y
    velocity_y -= 0.4
    px -= velocity_x
    if px+10 <= 0:  #infinite random pipe generation
        px = window_wd
        h = random.randint(20, window_len-gap-20)

def distance(a, b):
    return ((a**2) + (b**2))**0.5
'''
def normalization_and_data_collection():
    global state, data, output

    x1 = distance(abs(y-h), abs(px-x))
    x2 = distance(abs(y-(h+gap)), abs(px-x))
    x3 = y
    x4 = abs(window_len-y)
    state = [x1, x2, x3, x4]
    data.append([np.array(state)/window_wd, np.array(output)])
    output = 0
    
def automated_data_collection():
    if y >= int(h+gap-20): jump() 
'''
def ai():
    global state 

    x1 = distance(abs(y-h), abs(px-x))  
    x2 = distance(abs(y-(h+gap)), abs(px-x))
    x3 = y
    x4 = abs(window_len-y)
    state = [x1, x2, x3, x4]
    state = [np.array(state)/window_wd]
    state = np.vstack(state)
    should_i_jump = (model.predict(state) > 0.5).astype(int)
    if should_i_jump[0][0] == 1:
        jump()

def game():
    while run_game:
        if collision(y):    # basically restarts the game
            reset_func()
        key_strokes()
        game_logic()
        ai()
        # normalization_and_data_collection()
        graphics()

if __name__ == '__main__':
    game()
    # np.save('testing_data3.npy', data)


pygame.quit()
quit()
