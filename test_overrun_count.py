from players import players
from dice_old import dice
players_list = players.create_players(2)
print(f"players_list = {players_list}")
players.update_players_projected_new_position(player_id=1, pos=98)
players.update_player_new_position(player_id=1, confirmed_new_pos=98)
players.update_player_current_postion(player_id=1)


for i in range(12):
    print(f"i = {i}")
    dice1, dice2 = dice.roll_dice(player_id=1)
    dice_sum = dice1 + dice2
    players.play(player_id=1, dice_sum=dice_sum)
