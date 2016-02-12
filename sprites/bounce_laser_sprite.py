import time
import pygame
from sprites.bounce_rectangle_sprite import RectangleSprite
from helper.bounce_color import Color

class LaserSprite(RectangleSprite):
  size = width, height = 4, 4
  switch_interval = 1
  OFF = -1
  ON = 1
  def __init__(self, center_x, center_y):
    RectangleSprite.__init__(self, center_x, center_y)
    self.size = LaserSprite.size
    self.state = LaserSprite.OFF
    self.switch_interval = LaserSprite.switch_interval
    self.center_x, self.center_y = center_x, center_y

    self.image = pygame.Surface(LaserSprite.size)
    self.image.fill(Color.RED)
    self.rect = self.image.get_rect(center=(self.center_x, self.center_y))

  def switch(self):
    self.state = -self.state

  def move_up(self):
    self.rect = self.rect.move([0,-1])
