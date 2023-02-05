import pandas as pd

class CSVHandler:
    """
    A class to handle reading and writing of CSV files.
    
    Methods:
        - read_csv(csv_file)
            Reads a CSV file and returns a dictionary with 'data' key containing the Pandas DataFrame 
            or 'error' key containing the error message.
        - write_csv(df, output_file)
            Writes the Pandas DataFrame to a CSV file and returns a dictionary with 'message' key containing 
            success message or 'error' key containing the error message.
    """
    def __init__(self):
        """
        Initialise the CSVHandler class.
        """
        pass

    def read_csv(self, csv_file):
        """
        Reads a CSV file and returns a dictionary with 'data' key containing the Pandas DataFrame
        or 'error' key containing the error message.
        
        Args:
            - csv_file (str): The name of the CSV file to be read, including the path.
        
        Returns:
            - dict: A dictionary with 'data' key containing the Pandas DataFrame or 'error' key 
                  containing the error message.
        """
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

    def write_csv(self, df, output_file):
        """
        Writes the Pandas DataFrame to a CSV file and returns a dictionary with 'message' key 
        containing success message or 'error' key containing the error message.
        
        Args:
            - df (pandas.DataFrame): The Pandas DataFrame to be written to a CSV file.
            output_file (str): The name of the CSV file to be written, including the path.
        
        Returns:
            - dict: A dictionary with 'message' key containing success message or 'error' key 
            containing the error message.
        """
        if not isinstance(df, pd.DataFrame) or df.empty:
            return {'error': 'Error: No data in the dataframe to save.'}
        if not output_file.endswith('.csv'):
            return {'error': f'Error: The output file {output_file} is not a .csv file'}
        try:
            df.to_csv(output_file, index=False)
            return {'message': f'Data saved to {output_file}'}
        except IOError:
            return {'error': f'Error: The directory specified in {output_file} does not exist. Please specify a valid directory.'}
