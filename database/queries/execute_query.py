import psycopg2
from psycopg2 import sql

class ExecuteQuery:
    """Class for executing database queries.
    
    This class provides a convenient way to execute SQL queries on the database. The query is executed using an active
    connection and the results are automatically committed. 
    
    Args:
        connection (psycopg2.extensions.connection): An active database connection.
    """
    def __init__(self, connection):
        """
        Initialises the ExecuteQuery class with an active database connection.
        
        Args:
            connection (psycopg2.extensions.connection): An active database connection.
        """
        self.connection = connection

    def execute_query(self, query, params=None):
        """Execute a query on the database.
        
        This method executes a provided SQL query on the database using an active connection. If a list of parameters
        is provided, they will be passed to the query. The results of the query are automatically committed.
        
        Args:
            query (str): The SQL query to be executed.
            params (list, optional): A list of parameters to be passed to the query. Defaults to None.
        """
        with self.connection.cursor() as cursor:
            if params:
                cursor.execute(sql.SQL(query), params)
            else:
                cursor.execute(sql.SQL(query))
        self.connection.commit()
