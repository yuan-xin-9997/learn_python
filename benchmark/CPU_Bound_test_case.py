import random

def append_to_list(lst, num_items):
  """
  Appends num_items integers within the range [0-20000000) to the input lst
  """
  for n in random.sample(range(20000000), num_items):
    lst.append(n)