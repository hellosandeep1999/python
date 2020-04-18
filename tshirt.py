# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:56:52 2020

@author: user
"""

"""

Q2. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height 
and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. 
How would you figure out the actual size of these 3 types of shirt to better 
fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of 
the data as stated above.


"""


----------------------------------------------------------------------------------------------------



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset (Bivariate Data Set with 3 Clusters)
dataset = pd.read_csv('tshirts.csv')

features = dataset.iloc[:, [1,2]].values

dataset.isnull().any(axis=0)
#Scatter all these data points on the matplotlib
# It seems as a human that it will have 3 clusters or groups
plt.scatter(features[:,0], features[:,1])
plt.show()


from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features) 
    wcss.append(kmeans.inertia_)
    
print(wcss)

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means to the dataset using 3 clusters

from sklearn.cluster import KMeans
# Since we have seen the visual, we have told the algo to make 3 cluster
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)

pred_cluster = kmeans.fit_predict(features) # We have only passed features 

print(pred_cluster)


print(len(features[pred_cluster == 1]))
print(len(features[pred_cluster == 0]))
print(len(features[pred_cluster == 2]))


# Visualising the clusters
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Medium')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Large')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Small')

print(kmeans.cluster_centers_)  

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')

plt.title('Clusters of datapoints')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()

         
           
           
           
           
         
           










