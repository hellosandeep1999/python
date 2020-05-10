# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:27:07 2020

@author: user
"""




"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) 
and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

Perform K-means clustering to distinguish urban drivers and rural drivers.
Perform K-means clustering again to further distinguish speeding drivers 
from those who follow speed limits, in addition to the rural vs. urban division.
Label accordingly for the 4 groups.


"""


---------------------------------------------------------------------------------------------------





# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset (Bivariate Data Set with 3 Clusters)
dataset = pd.read_csv('deliveryfleet.csv')

features = dataset.iloc[:, [1,2]].values


# There is no Categorial data
# There is no Missing data 
# There is no different scale data

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


# Fitting K-Means to the dataset using 2 clusters


from sklearn.cluster import KMeans
# Since we have seen the visual, we have told the algo to make 3 cluster
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)

pred_cluster = kmeans.fit_predict(features) # We have only passed features 

print(pred_cluster)


print(len(features[pred_cluster == 1]))
print(len(features[pred_cluster == 0]))



# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')

print(kmeans.cluster_centers_)  # There are three points for 4 centroid

print(kmeans.cluster_centers_[:, 0]) # x 
print(kmeans.cluster_centers_[:, 1]) # y 

# Central Location of the Cluster == Centroid

# Centroid = Avg of x coordinate and Avg of y coordinate for lets assume Cluster 1
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')


plt.title('Clusters of datapoints')
plt.xlabel('Distance')
plt.ylabel('Speed')
plt.legend()
plt.show()



         
#2) Perform K-means clustering again to further distinguish speeding drivers 
#from those who follow speed limits, in addition to the rural vs. urban division.
#Label accordingly for the 4 groups.          
           
           
           
           
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('deliveryfleet.csv')

features = dataset.iloc[:, [1, 2]].values
   

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)

pred_cluster = kmeans.fit_predict(features) 

print(pred_cluster) # Its the cluster id with 0,1,2,3 

print(features[pred_cluster == 0])

print(features[pred_cluster == 1])

print(features[pred_cluster == 2])

print(features[pred_cluster == 3])


# Visualising the clusters
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Follow speed in Rural')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Not follow speed in Urban')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Follow speed in Urban')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'olive', label = 'Not follow speed in Rural')


print(kmeans.cluster_centers_)  # There are two points for 2 centroid   Rural follow speed

print(kmeans.cluster_centers_[:, 0]) 
print(kmeans.cluster_centers_[:, 1])
# Central Location of the Cluster == Centroid

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')


plt.title('Clusters of datapoints')
plt.xlabel('Distance')
plt.ylabel('Speed')
plt.legend()
plt.show()

      
           
    
           
           
           
           