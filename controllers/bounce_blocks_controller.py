import math
import random
import pygame

from sprites.bounce_block import Block
from sprites.bounce_block_sprite import BlockSprite
from sprites.bounce_rectangle_sprite import RectangleSprite
from sprites.bounce_level_text import LevelText

from sprites.bounce_rows import Rows
from sprites.bounce_cell import Cell

from helper.bounce_color import Color
from helper.bounce_sprite_groups import SpriteGroups


class BlocksController():
  def __init__(self, sprite_groups):
    self.sprite_groups = sprite_groups
    self.blocks = sprite_groups.blocks
    self.last_block = sprite_groups.last_block

    self.rows = Rows()

  def update_blocks(self):
    added = False
    self.check_collisions()
    if self.is_space_for_new_blocks():
      self.sprite_groups.level_text.sprites()[0].add()
      self.add_blocks_and_spaces()
      added = True

    self.move_all_blocks()
    self.remove_off_screen_blocks()
    return added

  def check_collisions(self):
    blocks_hit = self.sprite_groups.blocks_hit
    for block in blocks_hit:
      block.image.fill(Color.AQUAFINE)

  def is_space_for_new_blocks(self):
    last_block_size = self.last_block.sprites()[0].size
    last_block_y = self.last_block.sprites()[0].rect.bottom
    if last_block_y <= 600:
      return True
    return False

  def add_blocks_and_spaces(self):
    filled, unfilled = self.get_new_cells()

    spaces = BlocksController.cells_to_rectangles(unfilled)
    self.sprite_groups.replace_spaces(spaces)

    blocks = BlocksController.cells_to_blocks(filled)
    self.sprite_groups.add_blocks(blocks)

  def move_all_blocks(self):
    for block_sprite in self.blocks:
      block_sprite.moveUp()
    for space in self.sprite_groups.free_spaces:
      space.move_up()
  
  def remove_off_screen_blocks(self):
    for block_sprite in self.blocks:
      if block_sprite.rect.y <= -BlockSprite.height:
        block_sprite.kill() 

  def get_new_cells(self):
    next_rows = self.rows.get_new_rows()

    filled_cells, unfilled_cells = BlocksController.get_filled_unfilled_cells(next_rows)
    return filled_cells, unfilled_cells

  @staticmethod
  def cells_to_rectangles(cells):
    rectangles = []
    for cell, row_type in cells:
      rectangle = RectangleSprite((cell.index/2)*RectangleSprite.width + (RectangleSprite.width/2), 600 + (RectangleSprite.height/2), row_type)
      rectangles.append(rectangle)
    return rectangles


  @staticmethod
  def cells_to_blocks(cells):
    blocks = []
    for cell, row_type in cells:

      rectangle_centerx = (cell.index/2)*RectangleSprite.width + (RectangleSprite.width/2)
      rectangle_centery = 600 + (RectangleSprite.height/2)

      if row_type == RectangleSprite.BORDER_ROW:
        block = Block(rectangle_centerx + 4, rectangle_centery - (RectangleSprite.height/2), row_type)
      elif row_type == RectangleSprite.BLOCK_ROW:
        block = Block(rectangle_centerx - (RectangleSprite.width/2) + 4, rectangle_centery, row_type)
      else:
        raise TypeError("No Row Type specified")
      blocks.append(block)
    return blocks

  @staticmethod
  def get_filled_unfilled_cells(rows):
    filled_cells = []
    unfilled_cells = []

    for row in rows:
      for cell in row:
        if cell.is_filled:
          filled_cells.append((cell,row.row_type))
        elif not cell.is_filled and cell.cell_type == Cell.BORDER:
          unfilled_cells.append((cell,row.row_type))

    return filled_cells, unfilled_cells
