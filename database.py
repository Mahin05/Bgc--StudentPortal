import sqlite3
con=sqlite3.connect('1728094.db')
cur=con.cursor()
# cur.execute("CREATE TABLE admin(ID INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT NOT NULL,Email EMAIL NOT NULL,Password TEXT NOT NULL)")
cur.execute("CREATE TABLE cse1728094(Serial INTEGER PRIMARY KEY,RegNumber VARCHAR(30) NOT NULL,CourseName VARCHAR(50) NOT NULL,Payment VARCHAR(30) NOT NULL)")
con.close()