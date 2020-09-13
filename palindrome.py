# Is phrase a palindrome?


def is_palindrome(phrase):
    converted_phrase = phrase.lower()
    reversed_word = converted_phrase[::-1]
    if converted_phrase == reversed_word:
        return "Is palindrome"
    else:
        return "Not palindrome"


print(is_palindrome("Pop"))  # Is palindrome
print(is_palindrome("cat"))  # Not palindrome
print(is_palindrome("yooy"))  # Is palindrome
