from data import teams,matches

def valid_integer(team_id: str):
    return team_id.isdigit(), "You must choose an positive integer"

def is_exist_team(team_id, teams):
    for team in teams:
        if team["id"] == team_id:
            return True, None
    return False, "team is not exist"

def input_team_validation(team_id):
    is_integer, error_msg = valid_integer(team_id)
    if not is_integer:
        return False, error_msg

    return is_exist_team(int(team_id), teams) 
    

def is_exist_and_diff( team_id, home_id, teams):
    is_valid, error_msg = input_team_validation(team_id)
    if not is_valid:
        return is_valid, error_msg
    if team_id == home_id:
        return False, "Teams must be diff"
    return True, None
    

def first_meeting(first_team, second_team, matches: list):
    for match in matches:
        if (match["home_team_id"] == first_team and match["away_team_id"] == second_team) or (match["home_team_id"] == second_team and match["away_team_id"] == first_team):
            return False
    return True
            
def is_positive_integer(s:str):
    return s.isdigit()