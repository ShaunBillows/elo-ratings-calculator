from match_results_generator import JSONProcessor
from elo_ratings_calculator import EloCalculator
from grapher import Grapher

if __name__ == "__main__":

    """ Section 1: Process raw data """
    
    # # List of seasons and corresponding raw and processed data paths
    # seasons = [
    #     ('./data/raw-data/20-21', './data/processed-data/20-21.csv'),
    #     ('./data/raw-data/19-20', './data/processed-data/19-20.csv'),
    #     ('./data/raw-data/21-22', './data/processed-data/21-22.csv'),
    #     ('./data/raw-data/22-23', './data/processed-data/22-23.csv')
    # ]

    # # Process raw data for each season
    # for raw_data, processed_data in seasons:
    #     processor = JSONProcessor(raw_data, processed_data)
    #     processor.generate_match_results_csv()

    """ Section 2: Calculate Elo ratings for each season """
    
    # # Input File paths
    # file_paths = {
    #     "20-21": "./data/processed-data/20-21.csv",
    #     "19-20": "./data/processed-data/19-20.csv",
    #     "21-22": "./data/processed-data/21-22.csv",
    #     "22-23": "./data/processed-data/22-23.csv"
    # }

    # # Number of weeks to calculate Elo ratings for (valid range: 0 to 39)
    # target_week = 39

    # # Output Directories and Files for Elo Ratings by Match and Week
    # output_dirs = {
    #     "20-21": {
    #         "week-data": "./data/results/elo-ratings/20-21/week-data",
    #         "match-data": "./data/results/elo-ratings/20-21/match-data/index.csv"
    #     },
    #     "19-20": {
    #         "week-data": "./data/results/elo-ratings/19-20/week-data",
    #         "match-data": "./data/results/elo-ratings/19-20/match-data/index.csv"
    #     },
    #     "21-22": {
    #         "week-data": "./data/results/elo-ratings/21-22/week-data",
    #         "match-data": "./data/results/elo-ratings/21-22/match-data/index.csv"
    #     },
    #     "22-23": {
    #         "week-data": "./data/results/elo-ratings/22-23/week-data",
    #         "match-data": "./data/results/elo-ratings/22-23/match-data/index.csv"
    #     }
    # }

    # for season, file_path in file_paths.items():
    #     # Calculate Elo ratings for each season
    #     elo_calculator = EloCalculator("csv", file_path)
    #     elo_calculator.calculate_elo_ratings_for_each_match("csv", output_dirs[season]["match-data"])
    #     elo_calculator.calculate_elo_ratings_for_each_week("csv", output_dirs[season]["week-data"], target_week)

    """ Section 3: Scatter plot Elo probability vs bookmakers probability """

    # Set up paths for input and output files
    title_seasons = [('19-20 Premier League', '19-20'), 
                    ('20-21 Premier League', '20-21'), 
                    ('21-22 Premier League', '21-22'), 
                    ('22-23 Premier League', '22-23')]
    
    data_dir = './data/results/elo-ratings/{}/match-data/'
    csv_files = [data_dir.format(season) + 'index.csv' for _, season in title_seasons]
    output_files = [data_dir.format(season) + 'elo-vs-bookies-probabilities-{}.png'.format(season) for _, season in title_seasons]

    # Initialise an instance of the Grapher class
    grapher = Grapher()

    # Create scatter graphs for Elo vs bookmakers probabilities
    for title, csv_file, output_file in zip(title_seasons, csv_files, output_files):
        grapher.get_data_from_csv(csv_file)
        grapher.plot_elo_bookies_scatter(output_file=output_file, title=title[0], show=False)

    # Note: there is currently a bug causing all the graphs to display if only the last 'show' is set to True
