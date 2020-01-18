import pandas as pd
import numpy as np
user_data=pd.read_csv('userdata.csv')
project_data= pd.read_csv('projectdata.csv')
user_data.fillna(0, inplace=True)
userids=user_data['User_ID/Skill_ID']
user_data.drop(['User_ID/Skill_ID'], axis = 1, inplace=True)
user_data = user_data / user_data.max(axis=0)
user_data['ID']=userids
user_data.set_index("ID", inplace=True)
userid=1
d1=user_data.loc[userid]
project_ids = project_data['ProjectID']
project_data.drop(['ProjectID'], axis=1, inplace=True)
scores = np.dot(project_data, d1)
scores= scores.transpose()
df= pd.DataFrame(scores)
df['ProjectID']=project_ids
df.sort_values(0, ascending=False, inplace=True)
res_df = df[df[0] > 5] 
print(res_df)
