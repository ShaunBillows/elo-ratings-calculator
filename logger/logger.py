import logging

class Logger:
    """
    This class provides a centralised and customisable logging solution for the application.

    The purpose of the Logger class is to provide a way to log messages in a consistent and standardised way throughout the application. This class uses the Python `logging` module and implements a singleton pattern to ensure that there is only one instance of the logger throughout the entire application.  If multiple instances are requested, the __new__ method is used to ensure that only one instance is created, and all subsequent attempts to create an instance will return the existing instance.
    
    The Logger class also provides an interface to log messages to a log file as well as to the console.  This can be controlled by setting the `level` parameter while instantiating the logger. By default, the log level is set to `logging.DEBUG` and the log messages will be written to the file `application.log`. The log messages can also be written to the console if the level of the message is at least 
    `logging.WARNING`.

    The log messages have a standard format which includes the following information:
     - Timestamp (`asctime`)
     - Logger name (`name`)
     - Log level (`levelname`)
     - The actual message (`message`)
    
    Attributes:
    - log_file (str): The name of the log file to write log messages to.
    - level (int): The level of log messages to log. Defaults to `logging.DEBUG`.
    - logger (logging.Logger): The logger instance.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, log_file='application.log', level=logging.DEBUG):
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(level)

            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
