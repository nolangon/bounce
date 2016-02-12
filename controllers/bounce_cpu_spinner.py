class CPUSpinner():
  def __init__(self, controller, view):
    self.view = view
    self.controller = controller
  
  def run(self):
    self.view.run()
    while True:
      self.controller.update_sprites()
      self.view.run()
