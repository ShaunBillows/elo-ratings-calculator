import os
import pandas as pd
from logger import Logger
from error_handler import ErrorHandler

class JSONProcessor:
    """
    This class processes all the JSON files in a given folder containing raw match result data, and converts the data into a CSV file in a format suitable for generating Elo ratings. The processed data includes information such as the home and away team names, scores, and odds from a range of bookmakers. The resulting CSV file can then be used as input for generating Elo ratings of teams in a given league or season, and the bookmakers odds can be used to test and optimise the algorithm to create a (hopefully successful) betting system.

    Methods:
        process_json_files(folder_path, process_json_callback): Processes all the JSON files in the given folder, passing each file to the `process_json_callback` function. The function accepts a path to the folder containing the JSON files, and a callback function to process the data from each JSON file.
        process_json_callback(data): The function to process the data from each JSON file. It accepts a dictionary of data and returns a dictionary of processed data.
        save_to_csv(data, file_name): Saves the processed data to a CSV file. It accepts a dictionary of data and a file name string and returns a CSV file.
        generate_match_results_csv(folder_path, csv_file): Brings everything together, processing all the data from a season and converting it to a CSV file. It accepts a path to the folder containing the JSON files and a file name string for the resulting CSV file.

    Attributes:
        folder_path (str): The path to the folder containing the JSON files.
        csv_file (str): The name of the resulting CSV file.
        results (list): A list of dictionaries, each representing a row of processed data.
        logger (class): The Logger class handles all logging messages for better readability and maintainability.
    """
    
    def __init__(self, folder_path, csv_file):
        self.folder_path = folder_path
        self.csv_file = csv_file
        self.results = []
        self.logger = Logger().logger
        self.error_handler = ErrorHandler(log_destination='file')
    
    def process_json_files(self, process_json_callback):
        """
        Processes all the JSON files in the folder specified in `folder_path`.
        Opens each file with a ".json" extension, reads its contents, and passes the data to `process_json_callback`.
        If the folder does not exist, logs an error message.
        If there is an error while reading a file, logs an error message.

        Args:
            process_json_callback (function): The function to process the data from each JSON file.
        """

        if not os.path.exists(self.folder_path):
            self.error_handler.log_error(f"The folder path {self.folder_path} does not exist")
            return
        for file_name in sorted(os.listdir(self.folder_path)):
            if file_name.endswith(".json"):
                file_path = os.path.join(self.folder_path, file_name)
                try:
                    with open(file_path, "r") as f:
                        data = pd.read_json(file_path)
                        process_json_callback(data)
                except Exception as e:
                    self.error_handler.log_error(f"An error occurred while reading file {file_name}: {str(e)}")

    def process_json_callback(self, data):
        """
        A callback function that processes the data from one JSON file and appends the processed data to the `results` list of the JSONProcessor instance.

        Args:
            data (dict): The data from a JSON file.
        """

        match_results = data['d']['rows']
        match_results.reverse()
        for i, result in enumerate(match_results):
            if result['result'] == 'postp.':
                self.logger.info(f"Game between {result['home-name']} and {result['away-name']} was postponed")
                continue # Skip this game as it is postponed
            else:
                if 'result' not in result.keys():
                    self.logger.warning(f"Game between {result['home-name']} and {result['away-name']} is missing the result key")
                    continue # make sure the item has a results key
            try:
                self.results.append({
                    'home-name': result['home-name'],
                    'home-name': result['home-name'],
                    'away-name': result['away-name'],
                    'home-result': result['homeResult'],
                    'away-result': result['awayResult'],
                    'home-win': True if result['home-winner'] == 'win' else False,
                    'away-win': True if result['away-winner'] == 'win' else False,
                    'home-odds-avg': round(result['odds'][0]['avgOdds'] - 1,2),
                    'home-odds-max': round(result['odds'][0]['maxOdds'] - 1,2),
                    'draw-odds-avg': round(result['odds'][1]['avgOdds'] - 1,2),
                    'draw-odds-max': round(result['odds'][1]['maxOdds'] - 1,2),
                    'away-odds-avg': round(result['odds'][2]['avgOdds'] - 1,2),
                    'away-odds-max': round(result['odds'][2]['maxOdds'] - 1,2),
                    'date-start-timestamp': result['date-start-timestamp']
                })
            except KeyError as e:
                self.error_handler.log_error(f"An error occurred while processing game {i}: {str(e)}")
   
    def save_to_csv(self):
        """
        Saves the processed data stored in the `results` list of the JSONProcessor instance to a CSV file.
        The name of the file is specified by the `csv_file` attribute of the JSONProcessor instance.
        """

        if not self.results:
            self.error_handler.log_error("No results to save to CSV file")
            return
        try:
            df = pd.DataFrame(self.results)
            df.to_csv(self.csv_file, index=False)
            self.logger.info(f'Elo ratings for matches in the 19-20 season have been calculated and saved to {self.csv_file}')
        except IOError as e:
            self.error_handler.log_error(f"An error occurred while creating the CSV file: {str(e)}")

    def generate_match_results_csv(self):
        self.process_json_files(self.process_json_callback)
        self.save_to_csv()
        