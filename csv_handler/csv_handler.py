import pandas as pd
from .csv_io import CSVReader
from .csv_io import CSVWriter

class CSVHandler:
    """
    Class for handling reading and writing of CSV files.

    Attributes:
        read_csv_handler (CSVReadHandler): Object for handling the reading of CSV files.
        write_csv_handler (CSVWriteHandler): Object for handling the writing of Pandas DataFrames to CSV files.

    Methods:
        read_csv(csv_file: str) -> Dict[str, Union[str, pd.DataFrame]]:
            Reads a CSV file and returns a dictionary with 'data' key containing the Pandas DataFrame 
            or 'error' key containing the error message.
        write_csv(df: pd.DataFrame, output_file: str) -> Dict[str, str]:
            Writes the Pandas DataFrame to a CSV file and returns a dictionary with 'message' key 
            containing success message or 'error' key containing the error message.

    Raises:
        None
    """
    def __init__(self):
        self.read_csv_handler = CSVReader()
        self.write_csv_handler = CSVWriter()

    def read_csv(self, csv_file):
        return self.read_csv_handler.read_csv(csv_file)

    def write_csv(self, df, output_file):
        return self.write_csv_handler.write_csv(df, output_file)
