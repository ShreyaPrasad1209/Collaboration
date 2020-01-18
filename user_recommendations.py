#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
project_data= pd.read_csv('projectdata.csv')
project_data.set_index('ProjectID', inplace=True)

# In[2]:


# In[3]:

ids=['PID1', 'PID7']

for projectid in ids:
    user_data=pd.read_csv('userdata.csv')
    user_data.fillna(0, inplace=True)
    userids=user_data['User_ID/Skill_ID']
    user_data.drop(['User_ID/Skill_ID'], axis = 1, inplace=True)
    user_data = user_data / user_data.max(axis=0)
    d1=project_data.loc[projectid]
    #print(user_data.head(10))
    scores = np.dot(user_data, d1)
    scores=scores.transpose()
    df= pd.DataFrame(scores)
    df.sort_values(0, ascending=False, inplace=True)
    df['ID']=userids
    user_data=pd.read_csv('userdata.csv')
    df= df.join(user_data.set_index('User_ID/Skill_ID'), on='ID')
    df.drop([0], axis = 1, inplace=True)
    df=df.head(10)
    df.to_csv('output_userids'+str(projectid)+'.csv')
