import pandas as pd

class CSVWriter:
    """
    Class for handling the writing of Pandas DataFrames to CSV files.

    Attributes:
        None

    Methods:
        write_csv(df: pd.DataFrame, output_file: str) -> Dict[str, str]:
            Writes the Pandas DataFrame to a CSV file and returns a dictionary with 'message' key 
            containing success message or 'error' key containing the error message.

    Raises:
        None
    """
    
    def __init__(self):
        pass

    def write_csv(self, df, output_file):
        if not isinstance(df, pd.DataFrame) or df.empty:
            return {'error': 'Error: No data in the dataframe to save.'}
        if not output_file.endswith('.csv'):
            return {'error': f'Error: The output file {output_file} is not a .csv file'}
        try:
            df.to_csv(output_file, index=False)
            return {'message': f'Data saved to {output_file}'}
        except IOError:
            return {'error': f'Error: The directory specified in {output_file} does not exist. Please specify a valid directory.'}
