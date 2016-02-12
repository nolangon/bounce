from sprites.bounce_row import Row
from sprites.bounce_cell import Cell


class BorderRow(Row):
  def __init__(self, ids, last_row=None):
    Row.__init__(self, ids, last_row)
    self.row_type = Row.BORDER
    self.cells = [Cell(i) for i in range(Row.length)]

  def fill(self, block_row):
    for i in range(1, len(block_row), 2):
      if not block_row[i].is_linked:
        self[i].fill()
    return self
