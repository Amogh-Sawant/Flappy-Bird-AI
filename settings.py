import pygame
import random

# window
window_len = 700
window_wd = 400
window = pygame.display.set_mode((window_wd, window_len))
pygame.display.set_caption("ga test")

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# game attributes
run_game = True
clock = pygame.time.Clock()
fps = 144

# initial position
x = 100
y = 300
px = window_wd

# misc
reset = False
gap = 150
velocity_x = 1.5
velocity_y = -2
h = random.randint(20, window_len-gap-20)

# AI attributes
generation = 0
population_size = 30
population = []
state = []
output = 0
data = []
parent1 = []
parent2 = []
best_generation_score = 0
current_generation_score = 0
temp_parent1 = []
temp_parent2 = []