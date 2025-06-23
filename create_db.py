import sqlite3 as sql

conn=sql.connect('db_web.db')
cursor=conn.cursor()
cursor.execute("drop table if exists users")
sql=''' create table 'users'(
'uid'integer primary key autoincrement,
'uname' text,
'contact' text
 )'''
cursor.execute(sql)
conn.commit()
conn.close()

