from match_results_generator import JSONProcessor
from elo_ratings_calculator import EloCalculator
from grapher import Grapher

if __name__ == "__main__":

    """ Section 1: Process raw data """
    
    # # # Set up input and output file paths
    # json_file_20_21 = './data/raw-data/20-21'
    # output_dir_20_21 = './data/processed-data/20-21.csv'
    # json_file_19_20 = './data/raw-data/19-20'
    # output_dir_19_20 = './data/processed-data/19-20.csv'
    # json_file_21_22 = './data/raw-data/21-22'
    # output_dir_21_22 = './data/processed-data/21-22.csv'
    # json_file_22_23 = './data/raw-data/22-23'
    # output_dir_22_23 = './data/processed-data/22-23.csv'

    # # Process raw data for 19-20 season
    # processor = JSONProcessor(json_file_20_21, output_dir_20_21)
    # processor.generate_match_results_csv()
    # # Process raw data for 19-20 season
    # processor = JSONProcessor(json_file_19_20, output_dir_19_20)
    # processor.generate_match_results_csv()
    # # Process raw data for 19-20 season
    # processor = JSONProcessor(json_file_21_22, output_dir_21_22)
    # processor.generate_match_results_csv()
    # # Process raw data for 19-20 season
    # processor = JSONProcessor(json_file_22_23, output_dir_22_23)
    # processor.generate_match_results_csv()

    """ Section 2: Calculate Elo ratings for each week """

    # # Set up input and output file paths
    # csv_file_20_21 = './data/processed-data/20-21.csv'
    # output_dir_20_21 = './data/results/elo-ratings/20-21/week-data'
    # csv_file_19_20 = './data/processed-data/19-20.csv'
    # output_dir_19_20 = './data/results/elo-ratings/19-20/week-data'
    # csv_file_21_22 = './data/processed-data/21-22.csv'
    # output_dir_21_22 = './data/results/elo-ratings/21-22/week-data'
    # csv_file_22_23 = './data/processed-data/22-23.csv'
    # output_dir_22_23 = './data/results/elo-ratings/22-23/week-data'

    # # # Number of weeks in a season (0 - 39 weeks)
    # nb_weeks_in_season = 39

    # # initialise an instance of the EloCalculator class
    # elo_calculator = EloCalculator()
    
    # # Calculate Elo ratings for 20-21 season
    # elo_calculator.calculate_elo_ratings_for_each_week(csv_file_20_21, output_dir_20_21, nb_weeks_in_season)
    # # # Calculate Elo ratings for 19-20 season
    # elo_calculator.calculate_elo_ratings_for_each_week(csv_file_19_20, output_dir_19_20, nb_weeks_in_season)
    # # # Calculate Elo ratings for 21-22 season
    # elo_calculator.calculate_elo_ratings_for_each_week(csv_file_21_22, output_dir_21_22, nb_weeks_in_season)
    # # # Calculate Elo ratings for 22-23 season
    # elo_calculator.calculate_elo_ratings_for_each_week(csv_file_22_23, output_dir_22_23, nb_weeks_in_season)

    """ Section 3: Calculate Elo ratings for each match """

    # # # Set up input and output file paths
    # csv_file_20_21 = './data/processed-data/20-21.csv'
    # output_file_20_21 = './data/results/elo-ratings/20-21/match-data/index.csv'
    # csv_file_19_20 = './data/processed-data/19-20.csv'
    # output_file_19_20 = './data/results/elo-ratings/19-20/match-data/index.csv'
    # csv_file_21_22 = './data/processed-data/21-22.csv'
    # output_file_21_22 = './data/results/elo-ratings/21-22/match-data/index.csv'
    # csv_file_22_23 = './data/processed-data/22-23.csv'
    # output_file_22_23 = './data/results/elo-ratings/22-23/match-data/index.csv'

    # # # initialise an instance of the EloCalculator class
    # elo_calculator = EloCalculator()

    # # Calculate Elo ratings for 20-21 season
    # elo_calculator.calculate_elo_ratings_for_each_match(csv_file_20_21, output_file_20_21)
    # # Calculate Elo ratings for 19-20 season
    # elo_calculator.calculate_elo_ratings_for_each_match(csv_file_19_20, output_file_19_20)
    # # Calculate Elo ratings for 21-22 season
    # elo_calculator.calculate_elo_ratings_for_each_match(csv_file_21_22, output_file_21_22)
    # # # Calculate Elo ratings for 22-23 season
    # elo_calculator.calculate_elo_ratings_for_each_match(csv_file_22_23, output_file_22_23)

    """ Section 4: Scatter plot Elo probability vs bookmakers probability (WIP)"""

    # Set up input and output file paths
    title_19 = '19-20'
    csv_file_20_21 = './data/results/elo-ratings/19-20/match-data/index.csv'
    output_file_20_21 = './data/results/elo-ratings/19-20/match-data/elo-vs-bookies-probabilities-19-20.png'
    title_20 = '20-21'
    csv_file_19_20 = './data/results/elo-ratings/20-21/match-data/index.csv'
    output_file_19_20 = './data/results/elo-ratings/20-21/match-data/elo-vs-bookies-probabilities-20-21.png'
    title_21 = '21-22'
    csv_file_21_22 = './data/results/elo-ratings/21-22/match-data/index.csv'
    output_file_21_22 = './data/results/elo-ratings/21-22/match-data/elo-vs-bookies-probabilities-21-22.png'
    title_22 = '22-23'
    csv_file_22_23 = './data/results/elo-ratings/22-23/match-data/index.csv'
    output_file_22_23 = './data/results/elo-ratings/22-23/match-data/elo-vs-bookies-probabilities-22-23.png'

    # # initialise an instance of the Grapher class
    grapher = Grapher()

    # Create scatter graphs for Elo vs bookmakers probabilities
    grapher.plot_elo_bookies_scatter(csv_file=csv_file_19_20, output_file=output_file_19_20, title=title_19)
    grapher.plot_elo_bookies_scatter(csv_file=csv_file_20_21, output_file=output_file_20_21, title=title_20)
    grapher.plot_elo_bookies_scatter(csv_file=csv_file_21_22, output_file=output_file_21_22, title=title_21)
    grapher.plot_elo_bookies_scatter(csv_file=csv_file_22_23, output_file=output_file_22_23, title=title_22)
