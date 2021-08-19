import csv
import sqlite3

connection = sqlite3.connect('TestDB.db')
cursor = connection.cursor()
file = open('/home/milesproject2021/coding/Words2.csv')
contents = csv.reader(file)
insert_records = "INSERT INTO WORDS (Keywords, True_Meaning, False_Meaning, Related_words, Start_word) VALUES(?, ?, ?, ?, ?)"
cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM WORDS"
rows = cursor.execute(select_all).fetchall()
for r in rows:
    print(r)
connection.commit()
connection.close()
