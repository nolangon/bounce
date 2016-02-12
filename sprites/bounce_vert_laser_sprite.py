import time
import pygame
from sprites.bounce_laser_sprite import LaserSprite
from helper.bounce_color import Color

class VertLaserSprite(LaserSprite):
  size = width, height = 3, 42
  switch_interval = 3
  def __init__(self, center_x, center_y):
    LaserSprite.__init__(self, center_x, center_y)
    self.size = VertLaserSprite.size
    self.center_x, self.center_y = center_x, center_y
    self.switch_interval = VertLaserSprite.switch_interval
 
    self.image = pygame.Surface(self.size)
    self.image.fill(Color.RED)
    self.rect = self.image.get_rect(center=(self.center_x, self.center_y))
