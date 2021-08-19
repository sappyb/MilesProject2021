import csv
import sqlite3

connection = sqlite3.connect('TestDB.db')

cursor = connection.cursor()


select_all = "SELECT * FROM WORDS"

rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

connection.commit()

connection.close()
