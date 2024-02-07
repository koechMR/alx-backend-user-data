#!/usr/bin/env python3
"""
Main file
"""
import re
from typing import List
import logging
import os

patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(patterns['extract']([field], separator), patterns['replace'](redaction), message)
    return message

def main():
    """
    Main function
    """
    db_user = os.getenv('PERSONAL_DATA_DB_USERNAME')
    db_pwd = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    cnx = mysql.connector.connect(user=db_user, password=db_pwd, host=db_host, database=db_name)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor:
        print(row)
    cursor.close()
    cnx.close()
    
if __name__ == '__main__':
   main()