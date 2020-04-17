# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:49:45 2020

@author: user
"""
inp = int(input())

d = {}
for i in range(inp):
    name,*marks = input().split()
    scores = list(map(float, marks))
    average = (scores[0]+scores[1]+scores[2])/3
    d[name] = average
d_name = input()
print("%.2f" % d[d_name])
    






x = int (input()) 
y = int (input()) 
n = int (input()) 
ar = [] 
p = 0 
for i in range ( x + 1 ) : 
    for j in range( y + 1): 
        if i+j != n: 
            ar.append([]) 
            ar[p] = [ i , j ] 
            p+=1 
print(ar)

x = int (input()) 
y = int (input()) 
z = int (input()) 
n = int (input())
ar = []
p = 0
for i in range(x+1):        
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                 ar.append([])
                 ar[p] = [i , j , k]
                 p += 1
print(ar)
    
string = input()
print(string.swapcase())


def swap_case(s):
    return s.swapcase()

s = input()
result = swap_case(s)
print(result)



def count_substring(string, sub_string):
    count = 0
    a = len(string)
    b = len(sub_string)
    for i in range(a):
         if sub_string in string[i:b]:
              count +=1
              b += 1
         else:
             b += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


s1 = "ABCDCDCCDGSTCDDCDC"
s2 = "CDC"
count = 0
a = len(s1)
b = len(s2)
for i in range(a):
    if s2 in s1[i:b]:
        count +=1
        b += 1
    else:
        b += 1


s = input()
n = int(input())
j = 0
k = n
for i in range(int(len(s)/n)+n):
       print(s[j:k])
       j += n
       k += n
       
       
width = 20
print ('HackerRank'.ljust(width,'-'))




thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))








def wrap(string, max_width):
        l = []
        j = 0
        k = max_width
        for i in range(int(len(string)/max_width)+1):
            l.append(string[j:k])  
            j += max_width
            k += max_width
        return "\n".join(l)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)








import time

def f1():
    l = [7, 13, 17, 231, 12, 8, 3]
    yield sum(l)/(len(l))


def f2():
    l = [7, 13, 17, 231, 12, 8, 3]
    return sum(l)/(len(l))

t1 = time.clock()
print(next(f1()))
t2 = time.clock()


t3 = time.clock()
print(f2())
t4 = time.clock()
print(t2-t1)
print(t4-t3)



import numpy

x = numpy.array([[1,2,7],[7,7,1]])
y = numpy.array([[6,5,5],[0,6,1]])




a = ['east','jaipur','japiur','62137','b']
from csv import writer
  
with open("former.csv",'+a',newline='') as obj_read:
    
    csv_read = writer(obj_read)
    
    csv_read.writerow(a)
    
    


class student:
    
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    
    
    def talk(self):
        print("Student name is: ",self.name)
        print("Student roll number is: ",self.roll_no)


s = student('sandeep','1001')
print(s.name)
print(s.roll_no)


class employee:
    
    def __init__(a,eno,ename,esal,eadd):
        a.eno = eno
        a.ename = ename
        a.esal = esal
        a.eadd = eadd
        
    def info(x):
        print("*"*20)
        print("Employee number will be: ",x.eno)
        print("Employee name is the: ",x.ename)
        print("Employee salary is: ",x.esal)
        print("Employee adderess is: ",x.eadd)
        print("*"*20)

e1 = employee(100,'rajesh',70000,'banglore')
e2 = employee(200,"suraj",60000,'UK')


e1.info()

class Test:
    def __init__(self):
        print("hello")
        
        
t = Test()
        
        
        
        
list1 = [1,'string',True,False,1,2.5]


list1.index(True)
print(list1)
#list1.remove(list[])
#list1.remove(list1[3])
     
#list1.remove(True)
        
        
        
        
        
def remove():
    if True in list1:
        if 
            
        print(list1.index(True))


l1 = [[1,2,3,4,5],[1,4,2,6,7],[1,4,2,6,9],[1,6,2,9,7]]   


for i in l1:
    for j in i:
        if j == 2:
            break
        print(j)
    
    
for a in [2,5,6,7]:
    print("outer begin:",a)
    flag=False
    for b in [100,300,400,500]:
        print("Inner begin",a,b);
        if b==400:
            flag=True;
            break
        print("inner end",a,b);
    if flag:
        break;
    print("outer end:",a)



class student:
    cname = 'Student_study'
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def stu(self):
        print("name is: ",self.name)
        print("roll_no is: ",self.roll_no)
   
    @classmethod
    def getclassname(cls):
        print('class name: ',cls.cname)
   
    @staticmethod   
    def average(x,y):
        print((x+y)/2)
        
    
s1 = student('rajesh',100)
s2 = student('suraj',101)


student.getclassname()
s1.average(10,20)




class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        
    
    
    
    
t1 = Test()

t1.a = 888
t1.b = 999
t2 = Test()
print(t1.a,t1.b)
print(t2.a,t2.b)


a = int((33-7)/2)
print('-'*a+"WELCOME"+'-'*a)


Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------



class Myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print('student name is: ',self.name)

class student(Myclass):
    def __init__(self,name,age):
        super().__init__(name,age)


p1 = student('Rajesh',25)
p2 = Myclass('suraj',22)
p1.age = 40
p1.name = 'ravi'


class Topten:
    def __init__(self):
        self.nums = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.nums <= 10:
            val = self.nums
            self.nums += 1
            
            return val
        else:
            raise StopIteration

values = Topten()

for i in values:
     print(i)    
        


class Employee:
    num_employee = 0
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname.lower()+"."+lname.lower()+"@gmail.com"
        Employee.num_employee += 1
    def fullname(self):
        return "{} {}".format(self.fname,self.lname)
        
class Developer(Employee):
    pass

emp1 = Employee("rajesh","Sharma",500000)
emp2 = Employee("Suraj","Uk",265922)
epm3 = Employee("Mohit","Sir",65000)

print(emp.fullname())

print(Employee.fullname(emp))



import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

#list of prime numbers
    
#is_prime(n) Will return True
# 2,3,5,7,11,13,17,19,23
    
#is_prime(n) Will return False
# 1,4,6,8,9,10,12,14,15,16,18

is_prime(2) SUCCESS
is_prime(3) SUCCESS
is_prime(8) Fail
is_prime(10) SUCCESS
is_prime(13) SUCCESS
is_prime(15) Fail
is_prime(23) SUCCESS
is_prime(18) SUCCESS


import unittest
class testdemo(unittest.TestCase):
    
    def test_1(self):
        self.assertFalse(is_prime(2))
    def test_2(self):
        self.assertFalse(is_prime(4))
  
import unittest

from prime import is_prime

class Tests ( unittest.TestCase):
  def test_1(self):
    """Check that 1 is not prime. """
    self.assertFalse(is_prime(1))

  def test_2(self):
    """Check that 2 is prime. """
    self.assertTrue(is_prime(2))

  def test_8(self):
    """Check that 8 is not prime. """
    self.assertFalse(is_prime(8))


unittest.main()

"""

