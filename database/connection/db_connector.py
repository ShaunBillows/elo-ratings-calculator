import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class DBConnector:
    """
    A class for connecting to a PostgreSQL database using the psycopg2 library. 
    The connection details are stored in environment variables.
    """
    def __init__(self):
        """
        Initialises the connection attribute to None.
        """
        self.connection = None

    def connect(self):
        """
        Connects to the database using the connection details stored in environment variables. 
        If the connection attribute is not None, the existing connection is returned.
        
        Returns:
            psycopg2 connection object.
        """
        if self.connection:
            return self.connection

        try:
            self.connection = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )
            print("Successfully connected to the database.")
        except Exception as e:
            print(f"Error connecting to the database: Details: {e}")
        return self.connection

    def close(self):
        """
        Closes the connection to the database, if the connection attribute is not None.
        """
        if self.connection:
            self.connection.close()
            print("Successfully closed the connection to the database.")
