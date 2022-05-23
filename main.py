import sys 
import os
import pygame

from snake import Snake
from food_generator import FoodGenerator
from globals import *

def main():

  pygame.init()

  # center the window created  
  os.environ['SDL_VIDEO_CENTERED'] = '1'
  
  game_display = pygame.display.set_mode((X_SIZE, Y_SIZE))
  pygame.display.set_caption('Snake Game - Score: 0')

  clock = pygame.time.Clock()
  s = Snake()
  g = FoodGenerator(50)
  
  score = 0
  while not s.has_collided():
    pygame.display.set_caption('Snake Game - Score: %s' % (score))
    game_display.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.display.quit()
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYUP:
          s.change_direction(event.key)

    # update the state of the food
    g.update(s, game_display)
    
    # update the state of the snake
    eaten = s.update(g.food, game_display)
    if eaten: score += 1

    pygame.display.update()
    clock.tick(20)

if __name__ =='__main__':
  main()