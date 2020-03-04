# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:48:28 2020

@author: user
"""
"""

1. Handle the missing values for Price column

"""


import pandas as pd

df2 = pd.read_csv("Automobile.csv")

avg = int(df2["price"].mean())

df2["price"] = df2["price"].fillna(avg)


"""

2. Get the values from Price column into a numpy.ndarray

"""


import numpy as np

a = list(df2["price"])

print(np.array(a))



"""

3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price

"""
df2["price"].min()

df2["price"].max()

df2["price"].mean()

df2["price"].std()

























