import sys
import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

# sql injection
sql = "select * from test where name like '%%%s%%'" % sys.argv[1]
cur.execute(sql)
 
con.close()