Iteration

"""


list = ["bannana","mango","apple","python"]
it = iter(list)

for i in range(len(list)):
    print(next(it))
    
    
class myclass:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=20:
            val = self.num*self.num
            self.num += 1
            return val
        else:
            raise StopIteration

my = myclass()
a = iter(my)
for i in a:
    print(i)

class py_solution:
    def int_to_Roman(self, num):
        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num//val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    
    
a = py_solution()    
    
print(a.int_to_Roman(200))
    
    
"""
Debugging

"""
import pdb
val = [1,3,4,5,6,7]
sum = 0
for i in val:
    sum = sum + i
print(sum)
pdb.set_trace()







import pandas as pd
a = pd.Series(['a','b','c','d'])
a = pd.Series(['a','b','c','d'],index = ['100','101','102','103'])


df = pd.read_csv("Desktop/Salaries.csv")

df.ndim

df.size
df.shape

df.info()

df.head(7)
    
df.tail(8)

df.index

df.columns

df.dtypes

df.values

df.loc[34:56]

df.loc[10:14,['salary','sex']]

df.iloc[10:14,[1,4]]

df['sex'].unique()
 
a = df['sex'].unique().tolist()

df['sex'].value_counts

df['sex'].value_counts(normalize = True)

df['sex'].value_counts(dropna = False)

df['salary'].mean()

df['salary'].std()

df.count()

df['salary'].isnull()

df[df['salary'].isnull()]


df_rank = df.groupby(['rank','sex'])

df_rank.mean()
df_rank.size()
df_rank.groups['Prof','Male']


df_rank=df.groupby(['rank','sex'])

df_rank.mean()
df_rank.groups
df_rank.count()


df.groupby('rank')[['salary','sex']].max()

df[df['salary'] > 120000].count()

df.loc[df['salary']>120000,'salary'].count()

df.loc[(df['salary'] > 120000) & (df['phd'] > 10) & (df['sex'] == 'Female' )]

df[df['phd'].isnull()]

df_fill = df.fillna(0)

df_round = df.fillna(round(df.mean(),0))

df['phd'] = df['phd'].fillna(df['phd'].mean())
df[df['phd'].isnull()]


df.drop('discipline',axis = 1,inplace=True)

df1 = df.dropna()

df["bool_sex"] = df["sex"].map(lambda x : 0 if x == 'Male' else 1 )


'''
1. Which Male and Female Professor has the highest and the lowest salaries
'''
df['rank'].unique()


df3 = df.loc[df['rank'] == "Prof"]



"""

