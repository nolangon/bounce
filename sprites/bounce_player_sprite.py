import pygame
from helper.bounce_color import Color
from sprites.bounce_rectangle_sprite import RectangleSprite

class PlayerSprite(RectangleSprite):
  size = width, height = 16, 16
  border = 4

  def __init__(self):
    RectangleSprite.__init__(self)
    self.image = pygame.Surface(PlayerSprite.size)
    self.image.fill(Color.AQUAFINE)
    self.rect = self.image.get_rect(center=(400,300))
    
    self.gravity = 1
    self.jump_force = -13
    self.x_velocity = 0
    self.y_velocity = 0

  def move_x(self, amount, sprite_groups):
    amount_permitted = amount

    if amount >= 0:
      deduction = -1
    else:
      deduction = 1

    old_rect = self.rect
    self.rect = self.rect.move(amount, -1)

    while self.check_collision_with_group(sprite_groups.blocks):
      self.rect = old_rect
      amount_permitted += deduction
      self.rect = self.rect.move(amount_permitted, -1)

  def move_y(self, amount, sprite_groups):
    amount_permitted = amount

    if amount >= 0:
      deduction = -1
    else:
      deduction = 1

    old_rect = self.rect
    self.rect = self.rect.move(0, amount)

    while self.check_collision_with_group(sprite_groups.blocks):
      self.rect = old_rect
      amount_permitted += deduction
      self.rect = self.rect.move(0, amount_permitted)

  def check_collision_with_group(self, group):
    for sprite in group:
      if self.rect.colliderect(sprite.rect):
        sprite.image.fill(Color.AQUAFINE)
        return True
    return False

  
