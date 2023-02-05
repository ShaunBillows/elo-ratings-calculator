import pandas as pd

class CSVReader:
    """
    Class for handling the reading of CSV files.

    Attributes:
        None

    Methods:
        read_csv(csv_file: str) -> Dict[str, Union[str, pd.DataFrame]]:
            Reads a CSV file and returns a dictionary with 'data' key containing the Pandas DataFrame 
            or 'error' key containing the error message.

    Raises:
        None
    """
    def __init__(self):
        pass

    def read_csv(self, csv_file):
        if not isinstance(csv_file, str):
            return {'error': f'Error: {csv_file} is not a string'}
        if not csv_file.endswith('.csv'):
            return {'error': f'Error: {csv_file} is not a .csv file'}
        
        try:
            df = pd.read_csv(csv_file, na_values=["N/A", "-", "?"])
            return {'data': df}
        except FileNotFoundError:
            return {'error': f'Error: The file {csv_file} could not be found'}
        except Exception as e:
            return {'error': f'Error: An error occurred while reading the file: {e}'}

