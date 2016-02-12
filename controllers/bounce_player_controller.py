import pygame
from sprites.bounce_player_sprite import PlayerSprite

class PlayerController():
  player_speed = 4

  def __init__(self, sprite_groups):
    self.player_sprite = sprite_groups.player.sprites()[0]
    self.sprite_groups = sprite_groups
    self.wall_jumped = False

  def update_player(self, events, collided, keys):
    jump_pressed = self.get_jump_pressed(events)
    self.move_player(keys, collided, jump_pressed)

  def move_player(self, keys, collided, jump_pressed):
    wall_collision = self.get_wall_collision()

    x = self.get_x(keys); y = self.get_y(keys, collided, wall_collision)
    self.player_sprite.move_x(x, self.sprite_groups)
    self.player_sprite.move_y(y, self.sprite_groups)
      
  def get_y(self, keys, collided, wall_collision):
    player = self.player_sprite
    if keys[pygame.K_SPACE] and (self.is_sitting() or (wall_collision != 0)):
      if player.y_velocity > 2:
        player.y_velocity = player.jump_force
        PlayerController.play_jump_sound()
      player.y_velocity += player.gravity
    elif collided:
      player.y_velocity = -1
    elif not collided and not self.is_sitting():
      if player.y_velocity < 2:
        player.y_velocity += player.gravity
    return player.y_velocity

  def get_x(self, keys):
    player = self.player_sprite
    if keys[pygame.K_LEFT]:
      player.x_velocity = -3
    elif keys[pygame.K_RIGHT]:
      player.x_velocity = 3
    else:
      player.x_velocity = 0
    return player.x_velocity

    player.move(player.x_velocity, player.y_velocity, self.sprite_groups)

  def get_jump_pressed(self, events):
    if events.get(pygame.K_SPACE):
      return True
    return False

  def get_wall_collision(self):
    player = self.player_sprite
    old_rect = player.rect
    player.rect = player.rect.move(-1,0)
    if player.check_collision_with_group(self.sprite_groups.blocks):
      player.rect = old_rect
      return 1
    player.rect = old_rect.move(1,0)
    if player.check_collision_with_group(self.sprite_groups.blocks):
      player.rect = old_rect
      return -1
    player.rect = old_rect
    return 0

  def is_sitting(self):
    player = self.player_sprite
    old_rect = player.rect
    player.rect = player.rect.move(0,1)
    if player.check_collision_with_group(self.sprite_groups.blocks):
      player.rect = old_rect
      return True
    return False

  @staticmethod
  def play_jump_sound():
    jump_sound = pygame.mixer.Sound('sounds/jump.wav')
    jump_sound.set_volume(.2)
    jump_sound.play()
