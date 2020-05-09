# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:38:36 2020

@author: user
"""

'''Code Challenge 1'''
"""
For our first pie chart, 
the data we will plot describes the number of students
who choose different engineering majors at 
colleges in the US each year.

Discipline 	            Number of graduates
Civil Engineering 	    15,000 graduates
Electrical Engineering 	50,000 graduates
Mechanical Engineering 	45,000 graduates
Chemical Engineering 	10,000 graduates

"""







import matplotlib.pyplot as plt
labels = ['Civil','Electrical','Mechanical','Chemical']
sizes = [15000,50000,45000,10000]
colors = ["gold","yellowgreen","lightcoral","lightskyblue"]
explode = [0,0,0.5,0]

plt.pie(sizes,labels = labels,
        explode = explode,
        colors = colors,
        autopct='%1.2f%%',
        shadow=True,
        startangle = 90)

plt.axis('equal')
plt.show()













---------------------------------------------------------------------------------------------



'''Code Challenge 2'''
"""
x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]

Plot a Bar Graph
"""    










import matplotlib.pyplot as plt
 
x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]
 
plt.bar([0,1,2,3,4,5], energy, align='center', alpha=1.0)
plt.xticks([0,1,2,3,4,5],x)
plt.ylabel('Used Energy')
plt.xlabel('Names of all gases')
plt.title('Gases Bar Chart')
 
plt.show()









