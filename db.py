import sqlite3

class Database:
    def __init__(self):
        self.db = sqlite3.connect('./christopher.db')
        self.cursor = self.db.cursor()

    # deze functie is geschreven met behulp van AI
    def create(self, table, columns, values):
        column_data = ", ".join(columns)
        value_data = ", ".join(f'"{value}"' for value in values)
        self.cursor.execute(f"INSERT INTO `{table}` ({column_data}) VALUES ({value_data});")
        self.db.commit()
        return self.cursor.lastrowid 

    def read(self, table, where = "WHERE 1"):
        self.cursor.execute(f"SELECT * FROM `{table}` {where};")
        return self.cursor.fetchall()

    # deze functie is geschreven met AI
    def update(self, table, columns, values, where):
        set_clause = ", ".join(f"`{col}` = ?" for col in columns)
        query = f"UPDATE `{table}` SET {set_clause} {where}"
        self.cursor.execute(query, values)
        self.db.commit()

    def delete(self, table, where):
        self.cursor.execute(f"DELETE FROM `{table}` {where};")
        self.db.commit()