class Row(object):
  BORDER = 1
  BLOCK = 2
  length = 37

  def __init__(self, ids, last_row=None,):
    self.ids = ids
    self.last_row = last_row
    self.row_type = None
    self.cells = []

    self.current_index = 0

  def __iter__(self):
    return iter(self.cells)

  def __len__(self):
    return len(self.cells)

  def __getitem__(self, index):
    return self.cells[index]

  def __setitem__(self, index, cell):
    self.cells[index] = cell

  def __delitem__(self, index):
    del self.cells[index]

  def next(self):
    if self.current_index >= len(self.cells):
      self.current_index = 0
      raise StopIteration
    else:
      index = self.current_index
      self.current_index += 1
      return self.cells[index]
