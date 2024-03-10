import logging
from typing import List, Dict
from snake_and_ladder_check import snake_and_ladder_check

#Players module: Done entirely by Sumedh

# dict to hold all players
players = {}
# winners
winners = []

winner_pos = 1


def create_players(num_of_players: int):
    """ create palyers based on input provided

    Args:
        num_of_players (int): number of players participating in game

    Returns:
        List[int]: List of palayers participating in game
    """

    for count in range(num_of_players):
        player = {
            'current_position': 0,
            'projected_new_position': 0,
            'new_position': 0,
            'is_completed_game': 0,
            'winner_pos': 0,
            'snake_bite_count': 0,
            'ladder_encountered_count': 0,
            'consecutive_turn_count': 0,
            'unlucky_roll_list': [],
            'overrun_count': 0
        }
        players[f'{count + 1}'] = player
    print(f"Created players : {players}")
    return [int(player) for player in players.keys()]


def update_player_new_position(player_id: int, confirmed_new_pos: int) -> None:
    """ update players new_position

    Args:
        player_id (int): player id
        confirmed_new_pos (int): new player position
    """

    players[f'{player_id}']['new_position'] = confirmed_new_pos
    print(f"players = {players}")


def update_winner_position(player_id: int, pos: int):
    """Update "winner_pos" for a player

    Args:
        player_id (int): Player id
        pos (int): winner pos
    """
    # global winner_pos
    players[f'{player_id}']['winner_pos'] = pos
    # winner_pos = winner_pos + 1


def increment_players_ladder_encountered_count(player_id: int):
    """Increment player's ladder_encountered_count whenever player climbs ladder

    Args:
        player_id (int): player id
    """
    players[f'{player_id}']['ladder_encountered_count'] = players[f'{player_id}']['ladder_encountered_count'] + 1


def increment_players_snake_bite_count(player_id: int):
    """Increment player's snake_bite_count whenever player got snake bite

    Args:
        player_id (int): player id
    """
    players[f'{player_id}']['snake_bite_count'] = players[f'{player_id}']['snake_bite_count'] + 1


def update_is_completed_game(player_id: int, status: int):
    """ Updates player's is_completed_status

    Args:
        player_id (int): player id
        status (int): 0 if player is still playing, 1 if player reached 100 tile

    """
    players[f'{player_id}']['is_completed_game'] = status


def get_is_complted_game(player_id: int) -> int:
    """Get player's is_completed_status

    Args:
        player_id (int): player id

    Returns:
        int: returns
    """
    return players[f'{player_id}']['is_completed_game']


def increment_consecutive_turn_count(player_id: int):
    """ increment player's consecutive_turnm_count

    Args:
        player_id (int): player id
    """
    players[f'{player_id}']['consecutive_turn_count'] = players[f'{player_id}']['consecutive_turn_count'] + 1


def reset_consecutive_turn_count(player_id: int):
    """ reset player's consecutive_turn_count

    Args:
        player_id (int): player id
    """
    players[f'{player_id}']['consecutive_turn_count'] = 0


def get_consecutive_turn_count(player_id: int):
    """

    Args:
        player_id (int): player id

    Returns:
        int: player's consecutive_turn_count
    """
    return players[f'{player_id}']['consecutive_turn_count']


def increment_overrun_count(player_id: int):
    """increment overrun_count

    Args:
        player_id (int): player id
    """
    players[f'{player_id}']['overrun_count'] = players[f'{player_id}']['overrun_count'] + 1


def get_overrun_count(player_id: int):
    """ get player's overrun count

    Args:
        player_id (int): player id

    Returns:
        int: player's overrun_count
    """
    return players[f'{player_id}']['overrun_count']


def reset_overrun_count(player_id: int):
    """ reset player's overrun_count

    Args:
        player_id (int): player id
    """
    players[f'{player_id}']['overrun_count'] = 0


def get_unlucky_roll_list(player_id: int):
    """
    Get Player's unlucky roll list
    Args:
        player_id (int): player_id
    """
    return players[f'{player_id}']['unlucky_roll_list']


def update_players_unlucky_roll_list(player_id, unlucky_roll_sum):
    players[f'{player_id}']['unlucky_roll_list'].append(unlucky_roll_sum)
    print(f"Players {player_id} unlucky roll list = {players[f'{player_id}']['unlucky_roll_list']}")


def reset_unlucky_roll_list(player_id):
    players[f'{player_id}']['unlucky_roll_list'] = []


def update_player_current_postion(player_id: int) -> None:
    """update players_current_position

    Args:
        player_id (int): player_id
    """
    new_pos = players[f'{player_id}']['new_position']
    if new_pos is not None:
        players[f'{player_id}']['current_position'] = new_pos
    print(f"players = {players}")


