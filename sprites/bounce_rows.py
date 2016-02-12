from sprites.bounce_block_row import BlockRow
from sprites.bounce_border_row import BorderRow

from helper.bounce_ids import Ids


class Rows(object):
  ''' Constructs new rows using Eller's Algorithm for
      generating mazes. '''
  def __init__(self):
    self.ids = Ids()
    self.last_row = None
    self.border_row = None
    self.rows = [self.last_row]

    self.count = 0

  def get_new_rows(self):
    if self.last_row is None:
      self.last_row = self.get_first_row()
      self.rows = [self.last_row]

      return self.rows
    prev_row = self.last_row
    self.last_row = self.get_block_row(prev_row)
    self.border_row = self.get_border_row(self.last_row)

    self.rows = [self.border_row, self.last_row]
    return self.rows

  def get_first_row(self):
    return BlockRow(self.ids).join()

  def get_block_row(self, prev_row):
    return prev_row.fill().link().join()

  def get_border_row(self, block_row):
    return BorderRow(self.ids).fill(block_row)

  def get_last_row(self):
    row = BorderRow(self.ids)
    row[0].fill(); row[-1].fill()
    return row
