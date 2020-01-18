#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import turicreate


# In[2]:


user_data=pd.read_csv('userdata.csv')
project_data= pd.read_csv('projectdata.csv')


# In[3]:


user_data.fillna(0, inplace=True)
userids=user_data['User_ID/Skill_ID']
user_data.drop(['User_ID/Skill_ID'], axis = 1, inplace=True)
user_data = user_data / user_data.max(axis=0)


# In[4]:


user_data['ID']=userids


# In[5]:


user_data.set_index("ID", inplace=True)


# In[6]:


userid=1
d1=user_data.loc[userid]

# In[7]:


project_ids = project_data['ProjectID']


# In[8]:

project_data.drop(['ProjectID'], axis=1, inplace=True)


# In[9]:

scores = np.dot(project_data, d1)


# In[10]:


res_df1= pd.DataFrame(scores)
res_df1['ProjectID']=project_ids

# In[11]:


res_df1.sort_values(0, ascending=False, inplace=True)


# In[12]:


user_project_data = turicreate.SFrame('Interactiondata1.csv') 


# In[13]:


personalized_model = turicreate.item_similarity_recommender.create(user_project_data,
                                                                  user_id = 'UserID',
                                                                  item_id = 'Interested')


# In[14]:


res_df2= personalized_model.recommend(users=[1], k=20, exclude_known = False)


# In[15]:


interaction_data= turicreate.SFrame('Interactiondata.csv')


# In[16]:


project_data['ProjectID']=project_ids

# In[17]:

project_data = turicreate.SFrame('projectdata.csv')
pm2 = turicreate.recommender.item_content_recommender.create(project_data, 'ProjectID')


# In[18]:


projids= interaction_data.filter_by(1, 'UserId')

# In[19]:


res_df3= pm2.recommend_from_interactions(projids['ProjectId'], k=20, exclude_known = False)


# In[20]:


rslt_df = pd.DataFrame(columns=['ProjectID', 'score'])

# In[91]:

for id in project_ids.iteritems(): 
    #print id[1]
    f1 = res_df1.where(res_df1['ProjectID']==id[1]).dropna()[0]
    f1= list(f1)
    f1=f1[0]
    #f2= res_df2.filter_by(id[1], 'Interested')['score']
    #print f2
    #if len(f2)==0:
    f2=0
    f3 = res_df3.filter_by(id[1], 'ProjectID')['score']
    if len(f3)==0:
        f3=0
    #print f3
    f=(f1+f2+f3)/3
    rslt_df.loc[id[0]] = [id[1],f[0]]
rslt_df.sort_values('score', ascending=False, inplace=True)
rslt_df=rslt_df.head(10)


# In[96]:


project_metadata= pd.read_csv('Projectmetadata.csv')


# In[97]:


rslt_df= rslt_df.join(project_metadata.set_index('ProjectID'), on='ProjectID')
rslt_df.to_csv('output.csv')

