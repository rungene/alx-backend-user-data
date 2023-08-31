#!/usr/bin/env python3
"""
filtered_logger
"""
from typing import List
import re
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Replaces occurences of of certain field values

    Args:
        fields: list of strings representing all fields to obfuscate
        redaction: string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: string separator for fields in message

    Return:
        a copy of message with some field values replaced
    """
    for field in fields:
        message = re.sub(field + '=.*?' + separator,
                         field + '=' + redaction + separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialise """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum"""
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Takes no args returns a logging.Logger object.
    """
    logger_name = 'user_data'
    log_level = logging.INFO
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    logger.setpropagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)

    return logger
