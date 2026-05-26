from db import Database

class User(Database):
    def __init__(self):
        super().__init__()

    # def create(self, id, title, body):
    #     self.cursor.execute(f"INSERT INTO projects VALUES ('{id}', '{title}', '{body}')")
    #     self.conn.commit()

    def read_all(self):
        return super().read("users")

    def read_username(self, username):
        return super().read("users", f"WHERE `username` = '{username}'")

    # def update(self):
    #     pass

    # def delete(self):
    #     pass
