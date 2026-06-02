from db import Database

class Project(Database):
    def __init__(self):
        super().__init__()

    def create(self, title, body):
        return super().create("projects", ["title", "body"], [title, body])

    def read_all(self):
        return super().read("projects")

    def read_id(self, id):
        return super().read("projects", f"WHERE `id` = {id}")

    # def update(self):
    #     pass

    # def delete(self):
    #     pass
