# Return dict of {ltr: frequency} from phrase.


def multiple_letter_count(phrase):
    return {letter: phrase.count(letter) for letter in phrase}


print(multiple_letter_count("lloooo"))  # {'l': 2, 'o': 4}
print(multiple_letter_count("ppooo"))  # {'p': 2, 'o': 3}
