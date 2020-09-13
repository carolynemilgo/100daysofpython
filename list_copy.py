# Return a copy of lst with non-true elements removed.


# or use filter
def return_true_elements(lst):
    new_list = [value for value in lst]
    return list(filter(None, new_list))


# This works too
# def return_true_elements(lst):
# lst_copy = [element for element in lst if element] #returns any that is iterable meaning it will be true
# return lst_copy


print(return_true_elements([1, 4, "and", None, []]))  # [ 1,4,'and]
print(
    return_true_elements(["print", "a", "and", False, [1, 4, 6]])
)  # ["print",'a',"and", [1,4,6]
