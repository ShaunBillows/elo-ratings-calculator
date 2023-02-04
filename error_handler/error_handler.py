from logger import Logger

class ErrorHandler:
    """
    The ErrorHandler class logs error messages to a specified log destination.

    Attributes:
        log_destination (str): The log destination for error messages, options are 'file', 'database', 'both'
        logger (Logger object): An instance of the Logger class.

    Methods:
        log_error(message): Logs an error message to the specified log destination.
    """

    def __init__(self, log_destination='file'):
        self.log_destination = log_destination
        self.logger = Logger().logger

    def log_error(self, message):
        if self.log_destination == 'file':
            self.logger.error(message)
        elif self.log_destination == 'database':
            # code to log to database
            pass
        elif self.log_destination == 'both':
            self.logger.error(message)
            # code to log to database
        else:
            self.logger.error("Invalid log destination. Choose 'file', 'database', or 'both'.")

