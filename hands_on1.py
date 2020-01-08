# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:13:47 2020

@author: user
"""

#string slice


#Print characters at the even index number 
string = "Rajasthan"
print(str[0::2])




#Print the given string in reverse
string = "Rajasthan"
print(str[::-1])




#Print Forsk using slicing ( forward indexing Left to Right  ) 
string = "Forsk Technologies"
print(string[:5])



#Print Forsk using slicing ( Reverse indexing Right to Left  )
string = "Forsk Technologies"
print(string[-18:-12])




#Print Technologies using slicing ( forward indexing Right to Left )
string = "Forsk Technologies"
print(string[6:18])




#Print ksroF using slicing ( forward indexing and Reverse  Indexing)  
string = "Forsk Technologies"
print(string[5::-1])
print(string[-13::-1])




#Print Technologies Forsk using slicing ( forward indexing Left to Right  )
string = "Forsk Technologies"
print(string[6:18],string[:5])




#Print Technologies Forsk using slicing ( Reverse indexing Right to Left ) 
string = "Forsk Technologies"
print(string[-12:],string[:-12])


f = "i love apple"
res = len(f.split()) 
print(res)





























