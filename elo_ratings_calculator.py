import pandas as pd

def elo_rating(home_score, away_score, home_elo, away_elo):
    """
    Updates the Elo ratings of the home and away teams based on the outcome of the game.
    
    Args:
        home_team (str): name of the home team
        away_team (str): name of the away team
        home_score (int): number of goals scored by the home team
        away_score (int): number of goals scored by the away team
        home_elo (int): current Elo rating of the home team
        away_elo (int): current Elo rating of the away team
        
    Returns:
        tuple: new Elo ratings for the home and away teams
    """

    # expected scores for the home and away teams based on their current ratings
    home_exp = 1 / (1 + 10 ** ((away_elo - home_elo) / 400))
    away_exp = 1 - home_exp

    # determine k-factor based on the rating difference between the two teams
    if abs(home_elo - away_elo) <= 400:
        k = 32
    elif abs(home_elo - away_elo) <= 800:
        k = 24
    else:
        k = 16
        
    # update Elo ratings based on the outcome of the game and the expected scores
    if home_score > away_score:
        home_new_elo = home_elo + k * (1 - home_exp)
        away_new_elo = away_elo + k * (0 - away_exp)
    elif home_score < away_score:
        home_new_elo = home_elo + k * (0 - home_exp)
        away_new_elo = away_elo + k * (1 - away_exp)
    else:
        home_new_elo = home_elo + k * (0.5 - home_exp)
        away_new_elo = away_elo + k * (0.5 - away_exp)
    return home_new_elo, away_new_elo

def calculate_elo_ratings(csv_file:str, output_file: str, weeks: int = None):
    """
    Calculates the Elo ratings for all teams in a premier league season, based on the outcome of the games. 
    The function takes a csv file containing match information as an input, and outputs the Elo ratings as a csv file.
    Optionally, the number of weeks of the season to consider can be specified. If not specified, the entire season will be considered.
    
    Args:
        csv_file (str): path to the csv file containing the match information
        output_file (str): path to the csv file where the Elo ratings will be saved
        weeks (int): optional parameter for the number of weeks of the season to consider 
    """
    
    # retrieve the matches information about a premier league season from a csv file
    df = pd.read_csv(csv_file)
    matches = df.to_dict('records')
    # number of games per week for the league
    nb_games_per_week = 10
    nb_weeks_in_season = len(matches) / nb_games_per_week
    # if weeks is not specified, we consider the whole season
    if weeks is None:
        matches_considered = matches
    # if the number of weeks specified is greater than the total number of weeks in the season,
    # prompt the user to specify a valid number of weeks
    elif weeks > nb_weeks_in_season:
        print(f"Please specify a valid number of weeks (up to {nb_weeks_in_season})")
        return
    else:
        # calculate number of matches to be taken into account 
        matches_to_consider = weeks * nb_games_per_week
        matches_considered = matches[:matches_to_consider]
    # Initialize Elo ratings for all 20 teams
    elo_ratings = {}
    for i in range(nb_games_per_week):
        elo_ratings[matches[i]['home-name']] = 1000
        elo_ratings[matches[i]['away-name']] = 1000
    # Iterate through each game
    for match in matches_considered:
        home_team = match['home-name']
        away_team = match['away-name']
        home_score = match['home-result']
        away_score = match['away-result']
        home_elo = elo_ratings[home_team]
        away_elo = elo_ratings[away_team]
        # Update Elo ratings for both teams
        home_new_elo, away_new_elo = elo_rating(home_score, away_score, home_elo, away_elo)
        elo_ratings[home_team] = home_new_elo
        elo_ratings[away_team] = away_new_elo
    # Save the results as a csv file
    df = pd.DataFrame(list(elo_ratings.items()), columns=['Team', 'Rating'])
    df.to_csv(output_file, index=False)
