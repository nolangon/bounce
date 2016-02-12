import pygame
from sprites.bounce_rectangle_sprite import RectangleSprite
from helper.bounce_color import Color

class StarSprite(RectangleSprite):
  size = width, height = 8, 8

  def __init__(self, center_x=0, center_y=0):
    RectangleSprite.__init__(self, center_x, center_y)
    self.image = pygame.Surface(self.size)
    self.image.fill(Color.YELLOW)
    self.rect = self.image.get_rect(center=(center_x,center_y))

    self.value = 5

  def move_up(self):
    self.rect = self.rect.move([0,-1])
