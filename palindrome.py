#Is phrase a palindrome?
def is_palindrome(phrase):
  converted_phrase = phrase[::-1]
  if converted_phrase == phrase:
    return "Is Palindrome"

  else:
    return "Not is_palindrome"
