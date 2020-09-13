
#Return most-common number in list.


def most_common(my_list):
    counter = 0 #initialize counter
    #loop through to get frequency of each element
    for number in my_list:
      frequency = my_list.count(number)
      #if current frequency is > than counter, update our counter with the new frequency
      if frequency > counter:
        counter = frequency
    return number

print(most_common([1,1,2,2,2,2,2]))     