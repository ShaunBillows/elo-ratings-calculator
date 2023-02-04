import pandas as pd
import datetime
from error_handler import ErrorHandler
from logger import Logger

class EloCalculator:
    """
    This class calculates Elo ratings for matches in a Premier League season from a CSV file containing processed matches data.

    Methods:
        calculate_individual_elo_ratings(home_score: int, away_score: int, home_elo: int, away_elo: int) -> Tuple[int, int]:
            Calculates individual Elo ratings based on the match result and the initial ratings of both teams.
        
        calculate_elo_ratings_for_one_week(csv_file:str, output_file:str, weeks: int = None):
            Calculates Elo ratings for one week of matches and saves the result to an output file.
        
        calculate_elo_ratings_for_each_week(csv_file:str, output_dir:str, nb_weeks_in_season:int):
            Calculates Elo ratings for each week in a season, up to a specified week, and saves the results as CSV files in the output directory.
        
        calculate_elo_ratings_for_each_match(csv_file:str, output_file:str):
            Calculates Elo ratings for each match in a season and saves the results to an output file.
    """

    def __init__(self):
        self.error_handler = ErrorHandler(log_destination='file')
        self.logger = Logger().logger

    def calculate_individual_elo_ratings(self, home_score: int, away_score: int, home_elo: int, away_elo: int):
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

    def calculate_elo_ratings_for_one_week(self, csv_file:str, output_file: str, weeks: int = None):
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
            self.error_handler.log_error(f"Please specify a valid number of weeks (up to {nb_weeks_in_season})")
            return
        else:
            # calculate number of matches to be taken into account 
            matches_to_consider = weeks * nb_games_per_week
            matches_considered = matches[:matches_to_consider]
        # Initialize Elo ratings for all 20 teams
        elo_ratings = {}
        teams = pd.unique(df[['home-name', 'away-name']].values.ravel())
        for team in teams:
            elo_ratings[team] = 1000
        # Iterate through each game
        for match in matches_considered:
            home_team = match['home-name']
            away_team = match['away-name']
            home_score = match['home-result']
            away_score = match['away-result']
            home_elo = elo_ratings[home_team]
            away_elo = elo_ratings[away_team]
            # Update Elo ratings for both teams
            home_new_elo, away_new_elo = self.calculate_individual_elo_ratings(home_score, away_score, home_elo, away_elo)
            elo_ratings[home_team] = home_new_elo
            elo_ratings[away_team] = away_new_elo
        # Save the results as a csv file
        df = pd.DataFrame(list(elo_ratings.items()), columns=['Team', 'Rating'])
        df.to_csv(output_file, index=False)
        self.logger.info(f'Elo ratings for week {weeks} have been calculated and saved to {output_file}')

    def calculate_elo_ratings_for_each_week(self, csv_file:str, output_dir:str, nb_weeks_in_season:int):
        """
        Calculates the Elo ratings of all teams in a premier league season based on the outcome of games, and saves the ratings for each week to a csv file.
        The function takes a csv file containing match information as an input, and the number of weeks in the season, and outputs the Elo ratings as csv files, one for each week.
        
        Args:
            csv_file (str): path to the csv file containing the match information
            output_dir (str): path to the directory where the Elo ratings will be saved as csv files
            nb_weeks_in_season (int): the number of weeks in the season
            
        """

        try:
            for week in range(nb_weeks_in_season):
                # call the calculate_elo_ratings function for each week
                self.calculate_elo_ratings_for_one_week(csv_file=csv_file, output_file=f'{output_dir}/week-{week}.csv', weeks=week)
            self.logger.info(f'Elo ratings for the season have been calculated and saved to {output_dir}')

        except FileNotFoundError as e:
            self.error_handler.log_error(f'File not found: {e}')
        except Exception as e:
            self.error_handler.log_error(f'An error occurred: {e}')

    def calculate_elo_ratings_for_each_match(self, csv_file:str, output_file:str):
        """
        Calculates Elo ratings for each match in a Premier League season and outputs the results to a specified CSV file, while also appending selected match data, such as bookmakers' odds, date, and results, from the input CSV file.
        Args:
            csv_file: A string indicating the file path of the input CSV containing processed match results data.
            output_file: A string indicating the file path to save the output CSV with calculated Elo ratings and appended match data.
        """

        # retrieve the matches information from a csv file
        try:
            df = pd.read_csv(csv_file, na_values=["N/A", "-", "?"])
        except FileNotFoundError:
            self.error_handler.log_error(f'The file {csv_file} could not be found')
            return
        matches = df.to_dict('records')
        # Initialize Elo ratings for all teams
        elo_ratings = {}
        teams = pd.unique(df[['home-name', 'away-name']].values.ravel())
        for team in teams:
            elo_ratings[team] = 1000
        # initialize the dataframe to store the elo ratings and bookmakers odds
        results_df = pd.DataFrame(columns=['home-name','away-name','home-elo','away-elo','home-win-odds','draw-odds','away-win-odds','home-result','away-result','match-date'])
        # Iterate through each game
        for match in matches:
            try:
                home_name = match['home-name']
                away_name = match['away-name']
                home_result = match['home-result']
                away_result = match['away-result']
                home_odds_avg = 1/(match['home-odds-avg'] + 1)
                draw_odds_avg = 1/(match['draw-odds-avg'] + 1)
                away_odds_avg = 1/(match['away-odds-avg'] + 1)
                epoch_time = match['date-start-timestamp']
                match_date = datetime.datetime.fromtimestamp(match['date-start-timestamp'])
                home_elo = elo_ratings[home_name]
                away_elo = elo_ratings[away_name]
                # calculate the elo probability for home win, draw and away win
                home_exp = 1 / (1 + 10 ** ((away_elo - home_elo) / 400))
                away_exp = 1 - home_exp
                draw_exp = 1 - home_exp - away_exp
                # Calculate the Elo home/away win probabilities
                home_win_elo = home_exp
                away_win_elo = away_exp
                draw_elo = 1 - (home_exp + away_exp)
                # Calculate the probabilities using the bookmakers odds for a draw
                # - allows for a direct comparison with the bookmakers
                draw_elo_bookies_draw_odds = draw_odds_avg
                home_win_elo_bookies_draw_odds = home_win_elo * (1 - draw_odds_avg)
                away_win_elo_bookies_draw_odds = away_win_elo * (1 - draw_odds_avg)
                # Update Elo ratings for both teams
                home_new_elo, away_new_elo = self.calculate_individual_elo_ratings(home_result, away_result, home_elo, away_elo)
                elo_ratings[home_name] = home_new_elo
                elo_ratings[away_name] = away_new_elo
                # append the results to the dataframe
                new_row = pd.DataFrame({'home-name':home_name,'away-name':away_name,'home-elo':home_new_elo,'away-elo':away_new_elo,'home-win-odds':home_odds_avg,'draw-odds':draw_odds_avg,'away-win-odds':away_odds_avg,'home-result':home_result,'away-result':away_result,'match-date':match_date, 'epoch_time': epoch_time, 'home-win-elo':home_win_elo,'draw-elo':draw_elo,'away-win-elo':away_win_elo, 'home_win_elo_bookies_draw_odds':home_win_elo_bookies_draw_odds, 'away_win_elo_bookies_draw_odds':away_win_elo_bookies_draw_odds, 'draw_elo_bookies_draw_odds':draw_elo_bookies_draw_odds }, index=[0])
                results_df = pd.concat([results_df, new_row], ignore_index=True)
            except KeyError as e:
                self.error_handler.log_error(f'Error when accessing match data: {e}')
                return
        # Save the results as a csv file
        try:
            results_df.to_csv(output_file, index=False)
            self.logger.info(f'Elo ratings for matches in the season have been calculated and saved to {output_file}')
        except IOError:
            self.error_handler.log_error(f"The directory specified in {output_file} does not exist. Please specify a valid directory.")
