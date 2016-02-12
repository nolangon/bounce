import random
class Ids(object):

  def __init__(self):
    self.ids = list(range(100))
  def get(self):
    if len(self.ids) <= 0:
      self.ids = list(range(100))

    rand_index = random.randint(0,len(self.ids)-1)
    rand_id = self.ids[rand_index]
    del self.ids[rand_index]
    return rand_id
