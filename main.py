import sqlite3

connection = sqlite3.connect("baseball.db")
cursor = connection.cursor()

testing = cursor.execute("SELECT LNAME FROM Pirates").fetchall()
print(testing)