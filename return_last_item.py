#Return last item in list (None if list is empty.)
# In termninal, call function in this format
# last_element([2,5,7,10]) if list of numbers 

def last_element(lst):
  if len(lst) == 0:
    return None
  else:
    return lst[-1]