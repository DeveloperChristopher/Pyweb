from db import Database

class Project(Database):
    def __init__(self):
        super().__init__()

    def create(self, title, body, img_type):
        return super().create("projects", ["title", "body", "img_type"], [title, body, img_type])

    def read_all(self):
        return super().read("projects")

    def read_id(self, id):
        return super().read("projects", f"WHERE `id` = {id}")

    def update(self, id, column, values):
        return super().update("projects", column, values, f"WHERE `id` = {id}")

    def delete_id(self, id):
        return super().delete("projects", f"WHERE `id` = {id}")
