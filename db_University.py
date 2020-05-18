# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:55:40 2020

@author: user
"""

"""

Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""




import sqlite3
from pandas import DataFrame

conn = sqlite3.connect("db_University.db")

c = conn.cursor()

#c.execute("DROP TABLE employees")
conn.commit()

c.execute("""CREATE TABLE student(
        name TEXT,
        age INTEGER,
        roll_no INTEGER,
        branch TEXT
        )"""
        )
#conn.commit()

c.execute("insert into student values('Ram','15','101','computer science')")             #student 1
c.execute("insert into student values('Mohan','18','102','computer science')")           #student 2
c.execute("insert into student values('Ganesh','17','103','computer science')")          #student 3
c.execute("insert into student values('Diksha','16','104','computer science')")          #student 4
c.execute("insert into student values('Dinesh','18','105','computer science')")           #student 5
c.execute("insert into student values('Shivansh','17','106','computer science')")          #student 6
c.execute("insert into student values('Akanksha','15','107','computer science')")          #student 7
c.execute("insert into student values('Mahesh','15','108','computer science')")           #student 8
c.execute("insert into student values('Preeti','17','109','computer science')")           #student 9
c.execute("insert into student values('Pooja','15','110','computer science')")           #student 10

#conn.commit()

c.execute("select*from student")

df = DataFrame(c.fetchall())
df.columns = ["name","age","roll_no","branch"]
df.to_csv('db_University.csv')

# for closing of data base
conn.close()
