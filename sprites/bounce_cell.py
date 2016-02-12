class Cell(object):
  STAR = 2
  BORDER = 1
  BLOCK = 0
  def __init__(self, index, set_id=-1, item=None):
    self.set_id = set_id
    self.index = index

    if item:
      if item == Cell.STAR:
        self.cell_type = Cell.STAR
    elif self.set_id == -1:
      self.cell_type = Cell.BORDER
    else:
      self.cell_type = Cell.BLOCK

    self.is_filled = False
    self.is_linked = False
    
  def __str__(self):
    return str(self.__dict__)

  def __eq__(self, other):
    if not isinstance(other, Cell):
      raise TypeError
    return self.set_id == other.set_id

  def __nonzero__(self):
    return True

  def fill(self):
    self.is_filled = True

  def unfill(self):
    self.is_filled = False
