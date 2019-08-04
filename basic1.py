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
def get_introduce2(row):
    return "I was born in " + str(row.year) + "my age is " + str(row.age)
df.introduce = df.apply(get_introduce2,axis=1)
df

#%%
def extract_year(row):
    return row.split('-')[0]

date_list = [{'yyyy-mm-dd':'2000-06-27'},{'yyyy-mm-dd':'2002-09-24'},{'yyyy-mm-dd':'2005-12-20'}]
df = pd.DataFrame(date_list, columns =['yyyy-mm-dd'])
df

#%%
df['year'] = df['yyyy-mm-dd'].map(extract_year)
df

#%%
job_list = [{'age':20,'job':'student'},{'age':30,'job':'developer'},{'age':30,'job':'teacher'}]
df = pd.DataFrame(job_list)
df

#%%
df.job = df.job.map({"student":1,"developer":2,"teacher":3})
df
#%%
x_y = [{'x':5.5, 'y':-5.6},{'x':-5.2,'y':5.5},{'x':-1.6,'y':-4.5}]
df = pd.DataFrame(x_y)
df

#%%
df = df.applymap(np.around)
df

#%%
friend_dict_list =[{'name':'John','midterm':95,'final':85},{'name':'Jenny','midterm':85,'final':80},{'name':'Nate','midterm':10,'final':30}]
df = pd.DataFrame(friend_dict_list,columns = ['name','midterm','final'])
df

#%%
df2 = pd.DataFrame([['Ben',50,50]],columns =['name','midterm','final'])
df2.head()

#%%
df.append(df2, ignore_index=True)

#%%
student_list =[{'name':'John','major':"Computer Science", 'sex':"male"},{'name':'Nate','major':"Computer Science",'sex':"male"},{'name':'Abraham','major':"Physics",'sex':"male"},{'name':'Brian','major':"Psychology",'sex':"male"},{'name':'Janny','major':"Economics",'sex':"female"},{'name':'Yuna','major':"Economics",'sex':"female"},{'name':'Jeniffer','major':"Computer Science",'sex':"female"},{'name':'Edward','major':"Computer Science",'sex':"male"},{'name':'Zara','major':"Psychology",'sex':"female"},{'name':'Wendy','major':"Economics",'sex':"female"},{'name':'Sera','major':"Psychology",'sex':"female"}]
df = pd.DataFrame(student_list,columns = ['name','major','sex'])
df

#%%
groupby_major = df.groupby('major')

#%%
groupby_major.groups

#%%
for name, group in groupby_major:
    print(name+": "+str(len(group)))
    print(group)
    print()

#%%
df_major_cnt = pd.DataFrame({'count':groupby_major.size()}).reset_index()
df_major_cnt

#%%
groupby_sex = df.groupby('sex')

#%%
for name, group in groupby_sex:
    print(name + ": " + str(len(group)))
    print(group)
    print()

#%%
df_sex_cnt = pd.DataFrame({'count' : groupby_sex.size()}).reset_index()
df_sex_cnt

