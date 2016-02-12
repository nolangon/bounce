import pygame

class RectangleSprite(pygame.sprite.Sprite):
  size = width, height = 44, 42
  BORDER_ROW, BLOCK_ROW = 1, 2

  def __init__(self, center_x=0, center_y=0, row_type=2):
    pygame.sprite.Sprite.__init__(self)
    self.center_x, self.center_y = center_x, center_y
    self.row_type = row_type

    self.image = pygame.Surface(RectangleSprite.size)
    self.rect = self.image.get_rect(center=(center_x, center_y))

  def remove_offscreen(self):
    if self.rect.right <= 0:
      self.kill()
    elif self.rect.left >= 800:
      self.kill()
    elif self.rect.top >= 650:
      self.kill()
    elif self.rect.bottom <= 0:
      self.kill()
    return self

  def move_up(self):
    self.rect = self.rect.move([0,-1])
