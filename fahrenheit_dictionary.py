# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:42:32 2020

@author: user
"""

"""
Code Challenge

# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

1 Get the corresponding `celsius` values in list
"""


#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))





------------------------------------------------------------------------------------------




"""
2 Create the `celsius` dictionary
"""


#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)










----------------------------------------------------------------------------------------





"""
3 convert a dictionary of Fahrenheit temperatures into celsius
"""


# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
print(celsius_dict)



