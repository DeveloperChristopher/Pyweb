from db import Database

class Project(Database):
    def __init__(self):
        super().__init__()

    def create(self, id, title, body):
        self.cursor.execute(f"INSERT INTO projects VALUES ('{id}', '{title}', '{body}')")
        self.conn.commit()

    def read_all(self):
        self.cursor.execute(f"SELECT * FROM `projects`")
        self.conn.commit()
        data = self.cursor.fetchall()
        return data

    def read_id(self, id):
        self.cursor.execute(f"SELECT * FROM projects WHERE id={id}")
        self.conn.commit()

    def update(self):
        pass

    def delete(self):
        pass

if __name__ == "__main__":
    project = Project()
    print(project.read_all())