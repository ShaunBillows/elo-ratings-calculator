import logging
from elo_ratings_calculator.elo_ratings_calculator import calculate_elo_ratings_for_one_week, calculate_elo_ratings_for_each_week

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Set up input and output file paths
    # csv_file_20_21 = './processed-data/20-21.csv'
    # output_file_20_21 = './elo-ratings/20-21'
    # csv_file_19_20 = './processed-data/19-20.csv'
    # output_file_19_20 = './elo-ratings/19-20'
    csv_file_21_22 = './processed-data/21-22.csv'
    output_file_21_22 = './elo-ratings/21-22'

    # Number of weeks in a season
    nb_weeks_in_season = 39
    
    # # Calculate Elo ratings for 20-21 season
    # calculate_elo_ratings_for_each_week(csv_file_20_21, output_file_20_21, nb_weeks_in_season)
    # logging.info(f'Elo ratings for the 20-21 season have been calculated and saved to {output_file_20_21}')

    # # Calculate Elo ratings for 19-20 season
    # calculate_elo_ratings_for_each_week(csv_file_19_20, output_file_19_20, nb_weeks_in_season)
    # logging.info(f'Elo ratings for the 19-20 season have been calculated and saved to {output_file_19_20}')

    # Calculate Elo ratings for 21-22 season
    calculate_elo_ratings_for_each_week(csv_file_21_22, output_file_21_22, nb_weeks_in_season)
    logging.info(f'Elo ratings for the 21-22 season have been calculated and saved to {output_file_21_22}')
    