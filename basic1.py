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
friend_list =[['name',['John','Jenny','Nate']],['age',[20,30,30]],['job',['student','developer','teacher']]]
df = pd.DataFrame.from_items(friend_list)
df.head()

#%%
df[1:3]

#%%
df.loc[[0,2]]

#%%
df_filtered = df[df.age >25]

#%%
df_filtered = df.query('age>25')
df_filtered

#%%
df_filtered = df[(df.age>25)&(df.name=='Nate')]
df_filtered

#%%
df

#%%
friend_list = [['John',20,'student'],['Jenny',30,'developer'],['Nate',30,'teacher']]
df = pd.DataFrame.from_records(friend_list)
df

#%%
df.iloc[:,0:2]

#%%
df.iloc[:,[0,2]]

#%%
friend_dict_list =[{'age':20,'job':'student'},{'age':30,'job':'developer'},{'age':30,'job':'teacher'}]
df = pd.DataFrame(friend_dict_list,index=['John','Jenny','Nate'])
df.head()

#%%
df.drop(['John','Nate'])

#%%
friend_dict_list = [{'name':'Jone','age':20,'job':'student'},{'name':'Jenny','age':30,'job':'developer'},{'name':'Nate','age':30,'job':'teacher'}]
df = pd.DataFrame(friend_dict_list)

#%%
df = df.drop(df.index[[0,2]])

#%%
friend_dict_list = [{'name':'Jone','age':20,'job':'student'},{'name':'Jenny','age':30,'job':'developer'},{'name':'Nate','age':30,'job':'teacher'}]
df = pd.DataFrame(friend_dict_list)
df = df[df.age != 30]

#%%
df

#%%
df = df.drop('age',axis=1)
df

#%%
df['salary'] = 0
df

#%%
import numpy as np 
df['salary'] = np.where(df['job'] !='student','yes','no')
df

#%%
friend_dict_list =[{'name':'John','midterm':95,'final':85},{'name':'Jenny','midterm':85,'final':80},{'name':'Nate','midterm':10,'final':30}]
df = pd.DataFrame(friend_dict_list,columns=['name','midterm','final'])
df

#%%
df['total'] = df['midterm'] +df['final']
df

#%%
df['average'] = df['total'] /2
df

#%%
grades = []
for row in df['average']:
    if row >= 90:
        grades.append('A')
    elif row >= 80:
        grades.append('B')
    elif row >= 70:
        grades.append('C')
    else:
        grades.append('F')
df['grade'] = grades
df

#%%
def pass_or_fail(row):
    print(row)
    if row != "F":
        return 'Pass'
    else:
        return 'Fail'

df.grade = df.grade.apply(pass_or_fail)
df

#%%
data_list = [{'yyyy-mm-dd':'2000-06-27'},{'yyyy-mm-dd':'2002-09-24'},{'yyyy-mm-dd':'2005-12-20'}]
df = pd.DataFrame(data_list, columns=['yyyy-mm-dd'])
df

#%%
def extract_year(row):
    return row.split('-')[0]
df['year'] = df['yyyy-mm-dd'].apply(extract_year)
df

#%%
def extract_year(year, current_year):
    return current_year - int(year)

#%%
df['age'] = df['year'].apply(extract_year,current_year=2018)
df
#%%
def get_introduce(age,prefix,suffix):
    return prefix + str(age) + suffix

#%%
df['introduce'] = df['age'].apply(get_introduce,prefix="I am",suffix=" years old")
df

#%%
