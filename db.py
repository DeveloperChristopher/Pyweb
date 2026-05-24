import sqlite3

class Database:
    def __init__(self):
        self.db = sqlite3.connect('./christopher.db')
        self.cursor = self.db.cursor()

    # def create(self, table, where = "WHERE 1"):
    #     self.db.cursor.execute(f"SELECT * FROM {table} {where}")

    def read(self, table, where = "WHERE 1"):
        self.cursor.execute(f"SELECT * FROM `{table}` {where}")
        return self.cursor.fetchall()

    # def update():
    #     pass

    # def delete():
    #     pass