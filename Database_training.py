# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:46:49 2020

@author: user
"""


#https://www.db4free.net/phpMyAdmin/
#import the library
import mysql.connector

#for making the connection we need connect()
conn = mysql.connector.connect(user='forsk_root',password='cooler2112',host='db4free.net',database='forsk_test')

#cursor can work for multiple tables 
c = conn.cursor()

#show to databases name in out database
c.execute("show databases")  

#show to tables name in out database
c.execute("SHOW TABLES")

for x in c:  
    print(x)  
    
    
#create a table 
c.execute("CREATE TABLE consumer(name VARCHAR(255), roll_no INT, Batch TEXT)")

#if want add new column in our data
c.execute("ALTER TABLE consumer ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



conn.commit()
#data insertion in our table
sql = "INSERT INTO consumer (name,roll_no,Batch) VALUES (%s,%s,%s)"
val = [('john',12,'cse'),('jonson',13,'cse'),('jame',15,'cse')]

c.executemany(sql,val)
conn.commit()



--------------------------------------------------------------------


#to select from database
c.execute("SELECT * FROM consumer")
myresult = c.fetchall()
for x in myresult:
    print(x)

------------------------------------------------------------------
#some column selection    
c.execute("SELECT Batch,name FROM consumer")
myresult = c.fetchall()
for x in myresult:
    print(x)
  ------------------------------------------------------------------  
    
#When selecting records from a table, you can filter 
#the selection by using the "WHERE" statement:
specific_line = c.execute("SELECT * FROM consumer WHERE name = 'jonson'")
c.execute(specific_line)
myresult = c.fetchall()
for x in myresult:
    print(x)
    
------------------------------------------------------------------

#Wildcard Characters

choose = c.execute("SELECT * FROM consumer WHERE name LIKE '%o%'")
c.execute(choose)
myresult = c.fetchall()
for x in myresult:
    print(x)

------------------------------------------------------------------

#Prevent SQL Injection
#When SQL query are provided by user then you should to escape the values

sql = "SELECT * FROM consumer WHERE name = %s"
add = ("jame",)
c.execute(sql,add)
myresult = c.fetchall()
for x in myresult:
    print(x)
 
conn.commit()



------------------------------------------------------------------


 #Sort the Result   
    
try:  
  
    sql = "SELECT * FROM consumer ORDER BY name"
    c.execute(sql)
    myresult = c.fetchall()
    for x in myresult:
        print(x) 
      
except:  
    conn.rollback()     
    

------------------------------------------------------------------
    
#Sort the values Order by name using DESC   
try:  
  
    sql = "SELECT * FROM consumer ORDER BY name DESC"
    c.execute(sql)
    #fetching the rows from the cursor object 
    myresult = c.fetchall()
    #printing the result
    for x in myresult:
        print(x)
          
except:  
    conn.rollback()
    print("Please Recheck your code")
    
   
------------------------------------------------------------------
  
#Delete a row  
try:  
  
    sql = "DELETE FROM consumer WHERE name = 'jame'"
    c.execute(sql)
    conn.commit()
          
except:  
    conn.rollback()
    print("Please Recheck your code")   
print(c.rowcount, "record(s) deleted")    
   




#Drop the complete table
try:  
  
    sql = "DROP TABLE consumer"
    c.execute(sql)
    
except:  
    conn.rollback()
    print("Please Recheck your code")   
 




#Update the table
try:  
  
    sql = "UPDATE consumer SET name = 'janardahn' WHERE address = 'john'"
    c.execute(sql)
    conn.commit()
    print(c.rowcount, "record(s) affected")

except:  
    conn.rollback()
    print("Please Recheck your code") 





#You can limit the number of records returned from the query, by using the "LIMIT" statement:
try:  
  
    c.execute("SELECT * FROM customers LIMIT 5")
    myresult = c.fetchall()
    for x in myresult:
        print(x)

except:  
    conn.rollback()
    print("Please Recheck your code")   





#You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.
try:  
  
    sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      INNER JOIN products ON users.fav = products.id"
    
    c.execute(sql)
    
    myresult = c.fetchall()
    
    for x in myresult:
      print(x)

except:  
    conn.rollback()
    print("Please Recheck your code")   





    
conn.close()




















  