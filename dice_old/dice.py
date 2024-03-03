from random import choice
dice_numbers=[1,2,3,4,5,6]

def roll_dice():
    """ Rolls dice for player

    Args:
        player_id (str): player id

    Returns:
        tuple: str, int
    """
    dice1=choice(dice_numbers)
    dice2=choice(dice_numbers)
    dice_sum = dice1 + dice2
    print(f"dice1= {dice1}, dice2={dice2}, dice_sum = {dice_sum}")
    return dice1, dice2
    