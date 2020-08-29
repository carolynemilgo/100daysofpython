# Reverse the string passed in

def reverse_string(phrase):
  
  #Ensure that input is converted to a string first
  converted_phrase = str(phrase)  
  #use a splice that steps backwards without adding the start and stop indexes
  return(converted_phrase[::-1])