#%%
student_list = [{'name': 'John', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Nate', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Abraham', 'major': "Physics", 'sex': "male"},
                {'name': 'Brian', 'major': "Psychology", 'sex': "male"},
                {'name': 'Janny', 'major': "Economics", 'sex': "female"},
                {'name': 'Yuna', 'major': "Economics", 'sex': "female"},
                {'name': 'Jeniffer', 'major': "Computer Science", 'sex': "female"},
                {'name': 'Edward', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Zara', 'major': "Psychology", 'sex': "female"},
                {'name': 'Wendy', 'major': "Economics", 'sex': "female"},
                {'name': 'Sera', 'major': "Psychology", 'sex': "female"},
                {'name': 'John', 'major': "Computer Science", 'sex': "male"},
         ]
df = pd.DataFrame(student_list, columns = ['name', 'major', 'sex'])
df

#%%
df.duplicated()

#%%
df = df.drop_duplicates()
df

#%%
student_list = [{'name': 'John', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Nate', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Abraham', 'major': "Physics", 'sex': "male"},
                {'name': 'Brian', 'major': "Psychology", 'sex': "male"},
                {'name': 'Janny', 'major': "Economics", 'sex': "female"},
                {'name': 'Yuna', 'major': "Economics", 'sex': "female"},
                {'name': 'Jeniffer', 'major': "Computer Science", 'sex': "female"},
                {'name': 'Edward', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Zara', 'major': "Psychology", 'sex': "female"},
                {'name': 'Wendy', 'major': "Economics", 'sex': "female"},
                {'name': 'Nate', 'major': None, 'sex': "male"},
                {'name': 'John', 'major': "Computer Science", 'sex': None},
         ]
df = pd.DataFrame(student_list, columns = ['name', 'major', 'sex'])
df

#%%
df.duplicated(['name'])

#%%
df.drop_duplicates(['name'],keep='last')

#%%
school_id_list = [{'name': 'John', 'job': "teacher", 'age': 40},
                {'name': 'Nate', 'job': "teacher", 'age': 35},
                {'name': 'Yuna', 'job': "teacher", 'age': 37},
                {'name': 'Abraham', 'job': "student", 'age': 10},
                {'name': 'Brian', 'job': "student", 'age': 12},
                {'name': 'Janny', 'job': "student", 'age': 11},
                {'name': 'Nate', 'job': "teacher", 'age': None},
                {'name': 'John', 'job': "student", 'age': None}
         ]
df = pd.DataFrame(school_id_list, columns = ['name', 'job', 'age'])
df

#%%
df.info()

#%%
df.isna()

#%%
df.isnull()

#%%
tmp = df
tmp["age"] = tmp["age"].fillna(0)
tmp

#%%
df["age"].fillna(df.groupby("job")["age"].transform("median"),inplace=True)

#%%
df

#%%
job_list = [{'name': 'John', 'job': "teacher"},
                {'name': 'Nate', 'job': "teacher"},
                {'name': 'Fred', 'job': "teacher"},
                {'name': 'Abraham', 'job': "student"},
                {'name': 'Brian', 'job': "student"},
                {'name': 'Janny', 'job': "developer"},
                {'name': 'Nate', 'job': "teacher"},
                {'name': 'Obrian', 'job': "dentist"},
                {'name': 'Yuna', 'job': "teacher"},
                {'name': 'Rob', 'job': "lawyer"},
                {'name': 'Brian', 'job': "student"},
                {'name': 'Matt', 'job': "student"},
                {'name': 'Wendy', 'job': "banker"},
                {'name': 'Edward', 'job': "teacher"},
                {'name': 'Ian', 'job': "teacher"},
                {'name': 'Chris', 'job': "banker"},
                {'name': 'Philip', 'job': "lawyer"},
                {'name': 'Janny', 'job': "basketball player"},
                {'name': 'Gwen', 'job': "teacher"},
                {'name': 'Jessy', 'job': "student"}
         ]
df = pd.DataFrame(job_list, columns = ['name', 'job'])

#%%
print(df.job.unique())

#%%
df.job.value_counts()

#%%
l1 = [{'name': 'John', 'job': "teacher"},
      {'name': 'Nate', 'job': "student"},
      {'name': 'Fred', 'job': "developer"}]

l2 = [{'name': 'Ed', 'job': "dentist"},
      {'name': 'Jack', 'job': "farmer"},
      {'name': 'Ted', 'job': "designer"}]
         
df1 = pd.DataFrame(l1, columns = ['name', 'job'])
df2 = pd.DataFrame(l2, columns = ['name', 'job'])

#%%
frames = [df1,df2]
result = pd.concat(frames,ignore_index=True)
result

#%%
l1 = [{'name':'John','job':"teacher"},{'name':'Nate','job':"student"},{'name':'Fred','job':"developer"}]

l2 = [{'name':'Ed','job':"dentist"},{'name':'Jack','job':"farmer"},{'name':'Ted','job':"designer"}]
df1 = pd.DataFrame(l1, columns =['name','job'])
df2 = pd.DataFrame(l2, columns =['name','job'])
result = df1.append(df2,ignore_index=True)

#%%
result

#%%
l1 = [{'name': 'John', 'job': "teacher"},
      {'name': 'Nate', 'job': "student"},
      {'name': 'Jack', 'job': "developer"}]

l2 = [{'age': 25, 'country': "U.S"},
      {'age': 30, 'country': "U.K"},
      {'age': 45, 'country': "Korea"}]

df1 = pd.DataFrame(l1,columns = ['name','job'])
df2 = pd.DataFrame(l2,columns = ['age','country'])
result = pd.concat([df1,df2],axis=1,ignore_index=True)
result

#%%
label = [1,2,3,4,5]
prediction = [1,2,2,5,5]

comparison = pd.DataFrame({'label':label,'prediction':prediction})
comparison 

#%%