def get_player_current_postion(player_id: int) -> int:
    """Get Player Current position

    Args:
        player_id (int): Player id

    Returns:
        int: player current position
    """
    current_postion = players[f'{player_id}']['current_position']
    return current_postion


def get_players_new_position(player_id: int) -> int:
    """Get Player New Position

    Args:
        player_id (int): Player id

    Returns:
        int: players new position
    """
    new_pos = players[f'{player_id}']['new_position']
    return new_pos


def update_snake_byte_count(player_id: int) -> int:
    """_summary_

    Args:
        player_id (int): _description_

    Returns:
        int: _description_
    """
    players[f'{player_id}']['snake_bite_count'] = players[f'{player_id}']['snake_bite_count'] + 1


def update_players_projected_new_position(player_id: int, pos: int) -> None:
    """Update Players projected new position

    Args:
        player_id (int): _description_
    """
    # if not players[f'{player_id}']['is_completed_game']:
    players[f'{player_id}']['projected_new_position'] = pos


def get_players_projected_new_position(player_id: int) -> int:
    """Get players projected new position

    Args:
        player_id (int): player id

    Returns:
        int: projected position
    """
    projected_new_pos = players[f'{player_id}']['projected_new_position']
    return projected_new_pos


def calulate_players_new_position(player_id: int, dice_sum: int):
    """Calculate and update players projected new position and confirmed new pos

    Args:
        player_id (int): player id
        dice_sum (int): dice roll sum

    Returns:
        None:
    """
    global winner_pos
    confirmed_new_pos = None
    current_position = get_player_current_postion(player_id=player_id)
    projected_new_position = current_position + dice_sum

    if (projected_new_position > 100) and get_overrun_count(player_id=player_id) <= 10:
        print(f"Cant play as {projected_new_position} is > 100")
        increment_overrun_count(player_id=player_id)
        update_players_unlucky_roll_list(player_id=player_id, unlucky_roll_sum=dice_sum)
        projected_new_position = current_position
        confirmed_new_pos = current_position

    elif projected_new_position == 100:
        print(f"{player_id} is Winner")
        confirmed_new_pos = 100
        update_is_completed_game(player_id=player_id, status=1)
        update_winner_position(player_id=player_id, pos=winner_pos)
        update_winners_list(player_id=player_id)
        winner_pos = winner_pos + 1
        update_players_projected_new_position(player_id=player_id, pos=projected_new_position)
        update_player_new_position(player_id=player_id, confirmed_new_pos=confirmed_new_pos)

    else:
        # confirm tentative_new position from backend module 2
        status, confirmed_new_pos = snake_and_ladder_check.snake_and_ladder_check(
            projected_new_position=projected_new_position)
        reset_overrun_count(player_id=player_id)
        if status == "Ladder":
            increment_players_ladder_encountered_count(player_id=player_id)
        elif status == "Snake":
            increment_players_snake_bite_count(player_id=player_id)
        if len(get_unlucky_roll_list(player_id=player_id)) > 0:
            # reset players unlucky_roll_list
            print(f"reset players unlucky roll list")
            reset_unlucky_roll_list(player_id=player_id)

    update_players_projected_new_position(player_id=player_id, pos=projected_new_position)
    update_player_new_position(player_id=player_id, confirmed_new_pos=confirmed_new_pos)
    return projected_new_position, confirmed_new_pos


def get_players_movement_sequence(player_id: int) -> List:
    """Get Players positions movement sequence

    Args:
        player_id (int): _description_
    """
    tentative_position = get_players_projected_new_position(player_id=player_id)
    new_position = get_players_new_position(player_id=player_id)
    return tentative_position, new_position


def update_consecutive_turn_all_players(player_id: int):
    """ update consecutive_turn for all players,
    this function increases consecutive_turn for player whos player id matches,
    otherwise resets consecutive_turn

    Args:
        player_id (int): player id
    """
    for key in players.keys():
        if key != f'{player_id}':
            reset_consecutive_turn_count(key)
        else:
            increment_consecutive_turn_count(key)


def play(player_id: int, dice_sum: int):
    """ Play for players id, this function calculates player's projected new position and
    confirmed new position based on player's current position and dice sum

    Args:
        player_id (int): player id
        dice_sum (int): dice sum

    Returns:
        (int, int) : projected_new_position and confirmed_new_position
    """

    projected_new_position, confirmed_new_position = calulate_players_new_position(player_id=player_id,
                                                                                   dice_sum=dice_sum)

    # update consecutive_turn for all players
    update_consecutive_turn_all_players(player_id=player_id)
    return projected_new_position, confirmed_new_position


def update_winners_list(player_id: int):
    """Update winner list

    Args:
        player_id (int): player id
    """
    global winners
    winners.append(player_id)


def get_winners() -> List:
    """Returns winners list in winning order

    Returns:
        List: winners list
    """

    return winners