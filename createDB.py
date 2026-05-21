import sqlite3
conn = sqlite3.connect('christopher.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE users(
               id text,
               username text,
               password text
               );
               """)

cursor.execute("""
               CREATE TABLE projects(
               id text,
               title text,
               body text
               );
               """)

cursor.execute("""
               INSERT INTO users VALUES ('admin', 'admin', '#1Geheim!')
               """)

conn.commit()
conn.close()