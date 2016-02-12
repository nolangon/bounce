import math
import random
import pygame
from sprites.bounce_rectangle_sprite import RectangleSprite
from helper.bounce_color import Color


class BlockSprite(RectangleSprite):
  size = width, height = 44, 42
  horiz_block_size = horiz_width, horiz_height = 44, 4
  vert_block_size = vert_width, vert_height = 4, 42

  def __init__(self, center_x=0, center_y=0, border_type=0):
    RectangleSprite.__init__(self, center_x, center_y)
    self.border_type = border_type
    self.size = BlockSprite.get_size(border_type)
    self.image = pygame.Surface(self.size)
    self.rect = self.image.get_rect(center=(center_x,center_y))

  def moveUp(self):
    self.rect = self.rect.move([0,-1])

  @staticmethod
  def get_size(border_type):
    if border_type == 1:
      size = BlockSprite.horiz_block_size
    elif border_type == 2:
      size = BlockSprite.vert_block_size
    else:
      size = BlockSprite.size
    return size
