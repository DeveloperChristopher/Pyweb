import sqlite3

conn = sqlite3.connect('./christopher.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE `users` ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'username' text, 'password' text);")
cursor.execute("CREATE TABLE `projects`('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'title' text, 'body' text);")
cursor.execute("INSERT INTO `users` ('username', 'password') VALUES ('admin', '#1Geheim!');")
cursor.execute("INSERT INTO `projects` ('title', 'body') VALUES ('BPYWEB', 'Het maken van een portfolio website.');")

conn.commit()
conn.close()