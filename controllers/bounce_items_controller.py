import random
import operator
import pygame

from sprites.bounce_row import Row
from sprites.bounce_block_sprite import BlockSprite
from sprites.bounce_rectangle_sprite import RectangleSprite
from sprites.bounce_star_sprite import StarSprite

from helper.bounce_color import Color
from helper.bounce_sprite_groups import SpriteGroups


class ItemsController():
  max_stars = 10
  max_bombs = 2
  def __init__(self, sprite_groups):
    self.sprite_groups = sprite_groups
    self.unoccupied = sprite_groups.unoccupied_spaces
    self.stars = sprite_groups.stars
    self.all_items = sprite_groups.starsnbombs

    self.coin = pygame.mixer.Sound("sounds/coin.wav")

  def update_items(self):
    self.check_collisions()

    if self.is_star_space():
      self.add_star()

    self.move_items()
    self.remove_off_screen_items()

  def add_star(self):
    rand_space = random.choice(self.sprite_groups.free_spaces.sprites())
    self.sprite_groups.free_spaces.remove(rand_space)
    star = StarSprite(rand_space.center_x + 4, rand_space.center_y + 3)
    self.sprite_groups.add_star(star)

  def move_items(self):
    for item_sprite in self.all_items:
      item_sprite.move_up()
 
  def remove_off_screen_items(self):
    for item_sprite in self.all_items:
      if item_sprite.rect.y <= -item_sprite.height:
        item_sprite.kill()

  def is_star_space(self):
    last_star_y = self.sprite_groups.last_star.sprites()[0].rect.y
    if last_star_y <= 550:
      return True
    return False

  def check_collisions(self):
    for item in self.sprite_groups.starsnbombs_hit:
      self.coin.play()
      item.kill()
      
