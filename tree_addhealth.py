# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:45:17 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('tree_addhealth.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, 2].values

dataset.isnull().any(axis=0)