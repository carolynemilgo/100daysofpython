#Return dict of {ltr: frequency} from phrase.


def multiple_letter_count(phrase):
  #frequency = phrase.count(letter)
  return {letter: phrase.count(letter) for letter in phrase}