Numpy

"""

import numpy as np 

x = np.zeros(20, dtype=np.uint8)
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
print (x.itemsize)



x = np.zeros((3,3,3))

x = np.linspace(2,8,20,dtype = np.int)


x = np.random.random((3,3))*200

x = (np.identity(n = 5))


x = np.arange(5)
b = np.arange(5)

a = np.array(list(zip(x,b)))



incomes = np.random.normal(27000,15000,10000)


print()


import matplotlib.pyplot as plt
plt.hist(incomes, 20)
plt.show()


import matplotlib.pyplot as plt

plt.axis([0,50,0,5])

plt.boxplot()


x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]



plt.title("A line graph")

plt.xlabel("Y")

plt.ylabel("")




list = []
k = 2
while True: 
    for i in range(2,k):
        if k % i == 0:
            k += 1
            break
    else:
        list.append(k)
        k += 1
    if len(list) == 20:
        print(list)
        break
    
            
import matplotlib.pyplot as plot

x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]

plt.title("A line graph")

plt.xlabel('X')

plt.ylabel('Y')
plt.grid(True)

plt.scatter(x,y)

plt.plot(x,y)

plt.savefig("scatter.jpg")


plt.show()
plt.plot(x,y,color = 'green')
plt.plot(x,y,color = "#F2FF00")
         
plt.scatter(x,y,marker = "o",color = "black",label = "marker = '{0}'".format('.'))

labels = 'CSE','ECE','IT','EE'
size = [40,35,20,26]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = [0.5,0,0,0]


plt.pie(size, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=180)


objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
performance = [10,8,6,4,2,1]
 
plt.bar([0,1,2,3,4,5], performance, align='center', alpha=1.0)
plt.xticks([0,1,2,3,4,5], objects)
plt.ylabel('Usage')
plt.xlabel('Laguages')
plt.title('Programming Language Usage')
 
plt.show()


customerWaitTime = [43.1,35.6,37.6,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3,31.4,35.6,45.2,54.1,45.6,36.5,43.1]

customerWaitTime.sort()

print(customerWaitTime)
 
plt.hist(customerWaitTime,bins=[25,30,35,40,45,50,55]) 

plt.axis([25, 60, 0, 6]) 
plt.xlabel('Seconds')
plt.ylabel('Customers')



"""
Tutorial
"""

import pandas as pd
df = pd.read_excel("Book1.xslx")    #, na_values={  #Header = 1 or 0
        'eps':["not available","n.a."],
        'revenue':["not available","n.a.",-1],
        'eps':["not available","n.a."]
        })
df

df.to_csv("new.csv",columns=['column1','column2'])

df.to_csv("new.csv",header = False)


list  = ["banana","mango,","apple"]

a = iter(list)






import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0,2.0,0.01)
s = 1 + np.cos(2*np.pi*t)

plt.plot(t,s)

plt.grid(True)
plt.xlabel("Time(t)")
plt.ylabel("Seconds")
plt.title("Cosine Wave")

plt.show()




import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,.01)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label="sin baba")
plt.plot(x,y2,label="cos baba")

plt.legend()


import matplotlib.pyplot as plt; 
 
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
performance = [10,8,6,4,2,1]
 
plt.bar([0,1,2,3,4,5], performance, align='center', alpha=1.0)
plt.xticks([0,1,2,3,4,5], objects)
plt.ylabel('Usage')
plt.title('Programming Language Usage')
 
plt.show()
import matplotlib.pyplot as plt
# Customers wait times in seconds ( n = 20 customers )
customerWaitTime = [43.1,35.6,37.6,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3,31.4,35.6,45.2,54.1,45.6,36.5,43.1]

customerWaitTime.sort()
# [1 to 35]      30.3, 31.2, 31.4                     [3]
# [35 to 40]     35.6, 35.6, 36.5, 37.6               [4]
# [40 to 45]     40.3, 42.2, 43.1, 43.1, 43.5         [5]
# [45 to 50]     45.2, 45.3, 45.5, 45.6, 47.3         [5]
# [50 to 55]     50.2, 54.1                           [2]

#Ramesh can conclude that the majority of customers wait between 35.1 and 50 seconds.

print(customerWaitTime)
 
plt.hist(customerWaitTime,bins=[25,30,35,40,45,50,55]) 

plt.axis([25, 60, 0, 6]) 
plt.xlabel('Seconds')
plt.ylabel('Customers')

￼


import pandas as pd
a = ["Time",2,3,6,5,4,9,8]
s = pd.Series(a)


s.dtype

fruits = ["apple","bananan","mango"]
weekdays = ["mon","tue","wed"]

pd.Series(fruits,index=weekdays)

pd.read_csv()
￼￼￼

pd.read_csv()
pd.Series()



titanic = pd.read_csv("training_titanic.csv")

titanic.sort_values(inplace = True)



titanic["rajesh"] = titanic.PassengerId+","+titanic.Sex
    
    

def fun1(str):
    if str == "male":
        return 1
    else:
        return 0

c = titanic["Sex"]
c.apply(fun1)
 this season bring some new like its included data analytics part
   
    
url = "https://github.com/vishwajeetsinghrana8/MachineLearning/edit/master/ML55/employees.csv"

d1 = pd.read_csv("file.txt")
 
d1.to_csv("employees.csv")
    
d1.columns
d1.info()
d1.City
d1["Colors Reported"].value_counts(ascending=True) 
select = ["City","Colors Reported"]
d1[select]
    

import pandas as pd
nba = pd.read_csv("nba.csv")

nba["Salary"] = nba["Salary"].fillna(0).astype(int)


nba["Ranking"] = nba["Salary"].rank(ascending=False)


import math

math.sqrt(4)


import pandas as pd

bond = pd.read_csv("jamesbond.csv")

bond.set_index("Film")
bond.reset_index(drop=True)

bond.set_index("Year",inplace=True)

















































