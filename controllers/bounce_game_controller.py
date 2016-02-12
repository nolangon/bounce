import sys
import math
import random
import operator
import pygame

from controllers.bounce_player_controller import PlayerController
from controllers.bounce_blocks_controller import BlocksController
from controllers.bounce_lasers_controller import LasersController
from controllers.bounce_items_controller import ItemsController

from sprites.bounce_player import Player
from sprites.bounce_block import Block

from sprites.bounce_player_sprite import PlayerSprite
from sprites.bounce_block_sprite import BlockSprite
from sprites.bounce_laser_sprite import LaserSprite
from sprites.bounce_star_sprite import StarSprite
from sprites.bounce_level_text import LevelText

from helper.bounce_color import Color


class GameController:
  def __init__(self, sprite_groups):
    self.sprite_groups = sprite_groups
    self.add_starting_sprites()
    
    self.player_sprite = self.sprite_groups.player.sprites()[0]
    self.player_controller = PlayerController(self.sprite_groups)
    self.blocks_controller = BlocksController(self.sprite_groups)
    self.lasers_controller = LasersController(self.sprite_groups)
    self.items_controller = ItemsController(self.sprite_groups)

    self.events = self.get_events()
    self.collision = False

    pygame.key.set_repeat(1,10)

    pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play(loops=-1)

  def update_sprites(self):
    self.events = self.get_events()
    self.keys = pygame.key.get_pressed()
    self.collision = self.get_player_block_collisions()
    self.get_player_item_collisions()
    self.get_player_laser_collisions()

    self.player_controller.update_player(self.events, self.collision, self.keys)

    if not self.check_player_bounds():
      GameController.play_lose_sound()
      pygame.time.delay(1500)
      sys.exit()
    
    added = self.blocks_controller.update_blocks()
    self.lasers_controller.update_lasers(added)
    self.items_controller.update_items()
    
    pygame.event.pump()

  def get_events(self):
    events = {}
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        events[event.key] = 1
    return events

  def get_player_block_collisions(self):
    blocks = self.sprite_groups.blocks
    blocks_hit = self.sprite_groups.blocks_hit
    hit_blocks = pygame.sprite.spritecollide(self.player_sprite, blocks, False)
    if hit_blocks is not None: map(blocks_hit.add, hit_blocks)

  def get_player_item_collisions(self):
    items = self.sprite_groups.starsnbombs
    items_hit = self.sprite_groups.starsnbombs_hit
    hit_items = pygame.sprite.spritecollide(self.player_sprite, items, True)
    if hit_items is not None: map(items_hit.add, hit_items)

  def get_player_laser_collisions(self):
    lasers = self.sprite_groups.on_lasers
    lasers_hit = self.sprite_groups.lasers_hit
    hit_lasers = pygame.sprite.spritecollide(self.player_sprite, lasers, False)
    if hit_lasers:
      pygame.mixer.music.stop()
      pygame.mixer.Sound('sounds/lose.wav').play()
      pygame.time.delay(1500)
      sys.exit()
      map(lasers_hit.add, hit_lasers)

  def check_player_bounds(self):
    if self.player_sprite.rect.centery < 0:
      return False
    elif self.player_sprite.rect.centery > 600:
      return False
    else:
      return True

  def add_starting_sprites(self):
    self.sprite_groups.add_block(Block(400,350))
    self.sprite_groups.add_star(StarSprite(-300,-350))
    self.sprite_groups.add_player(Player())
    self.sprite_groups.add_level_text(LevelText())

  @staticmethod
  def play_lose_sound():
    pygame.mixer.music.stop()
    lose_sound = pygame.mixer.Sound('sounds/lose.wav')
    lose_sound.play()

  
