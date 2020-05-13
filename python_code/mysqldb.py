# -*- coding:utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password")
# print(mydb)
mycursor = mydb.cursor(buffered=True)

mycursor.execute("SHOW DATABASES")
'''
print(mycursor)
for d in mycursor:
    print(d)
'''
mycursor.execute("USE test")

mycursor.execute("SHOW TABLES")
for t in mycursor:
    print(t)
mycursor.execute("DESC classes")
for d in mycursor:
    print(d)
mycursor.execute("SELECT * FROM classes")
for c in mycursor:
    print("classid:%s, name:%s" % c)
'''
sql_insect = "INSERT INTO classes (name) VALUES (%s)"
var = ("6ban",)
mycursor.execute(sql_insect,var)
mydb.commit()
'''
'''
sql_delete = "DELETE FROM classes WHERE name = %s"
var_d = ("5ban",)
mycursor.execute(sql_delete, var_d)
mydb.commit()
'''
'''
sql_update = "UPDATE classes SET name = %s WHERE id=%s"
var_u = ("六班", 6)
mycursor.execute(sql_update, var_u)
mydb.commit()
'''
mycursor.execute("SELECT * FROM classes LIMIT 3")
for c in mycursor:
    print("classid:%s, name:%s" % c)
