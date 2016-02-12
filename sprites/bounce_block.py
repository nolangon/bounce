import sys
import math
import random
import pygame
from sprites.bounce_block_sprite import BlockSprite

class Block():
  def __init__(self, center_x=0, center_y=0, border_type=0):
    self.sprite = BlockSprite(center_x, center_y, border_type)

  def move_up(self):
    self.sprite.move_up()
