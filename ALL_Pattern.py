# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 18:46:35 2020

@author: user
"""

"""
Pattern 
     
       * * * *

"""

n = int(input("Enter A number of n: "))
for i in range(n):
    print("* ",end="")
    
    


""" 
Pattern
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    
"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print("* "*n)
    
    
    
""" 
Pattern
    5 5 5 5 5 
    5 5 5 5 5 
    5 5 5 5 5 
    5 5 5 5 5 
    5 5 5 5 5 
    
"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print((str(5)+ " ")*n)



""" 
Pattern
    1 1 1 1 1
    2 2 2 2 2
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5
    
"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print((str(i+1)+" ")*n)



""" 
Pattern
    A A A A A
    A A A A A
    A A A A A 
    A A A A A
    A A A A A
    
"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print((chr(65)+" ")*n)
    
    
    
"""
Pattern
    A
    B B
    C C C
    D D D D
    E E E E E

"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print((chr(65+i)+" ")*(i+1))
    
    

"""
Pattern
    * * * * *
    * * * *
    * * *
    * *
    *

"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print("* "*(n-i))




"""
Pattern
    1 2 3 4 5
    1 2 3 4
    1 2 3 
    1 2
    1
    
"""


n = int(input("Enter a number of n: "))
for i in range(n):
    for j in range(n-i):
        print(j+1,"",end="")
    print()
        
    
"""
Pattern
      1
     2 2
    3 3 3
  4 4 4 4 4
 5 5 5 5 5 5

"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print(i+1,"",end="")
    print()





"""
Pattern


                  1 
                2 1 2 
              3 2 1 2 3 
            4 3 2 1 2 3 4 
          5 4 3 2 1 2 3 4 5
          
"""



inp = int(input("Enter a number: "))
for i in range(inp):
    print("  "*(inp-i-1),end = '')
    for j in range(i+1):
        print((i+1)-j,end = " ")
    for j in range(i):
        print(j+2,end = " ")
    print()

  

"""
Pattern
        E
       E D
      E D C
     E D C B
    E D C B A

"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print(" "*(n-i-1), end="")
    for j in range(i+1):
        print(chr(64+n-j),"",end="")
    print()


"""
Pattern
     A
     A B
     A B C
     A B C D
     A B C 
     A B
     A   
     
"""
n = int(input("Enter a number of n: "))
for i in range(n):
    for j in range(i+1):
        print((chr(65+j)+" "), end="")
    print()
for i in range(n-1):
    for k in range(n-i-1):
        print((chr(65+k)+" "), end="")
    print()


"""
Pattern
      A B C D E 
        A B C D
          A B C
            A B
              A
"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print("  "*i,end="")
    for j in range(n-i):
        print((chr(65+j)+" "),end="")
    print()



"""
Pattern
     A B C D E F 
      A B C D E 
       A B C D 
        A B C 
         A B 
          A 
"""    
n = int(input("Enter a number of n: "))
for i in range(n):
    print(" "*i,end="")
    for j in range(n-i):
        print((chr(65+j)+" "),end="")
    print()


"""
Pattern
          *
         * *
        * * *
       * * * *
      * * * * *
       * * * *
        * * *
         * *
          *
"""
n = int(input("Enter a number of n: "))
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print("* ",end="")
    print()
for i in range(n-1):
    print(" "*(i+1),end="")
    for j in range(n-i-1):
        print("* ",end="")
    print()
    
"""
Pattern
     *
     * *
     * * *
     * * * *
     * * * * *
     * * * * * *
     * * * * *
     * * * *
     * * * 
     * *
     *
"""
n = int(input("Enter a number of n: "))
for i in range(n):
    print("* "*(i+1))
for i in range(n-1):
    print("* "*(n-i-1))
    
    
"""
Pattern
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print("  "*(n-i-1)+"* "*(i+1))
for i in range(n-1):
    print("  "*(i+1)+"* "*(n-i-1))
    


"""
Pattern
                  *
                *   *
              *       *
            *           *
          *               *
        *                   *
      *                       *
      
      
"""
n = int(input("Enter a number of n: "))
for i in range(n):
    print(" "*(n-i-1)+"* ",end="")
    if i>=1:
        print(" "*(2*i-1)+"* ",end="")
    print()


"""
Pattern
     *              *
      *            *
       *          *
        *        *
         *      *
          *    *
           *  *
            *
"""
n = int(input("Enter a number of n:"))
for i in range(n):
    print(" "*i,"* ",end='')
    if i!= n-1:
        print(" "*(2*n-2*i-3)+"* ",end="")
    print()


"""
Pattern
    A        A
     B      B
      C    C
       D  D
        E
"""
n = int(input("Enter a number of n:"))
for i in range(n):
    print(" "*i,chr(65+i),end="")
    if i!= n-1:
        print(" "*(2*n-2*i-3)+chr(65+i),end="")
    print()

"""
Pattern
              1
            1 2
          1 2 3 
        1 2 3 4 
      1 2 3 4 5 
        1 2 3 4
          1 2 3 
            1 2 
              1
              
"""
n = int(input("Enter a number of n:"))
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print(j+1,end="")
    print()
for i in range(n-1):
    print(" "*(i+1),end="")
    for j in range(n-i-1):
        print(j+1,end="")
    print()
        
    
    












































          





















































    
    
    
    
    
    
    
    

      





























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
























       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    