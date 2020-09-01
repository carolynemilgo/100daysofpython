#Given two friends, do they have any hobbies in common?

def common_hobbies(friend_one, friend_two):
  similar_hobbies = [hobby for hobby in friend_one if hobby in friend_two]
  if len(similar_hobbies) != 0:
    return("Go on friend date since these hobbies are similar:", similar_hobbies)
  else:
    return("Can't go on date")
