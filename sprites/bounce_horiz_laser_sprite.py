import time
import pygame
from sprites.bounce_laser_sprite import LaserSprite
from helper.bounce_color import Color

class HorizLaserSprite(LaserSprite):
  size = width, height = 44, 3
  switch_interval = 2
  def __init__(self, center_x, center_y):
    LaserSprite.__init__(self, center_x, center_y)
    self.size = HorizLaserSprite.size
    self.center_x, self.center_y = center_x, center_y
    self.switch_interval = HorizLaserSprite.switch_interval

    self.image = pygame.Surface(HorizLaserSprite.size)
    self.image.fill(Color.RED)
    self.rect = self.image.get_rect(center=(self.center_x, self.center_y))
