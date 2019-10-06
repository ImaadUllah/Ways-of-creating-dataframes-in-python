#!/usr/bin/env python
# coding: utf-8

# # Imaad Ullah
# # Email: imaad3358@gmail.com

# # Methods of Creating DataFrames in Python

# In[59]:


import pandas as pd


# ## Method 1: Creating Pandas DataFrame from lists of lists.

# In[60]:


lists = [['Inayat', 54, 60000],['Imaad', 24, 0],['Atta', 22, 35000],
         ['Kaleem', 15, 0],['Zaki', 14, 0],['Basit', 13, 0],
         ['Numan', 12, 0],['Hazqeel', 3, 0],['Aarfeen', 3, 0],
         ['Yaseen', 1, 0],['Aaiza', 0.5, 0]]


# In[72]:


method1_df = pd.DataFrame(data=lists, columns=['Name', 'Age', 'Salary'])
method1_df


# ## Method 2: Creating DataFrame from dict of narray/lists

# In[74]:


r_dic = {'Name': ['Inayat', 'Imaad', 'Atta', 'Kaleem'],
        'Age': [54, 24, 22, 15, ],
        'Salary': [60000, 0, 35000, 0]}


# In[73]:


method2_df = pd.DataFrame(r_dic)
method2_df


# In[ ]:





# In[76]:


raw_dic = {'Outlook':['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']
           ,'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
           ,'Humidity': ['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High']
           ,'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Strong']
           ,'Play': ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']}


# In[77]:


method2_df2 = pd.DataFrame(raw_dic)
method2_df2


# In[ ]:





# ## Method 3: Creating Dataframe from list of dicts

# In[33]:


rdl = [{'Name': 'Inayat', 'Age': 54, 'Salary': 60000},
      {'Age': 24, 'Name': 'Imaad', 'Salary': 0},
      {'Salary': 35000, 'Name': 'Atta', 'Age': 22}]


# In[78]:


method3_df = pd.DataFrame(rdl)
method3_df


# In[ ]:





# ## Method 4: Creating DataFrame using zip() function.

# In[79]:


names = ['Inayat', 'Imaad', 'Atta']
ages = [54, 24, 22]
salaries = [60000, 0, 35000]
zzip = zip(names, ages)
zzip
l = list(zzip)
l


# In[81]:


method4_df = pd.DataFrame(l, columns=['Names', 'Ages'])
method4_df


# ## Method 5: Creating DataFrame from Dictionaries of series.

# In[55]:


dic = {'Name': pd.Series(['Inayat', 'Imaad', 'Atta']),
      'Age': pd.Series([54, 24, 22]),
      'Salaries': pd.Series([60000,0,35000])}


# In[82]:


method5_df = pd.DataFrame(dic)
method5_df


# In[ ]:





# ## Method 6: Using lists in dictionary to create dataframe

# In[101]:


names = ['Imaad', 'Aimal', 'Hasnain', 'Tariq']
degs = ['MS Data Science', 'MS Political Science', 'Mechanical Engineering', 'BBA']
scores = [85, 79, 92, 75]
dic = {'Names': names, 'Degrees': degs, 'Scores': scores}
method6_df = pd.DataFrame(dic)
method6_df


# In[84]:


df = pd.DataFrame()
print(df)


# In[88]:


lst = [1,2,3,4,5,6,7,8,9]
dff = pd.DataFrame(lst, columns=['Numbers'])
dff


# In[ ]:





# In[95]:


test_batsmen = ['Virat Kohli', 'Steve Smith', 'Kane Williamson', 'Joe Root', 'David Warner']
odi_batsmen = ['Virat Kohli', 'Rohit Sharma', 'Joe Root', 'David Warner', 'Babar Azam']
t20_batsmen = ['Babar Azam', 'Aaron Finch', 'Colin Munro', 'Lokish Rahul', 'Fakhar Zaman']

ranking_batsmen = {'Tests': test_batsmen,
                  'ODIs': odi_batsmen,
                  'T20s': t20_batsmen}
index = 1


# In[100]:


batsmen_ranking_df = pd.DataFrame(ranking_batsmen, index=['1','2','3','4','5'])
batsmen_ranking_df

