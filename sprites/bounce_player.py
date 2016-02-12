import pygame
from sprites.bounce_player_sprite import PlayerSprite
from helper.bounce_sprite_groups import SpriteGroups


class Player(object):
  def __init__(self):
    self.sprite = PlayerSprite()

  def move(self, x_direction):
    self.sprite.move(x_direction)

  def check_any_collisions_with_blocks(self):
    if pygame.sprite.spritecollideany(self.sprite, SpriteGroups.blocks):
      pass

  def check_any_collisions_with_group(self, group):
    if pygame.sprite.spritecollideany(self.sprite, group):
      pass
