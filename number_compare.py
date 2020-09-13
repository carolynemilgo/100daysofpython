# Report on whether a>b, b>a, or b==a


def number_compare(a, b):
    if a > b:
        return " 'a' is greater than 'b' "
    elif a < b:
        return " 'b' is greater than 'a' "
    else:
        return " 'a' is equal to 'b' "


print(number_compare(4, 8))  # 'b' is greater than 'a'
print(number_compare(8, 4))  #'a' is greater than 'b'
print(number_compare(4, 4))  # 'a' is equal to 'b'
