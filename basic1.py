#%%
import pandas as pd 
s1 = pd.core.series.Series(['one','two','three'])
s2 = pd.core.series.Series([1,2,3])
pd.DataFrame(data=dict(word=s1, num=s2))



#%%
friend_dict_list = [{'name':'Jone','age':20,'job':'student'},{'name':'Jenny','age':30,'job':'develop'},{'name':'Nate','age':30,'job':'teacher'}]
df = pd.DataFrame(friend_dict_list)
df.head()

#%%
df = df[['name','age','job']]

#%%
df.head()

#%%
from collections import OrderedDict


#%%
friend_ordered_dict = OrderedDict([('name',['John','Jenny','Nate']),('age',[20,30,30]),('job',['student','develop','teacher'])])
df = pd.DataFrame.from_dict(friend_ordered_dict)

#%%
df.head()

#%%
friend_list =[['John',20,'student'],['Jenny',30,'developer'],['Nate',30,'teacher']]
column_name = ['name','age','job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)

#%%
df.head()

#%%
friend_list = [['name',['John','Jenny','Nate']],['age',[20,30,30]],['job',['student','develop','teacher']]]
df = pd.DataFrame.from_items(friend_list)

#%%
df.head()

#%%
df.to_csv('friend_list_from_df.csv')

#%%
friend_list = [['name',['John',None,'nate']],['age',[20,None,30]],['job',['student','develop','teacher']]]
df = pd.DataFrame.from_items(friend_list)

#%%
df.head()

#%%
