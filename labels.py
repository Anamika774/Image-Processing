# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 13:46:37 2021

@author: Anamika
"""


import pandas as pd

def parent(df,value):
    print(df.loc[df['childId']==value])
    if(df.loc[df['childId']==value]):
        d=dict();
        d['parenId']=df.loc['parentId']
        d['parent_name']=df.loc['parentName']
        return d
def concat(df):
    for i in range(len(df)):
        data=parent(df,df.iloc[i,0])
        df2=pd.DataFrame.from_dict(data)
        df['relation']=df['childName']+'['+df['childId']+']'+df['parentName']+'['+df['parentId']+']'+df2['parent_name']+'['+df2['parenId']+']'
        continue
        return df
df = pd.read_csv("C:/Users/Anamika/Desktop/open/dataset/original/hierarchy.csv", dtype='unicode')

df_final=concat(df)
print(df_final.head())
