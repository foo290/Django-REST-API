import json
import sqlite3
import os

database_file = os.path.join(os.getcwd() + r'\database\user_info\userinfo.db')


class UserServer:

    def __init__(self):
        pass

    def get_users(self):
        """ Users api end point response """
        try:
            connection = sqlite3.connect(database_file)
            cur = connection.cursor()
            raw = cur.execute(f'select name from students limit 5')
            data = raw.fetchall()
            data_list = [name[0] for name in data]
            data_list.append('more...')

            return data_list
        except Exception as error:
            return 'data not found'

    def get_user_data(self, userid):
        """ returns detailed information of individual request """
        try:
            connection = sqlite3.connect(database_file)
            cur = connection.cursor()
            cols = cur.execute("PRAGMA table_info(students)")
            col_fetch = cols.fetchall()
            col_list = [col[1] for col in col_fetch]

            raw = cur.execute(f'select * from students where roll_no="{userid}" ')
            data = raw.fetchall()[0]
            structured_data = {col: detail for col, detail in zip(col_list, data)}

            return structured_data
        except Exception as error:
            return 'data not found'
