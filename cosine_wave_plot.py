# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:52:57 2020

@author: user
"""

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

