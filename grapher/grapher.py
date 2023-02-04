from .plots import plot_elo_bookies_scatter
from logger import Logger
import pandas as pd

class Grapher:
    """
    The Grapher class provides an interface to access and visualise data.

    Attributes:
        - dataframe (pd.DataFrame): The processed data.
        - logger (Logger object): Handles logging messages.

    Methods:
        - get_data_from_sql(database, query): Fetches data from a database using a query.
        - get_data_from_csv(csv_file): Loads data from a CSV file.
        - plot_elo_bookies_scatter(csv_file=None, output_file=None, title=None, show=False): Generates a scatter plot of Elo ratings vs bookmaker odds.
    """
    def __init__(self):
        self.dataframe = []
        self.logger = Logger().logger

    def get_data_from_sql(self, database, query):
        # TODO
        return

    def get_data_from_csv(self, csv_file):
        if not csv_file.endswith('.csv'):
            self.logger.error(f'{csv_file} is not a .csv file')
            return

        try:
            df = pd.read_csv(csv_file, na_values=["N/A", "-", "?"])
            self.dataframe = df
        except FileNotFoundError:
            self.logger.error(f'The file {csv_file} could not be found')
        except Exception as e:
            self.logger.error(f'An error occurred while reading the file: {e}')

    def plot_elo_bookies_scatter(self, csv_file=None, output_file=None, title=None, show=False):
        """
        This method generates a scatter plot of Elo ratings versus bookmakers' odds for a given data source. The data source can be provided as a csv file, or through the get_data_from_csv method. The scatter plot shows the relationship between the Elo ratings and bookmakers' odds, which can be used to evaluate the accuracy of the Elo ratings as a predictor of match outcomes.
        
        Args:
            - csv_file (str, optional): The path to the csv file to be used as the data source. If not provided, the data source should have been set through `get_data_from_csv` method.
            - output_file (str, optional): The path and file name to save the generated scatter plot as an image file. If not provided, the scatter plot will not be saved.
            - title (str, optional): The title for the scatter plot. If not provided, a default title will be used.
            - show (bool, optional): A flag indicating whether to show the scatter plot. Default value is False.
            
        Raises:
            Exception: Raises an error if the data source is not provided or an error occurs while plotting the data. The error message is logged by the logger class.
        """
        if not isinstance(self.dataframe, pd.DataFrame) or self.dataframe.empty:
            self.logger.error("No data to plot. Please provide the data source through csv_file argument or call get_data_from_csv method.")
            return
        try:
            plot_elo_bookies_scatter(dataframe=self.dataframe, output_file=output_file, title=title, show=show)
        except Exception as e:
            self.logger.error(f'An error occurred while plotting the data: {str(e)}')
