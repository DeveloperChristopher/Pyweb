import sqlite3

class Database:
    def __init__(self):
        self.db = sqlite3.connect('./christopher.db')
        self.cursor = self.db.cursor()

    # deze functie is geschreven met behulp van AI
    def create(self, table, columns, values):
        column_data = ", ".join(columns)
        value_data = ", ".join(f"'{value}'" for value in values)
        self.cursor.execute(f"INSERT INTO `{table}` ({column_data}) VALUES ({value_data});")
        # return self.cursor.lastrowid needs some work

    def read(self, table, where = "WHERE 1"):
        self.cursor.execute(f"SELECT * FROM `{table}` {where};")
        return self.cursor.fetchall()

    # def update():
    #     pass

    # def delete():
    #     pass