import logging
from typing import List, Dict

players={}

def create_players(num_of_players: int):
    """ create palyers based on input provided 

    Args:
        num_of_players (int): number of players participating in game

    Returns:
        List[dict]: List of palayers participating in game, Each player is represented as dictionary
    """

    for count in range(num_of_players):
        # players[f'{count}+1'] = {
        #         'current_position': 0,
        #         'new_position': 0,
        #         'is_reached_end_tile': False,
        #         'Winner_pos': 0,
        #         'got_next_turn': False,
        #         'snake_bite_count': 0,
        #         'ladder_encountered_count': 0
        #         }
        player = {
                'current_position': 0,
                'projected_new_position': 0,
                'new_position': 0,
                'is_reached_end_tile': False,
                'Winner_pos': 0,
                'got_next_turn': False,
                'snake_bite_count': 0,
                'ladder_encountered_count': 0
                }
        players[f'{count+1}'] = player
    logging.info(f"Created players : {players}")
    print(f"Created players : {players}")
    return players    


def update_player_new_position(player_id: int , confirmed_new_pos: int) -> None:
    """ update players new_postion

    Args:
        player_id (int): player id
        confirmed_new_pos (int): new player position
    """
    players[f'{player_id}']['new_postion'] = confirmed_new_pos
    print(f"updated players new_position to {confirmed_new_pos}")


def update_player_current_postion(player_id : int) -> None:
    """update players_current_position

    Args:
        player_id (int): player_id
    """
    new_pos = players[f'{player_id}']['new_position']
    if new_pos is not None:
        players[f'{player_id}']['current_position'] = new_pos
        print(f"updated players current_position to {new_pos}")
    

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


def update_players_projected_new_position(player_id:int, pos:int) ->  None:
    """Update Players projected new position

    Args:
        player_id (int): _description_
    """
    players[f'{player_id}']['projected_new_position'] = players[f'{player_id}']['projected_new_position'] + pos


def get_players_projected_new_position(player_id:int )->int:
    """Get players projected new position

    Args:
        player_id (int): player id

    Returns:
        int: projected position
    """
    projected_new_pos = players[f'{player_id}']['projected_new_position']
    return projected_new_pos


def calulate_players_new_position(player_id:int, dice_sum: int ):
    """
    Args:
        player_id (int): _description_
    """
    current_position = get_player_current_postion(player_id=player_id)
    projected_new_position = current_position + dice_sum
    update_players_projected_new_position(player_id=player_id, pos=projected_new_position)

    # confirm tentative_new position from backend module 2
    # confirmed_new_pos = backend_stub(tentative_new_position)
    confirmed_new_pos = projected_new_position # need to remove once above function is done by Sufi
    return confirmed_new_pos


def get_players_movement_sequence(player_id:int) -> List:
    """Get Players positions movement sequence

    Args:
        player_id (int): _description_
    """
    tentative_position=get_players_projected_new_position(player_id=player_id)
    new_position = get_players_new_position(player_id=player_id)
    return tentative_position, new_position


