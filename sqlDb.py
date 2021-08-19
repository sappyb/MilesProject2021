import sqlite3
conn = sqlite3.connect('TestDB.db')
c = conn.cursor()
c.execute('''CREATE TABLE WORDS
        ([generated_id] INTEGER PRIMARY KEY,[Keywords] text, [True_Meaning] text, [False_Meaning] text, [Related_words] text, [Start_word] text)''')

c.execute('''CREATE TABLE WORD_HISTORY
             ([Word] text, [Date] date)''')

conn.commit()
