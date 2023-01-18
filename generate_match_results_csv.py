"""
This script processes all the JSON files in a given folder containing raw match result data, and converts the data into a CSV file in a format suitable for generating Elo ratings. The processed data includes information such as the home and away team names, scores, and odds from a range of bookmakers. The resulting CSV file can then be used as input for generating Elo ratings of teams in a given league or season, and the bookmakers odds can be used to test and optimise the algorithm to create a (hopefully successful) betting system.

Args:
folder_path (str): The path to the folder containing the JSON files.
callback_func (function): The function to process the data from each JSON file.

"""
import os
import pandas as pd

def process_json_files(folder_path, callback_func):
    """
    Iterates through all the JSON files in a given folder and calls a callback function to process the data.
    Args:
        folder_path (str): The path to the folder containing the JSON files.
        callback_func (function): The function to process the data from each JSON file.
    """
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as f:
                data = pd.read_json(file_path)
                callback_func(data)

def callback_func(data):
    """
    A callback function that processes the data from each JSON file and appends the results to a list.
    The data is then used to create a CSV file
    Args:
    data (dict): The data from each JSON file.
    """
    match_results = data['d']['rows']
    for result in match_results:
        results.append({
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
        })

def save_to_csv(data, file_name):
    """
    Saves the processed data to a CSV file.
    Args:
    data (list): The processed data.
    file_name (str): The name of the CSV file to be created.
    """
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)

results = []
process_json_files("./raw-data/19-20", callback_func)
save_to_csv(results, './processed-data/19-20.csv')
