# Return frequency of term in lst.


def frequency(lst, search_term):
    return lst.count(search_term)


print(frequency(["apple", "pear", "banana", "pear"], "banana"))  # 1
print(frequency(["apple", "pear", "banana", "pear"], "pear"))  # 2
