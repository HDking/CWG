# sql.py - create a SQLite3 table and populate it with data

import sqlite3
import datetime

date = datetime.datetime.utcnow()

# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:
    
    c = connection.cursor()
    c.execute("""CREATE TABLE posts (task_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, post TEXT NOT NULL,summary TEXT NOT NULL ,posted_date DATE, published INTEGER)""")
    
    c.execute('INSERT INTO posts (title, post, summary, posted_date ,published)' 'VALUES("Good", "Im good", "test summary" , "%s", 0)' %date)