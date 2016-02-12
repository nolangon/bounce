import sys
import pygame
from helper.bounce_color import Color

class LevelText(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.level_font = pygame.font.Font(None, 20)
    self.image = self.level_font.render("{0}/100".format(0), 1, (0,0,0))
    self.rect = self.image.get_rect(center=(769,10))

    self.level = 0

  def add(self, amt=1):
    self.level += amt
    if self.level >= 100:
      pygame.mixer.Sound('sounds/win.wav').play()
      pygame.time.delay(1500)
      sys.exit()

  def clear(self):
    self.level = 0

  def render(self):
    self.image = self.level_font.render("{0}/100".format(self.level), 1, (0,0,0))
