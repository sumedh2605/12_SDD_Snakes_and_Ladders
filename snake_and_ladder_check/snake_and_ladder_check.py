projected_new_position = int(input("Enter an integer: "))

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
          35: 5}


def snake_and_ladder_check():

    # Check if the input matches any ladder key
    if projected_new_position in ladders:
        print(f"Ladder found! Climb from {projected_new_position} to {ladders[projected_new_position]}.")
        confirmed_new_position = int(ladders[projected_new_position])  #used in sumedh's module

    # Check if the input matches any snakes key
    elif projected_new_position in snakes:
        print(f"Snake found! Slide down from {projected_new_position} to {snakes[projected_new_position]}.")
        confirmed_new_position = int(snakes[projected_new_position]) #used in sumedh's module

    # If no match is found
    else:
        print("No ladder or snake found for the given input.")

    print(confirmed_new_position)

snake_and_ladder_check()
