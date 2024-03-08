from players import players
from dice import Roll_dice
players_list = players.create_players(2)
print(f"players_list = {players_list}")
players.update_players_projected_new_position(player_id=1, pos=98)
players.update_player_new_position(player_id=1, confirmed_new_pos=98)
players.update_player_current_postion(player_id=1)

players.update_players_unlucky_roll_list(player_id=1, unlucky_roll_sum=12)

for i in range(12):
    print(f"i = {i}")
    dice_output = Roll_dice.dice_roll(player_id=1)
    dice1 = dice_output[0]
    dice2 = dice_output[1]
    dice_sum = dice1 + dice2
    players.play(player_id=1, dice_sum=dice_sum)
    
