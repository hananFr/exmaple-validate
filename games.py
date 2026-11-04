from data import teams,matches
from i_o import get_input
from validations import valid_integer,input_team_validation, is_exist_and_diff

def add_result():
    home_id = get_input("Insert home team id\n", input_team_validation)
    away_id = get_input("Insert away team id\n", is_exist_and_diff, home_id, teams)

    print(home_id, away_id)

add_result()



