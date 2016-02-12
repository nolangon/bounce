import random
import time
import pygame

from sprites.bounce_block import Block
from sprites.bounce_rectangle_sprite import RectangleSprite
from sprites.bounce_laser_sprite import LaserSprite
from sprites.bounce_horiz_laser_sprite import HorizLaserSprite
from sprites.bounce_vert_laser_sprite import VertLaserSprite

from helper.bounce_color import Color

class LasersController:
  def __init__(self, sprite_groups):
    self.sprite_groups = sprite_groups
    self.spaces = sprite_groups.free_spaces
    self.lasers = sprite_groups.all_lasers
    self.last_laser = sprite_groups.last_laser
    self.last_laser.add(LaserSprite(0,0))
    self.lasers_per_rows = 5

    self.last_time = time.time()
    self.switch_interval = 3
    self.is_vert_on = False

  def update_lasers(self, new_blocks_added):
    if self.is_space() and new_blocks_added:
      self.add_lasers()

    if self.update_time():
      LasersController.play_laser_sound()
      self.change_states()
    self.move_lasers()

  def add_lasers(self):
    k = min(self.lasers_per_rows, len(self.spaces))
    spaces = random.sample(self.spaces, k)
    for space in spaces:
      spaces.remove(space)
      laser_sprite = self.space_to_laser(space)
      self.add_laser(laser_sprite, space)

  def move_lasers(self):
    for laser_sprite in self.lasers:
      laser_sprite.remove_offscreen()
      laser_sprite.move_up()

  def change_states(self):
    for laser_sprite in self.lasers:
      laser_sprite.switch()
    self.switch_group()

  def update_time(self):
    now = time.time()
    if now - self.last_time >= self.switch_interval:
      self.last_time = now
      self.is_vert_on = not self.is_vert_on
      return True
    return False

  def is_space(self):
    if not self.last_laser:
      return False

    last_laser_size = self.last_laser.sprites()[0].size
    last_y = self.last_laser.sprites()[0].rect.y
    if last_y <= 600 - (last_laser_size[1]/2):
      return True
    return False

  def space_to_laser(self, space):
    if space.row_type == 1:
      laser_sprite = HorizLaserSprite(space.center_x + 4, space.center_y - (RectangleSprite.height/2))
      laser_sprite.state = random.choice([LaserSprite.OFF,LaserSprite.ON])
      return laser_sprite
    elif space.row_type == 2:
      laser_sprite = VertLaserSprite(space.center_x - (RectangleSprite.width/2) + 3, space.center_y)
      laser_sprite.state = random.choice([LaserSprite.OFF,LaserSprite.ON])
      return laser_sprite
    return None

  def add_laser(self, laser_sprite, space):
    if laser_sprite.state == LaserSprite.ON:
      self.sprite_groups.on_lasers.add(laser_sprite)
    elif laser_sprite.state == LaserSprite.OFF:
      self.sprite_groups.off_lasers.add(laser_sprite)

    if space.row_type == RectangleSprite.BLOCK_ROW:
      self.last_laser.add(laser_sprite)
    self.lasers.add(laser_sprite)

  def check_collisions(self):
    lasers_hit = self.sprite_groups.lasers_hit
    if lasers_hit:
      return True
    return False

  def switch_group(self):
    self.sprite_groups.on_lasers, self.sprite_groups.off_lasers = self.sprite_groups.off_lasers, self.sprite_groups.on_lasers

  @staticmethod
  def play_laser_sound():
    laser_sound = pygame.mixer.Sound('sounds/laser1.wav')
    laser_sound.set_volume(.2)
    laser_sound.play()
