# sql.py - create a SQLite3 table and populate it with data

import sqlite3
import datetime

date = datetime.datetime.utcnow()

# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE posts (task_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, reporter TEXT NOT NULL, post TEXT NOT NULL,summary TEXT NOT NULL ,posted_date DATE, published INTEGER)""")
    # c.execute('INSERT INTO posts (title,reporter, post, summary, posted_date ,published)' 'VALUES("Good", "James", "Im good", "test summary" , "%s", 0)' %date)

#Crisis Messages
with sqlite3.connect("messages.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE messages (message_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, message TEXT NOT NULL, type INTEGER, posted_date DATE, team INTEGER)""")
    # c.execute('INSERT INTO messages (title, message, type, posted_date, team)' 'VALUES("Good", "Im good", 0 , "%s", 1)' %date)
    
#Crisis Messages
with sqlite3.connect("crisis_messages.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE crisis_messages (message_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, message TEXT NOT NULL, type INTEGER, posted_date DATE, team INTEGER)""")
    # c.execute('INSERT INTO crisis_messages (title, message, type, posted_date, team)' 'VALUES("Good", "Im good", 0 , "%s", 1)' %date)