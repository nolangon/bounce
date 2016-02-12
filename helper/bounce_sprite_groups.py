import collections
import operator
import pygame

class SpriteGroups:
  def __init__(self):
    self.player = pygame.sprite.GroupSingle()

    self.starsnbombs = pygame.sprite.RenderUpdates()
    self.starsnbombs_hit = pygame.sprite.RenderUpdates()

    self.stars = pygame.sprite.RenderUpdates()
    self.stars_hit = pygame.sprite.RenderUpdates()
    self.last_star = pygame.sprite.GroupSingle()

    self.blocks = pygame.sprite.RenderUpdates()
    self.blocks_hit = pygame.sprite.RenderUpdates()
    self.last_block = pygame.sprite.GroupSingle()
    self.last_row = pygame.sprite.GroupSingle()

    self.unoccupied_spaces = pygame.sprite.RenderUpdates()
    self.free_spaces = pygame.sprite.RenderUpdates()

    self.all_lasers = pygame.sprite.RenderUpdates()
    self.on_lasers = pygame.sprite.RenderUpdates()
    self.off_lasers = pygame.sprite.RenderUpdates()
    self.last_laser = pygame.sprite.GroupSingle()
    self.lasers_hit = pygame.sprite.RenderUpdates()
    
    self.level_text = pygame.sprite.GroupSingle()

  def add_star(self, star_sprite):
    add = operator.methodcaller('add', star_sprite)
    map(add, [self.stars, self.last_star, self.starsnbombs])

  def add_block(self, block):
    self.last_block.add(block.sprite)
    self.blocks.add(block.sprite)

  def add_blocks(self, blocks):
    for block in blocks:
      self.add_block(block)

  def add_on_laser(self, laser_sprite):
    self.all_lasers.add(laser_sprite)
    self.on_lasers.add(laser_sprite)

  def add_off_laser(self, laser_sprite):
    self.all_lasers.add(laser_sprite)
    self.off_lasers.add(laser_sprite)

  def add_player(self, player):
    self.player.add(player.sprite)

  def add_space(self, space):
    self.unoccupied_spaces.add(space.sprite)

  def add_spaces(self, spaces):
    for space in spaces:
      self.free_spaces.add(space)

  def replace_spaces(self, spaces):
    self.free_spaces.empty()
    self.add_spaces(spaces)

  def add_to_all_spaces(self, spaces):
    for space in spaces:
      self.all_spaces.add(space)

  def add_level_text(self, level_text):
    self.level_text.add(level_text)
