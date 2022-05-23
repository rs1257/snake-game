import pygame

from globals import *

class Snake:
  direction = RIGHT
  body = [[4, 1], [3, 1], [2, 1], [1, 1]]
  eaten = False

  def __init__(self):
    self.x_size = X_SIZE / BLOCK_SIZE
    self.y_size = Y_SIZE / BLOCK_SIZE
    self.block_size = BLOCK_SIZE
  
  def move(self):
    # update the position of the head of the snake
    x = self.body[0][0] + self.direction[0]
    y = self.body[0][1] + self.direction[1]
    self.body.insert(0, [x, y])

    # pop the tail of the snake if it hasn't eaten
    if not self.eaten:
      self.body = self.body[:-1]
    else:
      self.eaten = False
  
  def has_collided(self):
    collided = False
    # check if the snakes head hits the walls
    if ((self.body[0][0] >= self.x_size - 1) or (self.body[0][1] >= self.y_size - 1) or
        (self.body[0][0] <= 0) or (self.body[0][1] <= 0)):
      collided = True
    # check if the snake hits itself
    elif self.body[0] in self.body[1:]:
      collided = True

    return collided

  def change_direction(self, direction):
    # 273 - UP, 274 - DOWN, 275 - RIGHT, 276 - LEFT
    if self.direction == LEFT or self.direction == RIGHT:
      if direction == pygame.K_UP:
        self.direction = UP
      elif direction == pygame.K_DOWN:
        self.direction = DOWN
    elif self.direction == UP or self.direction == DOWN:
      if direction == pygame.K_RIGHT:
        self.direction = RIGHT
      elif direction == pygame.K_LEFT:
        self.direction = LEFT

  def draw(self, window):
    for no, pos in enumerate(self.body):
      colour = (255, 0, 0) if no == 0 else (255, 255, 255)
      rect = pygame.Rect(pos[0] * self.block_size, pos[1] * self.block_size, self.block_size, self.block_size)
      pygame.draw.rect(window, colour, rect)

  def eat(self, food):
    if self.body[0] in food:
      food.remove(self.body[0])
      self.eaten = True

  def update(self, food, window):
    self.move()
    self.eat(food)
    self.draw(window)
    return self.eaten