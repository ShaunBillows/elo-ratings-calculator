import logging
# from generate_match_results_csv.generate_match_results_csv import generate_match_results_csv
from elo_ratings_calculator import calculate_elo_ratings_for_each_week, calculate_elo_ratings_for_each_match
from graphs import plot_elo_bookies_scatter

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    """ Section 1: Process raw data (WIP) """
    # Process raw data
    # 19-20
    # generate_match_results_csv("./raw-data/20-21", './processed-data/22-23csv')
    # process_json_files("./raw-data/20-21", process_json_callback)
    # save_to_csv(results, './processed-data/20-21.csv')

    """ Section 2: Calculate Elo ratings for each week """

    # # Set up input and output file paths
    # csv_file_20_21 = './processed-data/20-21.csv'
    # output_dir_20_21 = './elo-ratings/20-21/week'
    # csv_file_19_20 = './processed-data/19-20.csv'
    # output_dir_19_20 = './elo-ratings/19-20/week'
    # csv_file_21_22 = './processed-data/21-22.csv'
    # output_dir_21_22 = './elo-ratings/21-22/week'
    # csv_file_22_23 = './processed-data/22-23.csv'
    # output_dir_22_23 = './elo-ratings/22-23/week'

    # # # Number of weeks in a season (0 - 39 weeks)
    # nb_weeks_in_season = 39
    
    # # Calculate Elo ratings for 20-21 season
    # calculate_elo_ratings_for_each_week(csv_file_20_21, output_dir_20_21, nb_weeks_in_season)
    # logging.info(f'Elo ratings for weeks in the 20-21 season have been calculated and saved to {output_dir_20_21}')

    # # Calculate Elo ratings for 19-20 season
    # calculate_elo_ratings_for_each_week(csv_file_19_20, output_dir_19_20, nb_weeks_in_season)
    # logging.info(f'Elo ratings for weeks in the 19-20 season have been calculated and saved to {output_dir_19_20}')

    # # Calculate Elo ratings for 21-22 season
    # calculate_elo_ratings_for_each_week(csv_file_21_22, output_dir_21_22, nb_weeks_in_season)
    # logging.info(f'Elo ratings for weeks in the 21-22 season have been calculated and saved to {output_dir_21_22}')
    
    # # Calculate Elo ratings for 22-23 season
    # calculate_elo_ratings_for_each_week(csv_file_22_23, output_dir_22_23, nb_weeks_in_season)
    # logging.info(f'Elo ratings for weeks in the 22-23 season have been calculated and saved to {output_dir_22_23}')

    """ Section 3: Calculate Elo ratings for each match """

    # # # Set up input and output file paths
    # csv_file_20_21 = './processed-data/20-21.csv'
    # output_file_20_21 = './elo-ratings/20-21/match/index.csv'
    # csv_file_19_20 = './processed-data/19-20.csv'
    # output_file_19_20 = './elo-ratings/19-20/match/index.csv'
    # csv_file_21_22 = './processed-data/21-22.csv'
    # output_file_21_22 = './elo-ratings/21-22/match/index.csv'
    # csv_file_22_23 = './processed-data/22-23.csv'
    # output_file_22_23 = './elo-ratings/22-23/match/index.csv'

    # # Calculate Elo ratings for 20-21 season
    # calculate_elo_ratings_for_each_match(csv_file_20_21, output_file_20_21)
    # logging.info(f'Elo ratings for matches in the 20-21 season have been calculated and saved to {output_file_20_21}')

    # # Calculate Elo ratings for 19-20 season
    # calculate_elo_ratings_for_each_match(csv_file_19_20, output_file_19_20)
    # logging.info(f'Elo ratings for matches in the 19-20 season have been calculated and saved to {output_file_19_20}')

    # # Calculate Elo ratings for 21-22 season
    # calculate_elo_ratings_for_each_match(csv_file_21_22, output_file_21_22)
    # logging.info(f'Elo ratings for matches in the 21-22 season have been calculated and saved to {output_file_21_22}')
    
    # # # Calculate Elo ratings for 22-23 season
    # calculate_elo_ratings_for_each_match(csv_file_22_23, output_file_22_23)
    # logging.info(f'Elo ratings for matches in the 22-23 season have been calculated and saved to {output_file_22_23}')

    """ Section 4: Scatter plot Elo probability vs bookmakers probability (WIP)"""

    # Set up input and output file paths
    title_19 = '19-20'
    csv_file_20_21 = './elo-ratings/19-20/match/index.csv'
    output_file_20_21 = './elo-ratings/19-20/match/elo-vs-bookies-probabilities-19-20.png'
    title_20 = '20-21'
    csv_file_19_20 = './elo-ratings/20-21/match/index.csv'
    output_file_19_20 = './elo-ratings/20-21/match/elo-vs-bookies-probabilities-20-21.png'
    title_21 = '21-22'
    csv_file_21_22 = './elo-ratings/21-22/match/index.csv'
    output_file_21_22 = './elo-ratings/21-22/match/elo-vs-bookies-probabilities-21-22.png'
    title_22 = '22-23'
    csv_file_22_23 = './elo-ratings/22-23/match/index.csv'
    output_file_22_23 = './elo-ratings/22-23/match/elo-vs-bookies-probabilities-22-23.png'

    # Create scatter graphs for Elo vs bookmakers probabilities
    plot_elo_bookies_scatter(csv_file=csv_file_19_20, output_file=output_file_19_20, title=title_19)
    plot_elo_bookies_scatter(csv_file=csv_file_20_21, output_file=output_file_20_21, title=title_20)
    plot_elo_bookies_scatter(csv_file=csv_file_21_22, output_file=output_file_21_22, title=title_21)
    plot_elo_bookies_scatter(csv_file=csv_file_22_23, output_file=output_file_22_23, title=title_22)
