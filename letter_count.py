#How many times does letter appear in word (case-insensitively)?
#Use string count

def single_letter_count(word, letter):
 
  letter_count= (word.lower()).count(letter.lower())
  if letter_count == 0:
    return("Letter not found")
  else:
    return letter_count  
