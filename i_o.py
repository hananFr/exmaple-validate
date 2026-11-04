from data import teams

from validations import is_positive_integer

def get_input(msg, validation, *args, **kwargs):
    valid_input = False
    while not valid_input:
        input_value = input(msg)
        valid_input, error_msg = validation(input_value, *args, **kwargs)
        if not valid_input:
            print(error_msg)
    return input_value


def is_exist_team(team_id, teams):
    for team in teams:
        if team["id"] == team_id:
            return True, None
    return False, "team is not exist"

def get_exist_team(msg):
    exist_team = False
    value = input(msg)
    while not is_positive_integer(value) and not exist_team:
        value = input(msg)
        if not is_positive_integer(value):
            print('Is not an integer')
            continue
        exist_team = is_exist_team(value, teams)
        if not exist_team:
            print('Team does not exists')
    return value

