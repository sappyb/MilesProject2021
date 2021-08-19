import csv
import sqlite3

connection = sqlite3.connect('TestDB.db')

cursor = connection.cursor()
file = open('/home/milesproject2021/coding/Date.csv')

contents = csv.reader(file)
insert_records = "INSERT INTO WORD_HISTORY (Word, Date) VALUES(?, ?)"

cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM WORD_HISTORY"

rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

connection.commit()

connection.close()
