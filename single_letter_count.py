# How many times does letter appear in word (case-insensitively)?
# use the count method on string


def single_letter_count(word, letter):

    return word.lower().count(letter.lower())


print(single_letter_count("James", "j"))
print(single_letter_count("CotTon", "T"))
