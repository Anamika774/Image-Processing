# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 13:46:37 2021

@author: Anamika
"""


import pandas as pd
import sys
import argparse


def parent(dataf, sub_id, par_id, labellist):
    # add current parent minimally
    subdf = dataf.loc[dataf['childId'] == sub_id]
    num = subdf['parentId'].values[0] # assumes sub_id is unique, which is the case here
    name = subdf['parentName'].values[0]
    labellist.append(name+ '_' + num)  # append child label first

    pardf = dataf.loc[dataf['childId']==par_id]
    if len(pardf)!=0: #there is also parent of parent
        parpar_id = pardf['parentId'].values[0] #id of parent of parent
        labellist = parent(dataf, par_id, parpar_id, labellist) #notice order of arguments passed, par_id is the subject id now in the next iter
        #recursive call to parent function
    return labellist

def concat(df):
    all_labels=[]
    for i in range(len(df)):
        subjectId = df.iloc[i, 0] # childId
        name = df.iloc[i, 1] #childName #append child label first # childName   #label(subjectId) -> the local label  ; e.g. label(17) -> “features”
        parentId = df.iloc[i, 2] #direct parent Id
        label = name+'_'+subjectId #e.g., concatenate numbers and strings with underscores e.g., people_91
        final_llist = parent(df, subjectId, parentId, [label]) #does the parent have a parent?
        final_llist.reverse()
        all_labels.append('->'.join(final_llist)) #reverse list order, so that it goes from parent to -> child
    df['relation'] = all_labels
    return df #removed indentation from return statement to run entire for

def main(): #main cycle in your code
    #Changed so that it reads from a more generic location, i.e., without giving away your desktop path
    # input folder is passed as an argument
    #parser = argparse.ArgumentParser()
    #parser.add_argument('C:/Users/Anamika/Desktop/open/dataset/original/hierarchy.csv')
    #args = parser.parse_args()
    df = pd.read_csv("C:/Users/Anamika/Desktop/open/dataset/original/hierarchy.csv", dtype='unicode')
    df_clean = df[df['childId'].notnull()] #handle empty rows
    df_final=concat(df_clean)
    print(df_final.head())
    df_final.to_csv("C:/Users/Anamika/Desktop/open/dataset/labels.csv")
    return 0

if __name__ == '__main__':

    sys.exit(main())
