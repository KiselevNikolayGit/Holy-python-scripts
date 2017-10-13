"""
Database record class for manage data
Sqlite3 using in python3
By Kiselev Nikolay with love
"""


from database import Database


class Record (Database):
    """
    no dis yet. sorry.
    """

    table_name = ""
    __database = ""

    def __init__(self):
        super(Record, self).__init__()
        print("NOW: record is init")

aaa = Record()
