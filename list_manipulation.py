# Mutate lst to add/remove from beginning or end.


def list_manipulation(lst, command, location, value=None):
    if command == "add" and location == "end":
        lst.append(value)
        return lst
    elif command == "add" and location == "beginning":
        lst.insert(0, value)
        return lst
    elif command == "remove" and location == "beginning":
        lst.pop(0)
        return lst
    elif command == "remove" and location == "end":
        lst.pop(-1)
        return lst
    else:
        print("Command does not exist")


print(list_manipulation([1, 2, 3, 4, 5], "add", "end", 6))
print(list_manipulation([1, 2, 3, 4, 5], "add", "beginning", 4))
print(list_manipulation([1, 2, 3, 4, 5], "remove", "end", value=None))
print(list_manipulation([1, 7, 9, 10], "remove", "beginning", value=None))
print(list_manipulation([1, 2, 3, 4, 5], "remove", "beginning", value=None))
