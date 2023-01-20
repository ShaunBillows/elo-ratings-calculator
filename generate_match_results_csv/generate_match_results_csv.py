"""
This script processes all the JSON files in a given folder containing raw match result data, and converts the data into a CSV file in a format suitable for generating Elo ratings. The processed data includes information such as the home and away team names, scores, and odds from a range of bookmakers. The resulting CSV file can then be used as input for generating Elo ratings of teams in a given league or season, and the bookmakers odds can be used to test and optimise the algorithm to create a (hopefully successful) betting system.

Args:
folder_path (str): The path to the folder containing the JSON files.
process_json_callback (function): The function to process the data from each JSON file.

"""
import os
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO) # not can delete when moving func to main.py

def process_json_files(folder_path, process_json_callback):
    """
    Iterates through all the JSON files in a given folder and calls a callback function to process the data.
    Args:
        folder_path (str): The path to the folder containing the JSON files.
        process_json_callback (function): The function to process the data from each JSON file.
    """
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            try:
                with open(file_path, "r") as f:
                    data = pd.read_json(file_path)
                    process_json_callback(data)
            except Exception as e:
                logging.error(f"An error occurred while reading file {file_name}: {str(e)}")

def process_json_callback(data):
    """
    A callback function that processes the data from each JSON file and appends the results to a list.
    The data is then used to create a CSV file
    Args:
    data (dict): The data from each JSON file.
    """
    match_results = data['d']['rows']
    match_results.reverse()
    for i, result in enumerate(match_results):
        if result['result'] == 'postp.':
            logging.info(f"Game between {result['home-name']} and {result['away-name']} was postponed")
            continue # Skip this game as it is postponed
        else:
            if 'result' not in result.keys():
                logging.warning(f"Game between {result['home-name']} and {result['away-name']} is missing the result key")
                continue # make sure the item has a results key
        try:
            results.append({
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
            logging.error(f"An error occurred while processing game {i}: {str(e)}")

def save_to_csv(data, file_name):
    """
    Saves the processed data to a CSV file.
    Args:
    data (list): The processed data.
    file_name (str): The name of the CSV file to be created.
    """
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
    except IOError as e:
        logging.error(f"An error occurred while creating the CSV file: {str(e)}")


# def generate_match_results_csv(folder_path, csv_file):
#     results = []
#     process_json_files(folder_path, process_json_callback)
#     save_to_csv(results, csv_file)

# # 19-20
# results = []
# process_json_files("./raw-data/19-20", process_json_callback)
# save_to_csv(results, './processed-data/19-20.csv')


# # 20-21
# results = []
# process_json_files("./raw-data/20-21", process_json_callback)
# save_to_csv(results, './processed-data/20-21.csv')

# # 21-22
# results = []
# process_json_files("./raw-data/21-22", process_json_callback)
# save_to_csv(results, './processed-data/21-22.csv')

# 22-23
# results = []
# process_json_files("./raw-data/22-23", process_json_callback)
# save_to_csv(results, './processed-data/22-23.csv')