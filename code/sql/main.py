import sqlite3
import re

# SQLite3 connection
conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()

def get(request, *args):
    """
    Return Something from database
    """

    cursor.execute(request, args)
    sql = cursor.fetchall()

    # Find requests keys
    req_keys = re.sub(r'\t+', '', request)
    req_keys = re.sub(r'\n+', '', req_keys)
    req_keys = re.sub(r' +', '', req_keys)
    req_keys = req_keys[6:].split('FROM')[0]
    req_keys = req_keys.split(',')

    return [dict(zip(req_keys, i)) for i in sql]

def post(request, *args):
    """
    Update and save data in database
    """
    cursor.execute(request, args)
    conn.commit()
