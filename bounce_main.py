import pygame
from helper.bounce_sprite_groups import SpriteGroups
from controllers.bounce_game_controller import GameController
from view.bounce_view import View
from controllers.bounce_cpu_spinner import CPUSpinner

def main():

  pygame.init()

  sprite_groups = SpriteGroups()
  view = View(sprite_groups)
  controller = GameController(sprite_groups)
  spinner = CPUSpinner(controller, view)

  spinner.run()

main()
