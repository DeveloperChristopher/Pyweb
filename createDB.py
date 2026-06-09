import sqlite3

conn = sqlite3.connect('./christopher.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE `users` ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'username' text, 'password' text);")
cursor.execute("CREATE TABLE `projects`('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'title' text, 'body' text, img_type text);")
cursor.execute("INSERT INTO `users` ('username', 'password') VALUES ('admin', '#1Geheim!');")

conn.commit()
conn.close()