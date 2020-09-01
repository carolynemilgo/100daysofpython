#Return intersection of two lists as a new list::


def list_intersection(list_one,list_two):
  list_three = [value for value in list_one if value in list_two]
  return list_three 

