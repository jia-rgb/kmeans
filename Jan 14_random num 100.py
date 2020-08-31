# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:19:37 2020

@author: jejia
"""

#%% create three  group , 100 number each
import numpy as np
import matplotlib.pyplot as plt

import random
X= -2 * np.random.rand(100,2)

X= -2 * np.random.randn(100,2)

mu1 = [0,10]

sigma1 = [[1,0],[0,1]]

a1 = np.random.multivariate_normal(mu1, sigma1, 100)
plt.scatter(a1[:,0],a1[:,1], color='red')

mu2 = [10,0]

sigma2 = [[2,0],[0,2]]

a2 = np.random.multivariate_normal(mu2, sigma2, 100)
plt.scatter(a2[:,0],a2[:,1], color='red')

mu3 = [10,10]

sigma3 = [[1,0.5],[0.5,1]]

a3 = np.random.multivariate_normal(mu3, sigma3, 100)
plt.scatter(a3[:,0],a3[:,1], color='red')
#from sklearn.cluster import KMeans
   #from sklearn.datasets import make_blobs
   #plt.figure(figsize=(12, 12))
#%matplotlib inline
#from scipy.stats import norm
# generate random numbers from N(0,1)
#random_state=
#data_normal = norm.rvs(size=100,loc=0,scale=1random_state， random_state=random_state)
#loc is mean, scale is standard diviation, size is how many samples
#generate some random data in a two-dimensional space

#X= -2 * np.random.rand(100,2)
#X1 = 1 + 2 * np.random.rand(50,2)
#X[50:100, :] = X1
#b_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)
#plt.scatter(X[ : , 0], X[ :, 1], s = 50, c = b_pred)
#plt.show()

#what is random_state


#%% kmean, abandoned because the code is too long. shorter version below this
import math

def getEuclidean(point1, point2):
    dimension = len(point1)
    dist = 0.0
    for i in range(dimension):
        dist += (point1[i] - point2[i]) ** 2
    return math.sqrt(dist)

def k_means(dataset, k, iteration):
    #initialize 簇心向量
    index = random.sample(list(range(len(dataset))), k)
    vectors = []
    for i in index:
        vectors.append(dataset[i])
    #initialize label
    labels = []
    for i in range(len(dataset)):
        labels.append(-1)
    #repeat interation times
    while(iteration > 0):
        #初始化簇
        C = []
        for i in range(k):
            C.append([])
        for labelIndex, item in enumerate(dataset):
            classIndex = -1
            minDist = 1e6
            for i, point in enumerate(vectors):
                dist = getEuclidean(item, point)
                if(dist < minDist):
                    classIndex = i
                    minDist = dist
            C[classIndex].append(item)
            labels[labelIndex] = classIndex
        for i, cluster in enumerate(C):
            clusterHeart = []
            dimension = len(dataset[0])
            for j in range(dimension):
                clusterHeart.append(0)
            for item in cluster:
                for j, coordinate in enumerate(item):
                    clusterHeart[j] += coordinate / len(cluster)
            vectors[i] = clusterHeart
        iteration -= 1
    return C, labels


dataset = a3
C, labels = k_means(dataset, 5, 4)
colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
for i in range(len(C)):
    coo_X = []    #x坐标列表
    coo_Y = []    #y坐标列表
    for j in range(len(C[i])):
        coo_X.append(C[i][j][0])
        coo_Y.append(C[i][j][1])
    plt.scatter(coo_X, coo_Y, marker='x', color=colValue[i%len(colValue)], label=i)
 
#plt.legend(loc='upper right')
plt.show()
print(labels)


#%% kmean #2
from sklearn.cluster import KMeans
import numpy as np

e=np.append(a1,a2,axis=0) 
e=np.append(e,a3,axis=0) 
X = np.array(e)

kmeans = KMeans(n_clusters=6, random_state=0).fit(X)
kmeans.labels_


kmeans.predict([[0,0],[12,3]])

kmeans.cluster_centers_


#print(labels)
from matplotlib import pyplot as plt
label_pred = kmeans.labels_

mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
#这里'or'代表中的'o'代表画圈，'r'代表颜色为红色，后面的依次类推
#print each cluster in different color and shape
color = 0
j = 0 
for i in label_pred:
    plt.plot([X[j:j+1,0]], [X[j:j+1,1]], mark[i], markersize = 5)
    j +=1
plt.show()


