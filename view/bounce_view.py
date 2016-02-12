import pygame
from helper.bounce_sprite_groups import SpriteGroups

class View():
  screen_size = width, height = 800, 600

  def __init__(self, sprite_groups):
    self.screen = pygame.display.set_mode(View.screen_size)
    self.sprite_groups = sprite_groups

  def run(self):
    self.draw_screen()
    self.draw_stars()
    self.draw_lasers()
    self.draw_blocks()
    self.draw_player()
    self.draw_levels()
    pygame.display.update()

  def draw_screen(self):
    self.screen.fill((255,255,255))

  def draw_player(self):
    self.sprite_groups.player.draw(self.screen)

  def draw_blocks(self):
    self.sprite_groups.blocks.draw(self.screen)

  def draw_lasers(self):
    self.sprite_groups.on_lasers.draw(self.screen)

  def draw_stars(self):
    self.sprite_groups.stars.draw(self.screen)

  def draw_levels(self):
    self.sprite_groups.level_text.sprites()[0].render()
    self.sprite_groups.level_text.draw(self.screen)
