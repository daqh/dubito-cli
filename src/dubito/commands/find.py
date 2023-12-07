from dubito.database import db
import csv
from sys import stdout

def find(sql: str) -> None:
    '''
    Find a query in the database.

    Args:
        sql (str): The query to search.
    '''
    cursor = db.execute_sql(sql)
    headers = [desc[0] for desc in cursor.description]

    writer = csv.writer(stdout)
    writer.writerow(headers)
    for row in cursor:
        writer.writerow(row)
