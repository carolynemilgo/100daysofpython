# Return last item in list (None if list is empty.)


def last_element(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[-1]


print(last_element([2, 5, 7, 9]))  # 9
print(last_element([]))  # None
