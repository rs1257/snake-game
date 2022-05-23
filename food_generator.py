import pygame
import random

from globals import *

class FoodGenerator:
  food = []

  def __init__(self, number):
    self.x_size = X_SIZE / BLOCK_SIZE
    self.y_size = Y_SIZE / BLOCK_SIZE
    # only allow a maximum of about 20% of the grid to be filled with food
    self.number = min(number, (self.x_size * self.y_size) * 0.2)
    self.block_size = BLOCK_SIZE
    self.radius = int(self.block_size / 2)
  
  def generate_food(self, snake):
    while len(self.food) < self.number:
      # ensure the food is not at the edges
      x = random.randint(1, self.x_size - 2)
      y = random.randint(1, self.y_size - 2)
      
      # only add if the box is free
      if [x, y] not in snake.body and [x, y] not in self.food:
        self.food.append([x, y])
      
  def draw(self, window):
    for i in self.food:
      x_pos = i[0] * self.block_size + self.radius
      y_pos = i[1] * self.block_size + self.radius
      pygame.draw.circle(window, (0, 0, 255), [x_pos, y_pos], self.radius)
  
  def update(self, snake, window):
    self.generate_food(snake)
    self.draw(window)
