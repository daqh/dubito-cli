from dubito.database import db
import csv
from sys import stdout
import logging

def find(sql: str) -> None:
    '''
    Find a query in the database.

    Args:
        sql (str): The query to search.
    '''
    logging.debug(f"Executing query: {sql}")
    cursor = db.execute_sql(sql)
    logging.debug("Query executed successfully")

    headers = [desc[0] for desc in cursor.description]

    writer = csv.writer(stdout)
    writer.writerow(headers)
    for row in cursor:
        writer.writerow(row)
