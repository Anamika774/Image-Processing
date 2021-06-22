# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 18:11:01 2021

@author: Anamika
"""


import pandas as pd
import numpy as npn
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.metrics import confusion_matrix

#for removing null values of artwork_data.csv
data = pd.read_csv("C:/Users/Anamika/Desktop/open/dataset/artwork_data.csv", dtype='unicode')
print(data.isnull().sum())
modified=data.dropna(subset=['url','thumbnailUrl'])
print(modified.isnull().sum())
modified.to_csv('artwork_data')

data1 = pd.read_csv("C:/Users/Anamika/Desktop/open/dataset/arts-and-subjects-list.csv", dtype='unicode')
print(data1.head())
modified1=data1.dropna(subset=['thumbnail'])
print(modified1.isnull().sum())
modified1.to_csv('arts-and-subjects-list')

data2 = pd.read_csv("C:/Users/Anamika/Desktop/open/dataset/artist_data.csv", dtype='unicode')
print(data2.head())
modified2=data2.dropna(subset=['url'])
print(modified2.isnull().sum())
modified2.to_csv('artist_data.csv')

