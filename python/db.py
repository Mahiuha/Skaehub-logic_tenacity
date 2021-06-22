#importing the SQLite module

import sqlite3

#this line of code prints the sqlite version.

print("sqlite version" + " " + sqlite3.sqlite_version)

#the line of code below creates a database and connects to that database

conn = sqlite3.connect(database.db)
c = conn.cursor()
