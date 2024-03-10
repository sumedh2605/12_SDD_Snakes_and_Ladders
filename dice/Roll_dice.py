import random

def dice_roll():
    number = (1, 2)
    rollednumber = []
    for i in range(2):
        rollednumber.append(random.randint(1, 6))
    return(rollednumber)
