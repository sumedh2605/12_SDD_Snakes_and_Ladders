
ladders = {71: 92,
           61: 82,
           56: 75,
           36: 77,
           9: 30,
           6: 17}

snakes = {97: 78,
          95: 56,
          88: 38,
          62: 18,
          32: 10,
          36: 5}


user_input = int(input("Enter an integer: "))


# Check if the input matches any ladder key
if user_input in ladders:
    print(f"Ladder found! Climb from {user_input} to {ladders[user_input]}.")
    endpoint_ladder = ladders[user_input] #the value that should be shared with other modules

# Check if the input matches any snakes key
elif user_input in snakes:
    print(f"Snake found! Slide down from {user_input} to {snakes[user_input]}.")
    endpoint_snake = snakes[user_input] #the value that should be shared with other modules
# If no match is found
else:
    print("No ladder or snake found for the given input.")
