from sqlite3 import connect, Row
from DotDict import DotDict
from typing import List
import config

# SQLite3 connection
conn = connect(config.load().pathes.db)
conn.row_factory = Row
cursor = conn.cursor()

def get(request, *args) -> List[DotDict]:
    """
    Return Something from database
    """

    ## Get sqlite3.Row objects (there are in a list) and
    ## mapped they to DotDict object
    sql = cursor.execute(request, args)
    sql = sql.fetchall()
    sql = [DotDict(dict(zip(i.keys(), tuple(i)))) for i in sql]

    return sql

def post(request, *args):
    """
    Update and save data in database
    """
    cursor.execute(request, args)
    conn.commit()
