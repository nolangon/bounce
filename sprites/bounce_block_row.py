import sys
import pdb
import copy
import random
from sprites.bounce_row import Row
from sprites.bounce_cell import Cell

class BlockRow(Row):
  def __init__(self, ids, last_row=None):
    Row.__init__(self, ids, last_row)
    self.sets = {}
    self.cells = self.get_row_template()
    self.row_type = Row.BLOCK

  def fill(self):
    for i in range(0, len(self), 2):
      self[i].fill()
    for i in range(1, len(self), 2):
      self[i].is_linked = False
    return self

  def link(self):
    for set_id in self.sets:
      k = random.randint(1, len(self.sets[set_id]))
      indices_to_link = random.sample(self.sets[set_id], k)

      for index in indices_to_link:
        self[index].is_linked = True

    for i in range(1, len(self), 2):
      if self[i].is_linked == False:
        self[i] = Cell(i, self.ids.get())
        self.add_to_sets(self[i])
    return self

  def join(self):
    self.sets = {}
    for i in range(1, len(self), 2):
      join = random.random()
      right_index = self.right_neighbor_index(self[i])
      if right_index is None:
        self.add_to_sets(self[i])
        continue 

      if self[i] != self[right_index]:
        if join < .5:
          self.join_right(self[i])
          self.add_to_sets(self[i], self[right_index])
        else:
          self.add_to_sets(self[i])
      else:
        self[right_index-1].unfill()
    return self

  def join_right(self, cell):
    right_index = self.right_neighbor_index(cell)

    is_linked = self.cells[right_index].is_linked
    self.cells[right_index] = Cell(right_index, cell.set_id)
    self.cells[right_index].is_linked = is_linked

    self.cells[right_index - 1].unfill()

  def add_to_sets(self, *cells):
    for cell in cells:
      if cell.set_id in self.sets:
        if cell.index not in self.sets[cell.set_id]:
          self.sets[cell.set_id].append(cell.index)
      else:
        self.sets[cell.set_id] = [cell.index]

  def get_row_template(self):
    cells = []
    for i in range(Row.length):
      if i % 2 == 0:
        cell = Cell(i)
        cell.fill()
        cells.append(cell)
      else:
        cell = Cell(i, self.ids.get())
        cells.append(cell)
        self.add_to_sets(cell)
    return cells

  def right_neighbor_index(self, cell):
    if cell.index >= len(self) - 3:
      return None
    return cell.index + 2
