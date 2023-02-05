from dotenv import load_dotenv
from .connection import DBConnector
from .queries import ExecuteQuery

load_dotenv()

class Database:
    def __init__(self):
        self.conn = DBConnector().connect()
        self.execute_query = ExecuteQuery(self.conn)

    def close(self):
        self.conn.close()
