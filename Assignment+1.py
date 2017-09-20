
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import datetime


# In[2]:

talks_df = pd.read_csv("updated_tedtalks.csv", encoding = "ISO-8859-1")
print(talks_df.head())


# # Problem 1
# First, we want you to run a few basic stats.  For the comments and Views columns, calculate the average and standard deviation, as well as find the entry with the most comments and views.  (A package that you can start with is called 

# In[3]:

talks_df["comments"].describe()


# ## Comments
# Mean: 97.68 
# Std Dev: 117.37

# In[4]:

talks_df['comments'].max()

#talks_df['comments'].idxmax()


# ## Views
# 

# In[5]:

talks_df["views"].describe()


# In[6]:

talks_df['views'].max()


# # Problem 2
# Now, go to the Date column, and extract the months, and reorganize the data accordingly.  For example, from March_12, you would extract March, and restructure based off of that. 
# 

# In[23]:

#a = '12-May'
#dateee = datetime.datetime.strptime(a,"%d-%m")
calendar.month_name[3]
talks_df.sort()


# # Problem 3
# Delete columns ID, Themes, and Related Videos.
# 

# In[8]:

talks_df.drop("id",1, inplace = True)

talks_df.head()


# In[9]:

talks_df.drop('id.1',1,inplace = True)
talks_df.head()


# In[10]:

talks_df.drop('related_themes',1,inplace = True)
talks_df.head()


# In[11]:

talks_df.drop('related_videos',1,inplace = True)
talks_df.head()


# We want you to organize the data by these three common tags: Disease, Business, Entertainment.
# For each Tag, make a column that gives a BOOLEAN output to indicate whether the tag is present in a certain entry.  For instance if the tag was [“Business”, “Arts”, “Health”, “Food”] you would have three columns in the order of False, True, False.
# Make a separate data frame that only has entries with Business and Entertainment as the tags.  
# For each Tag, find the Mean, Median, and Mode for comments.
# 

# In[12]:

#talks_df['tags'] = np.where(talks_df['related_tags']=='Entertainment','True','False')
talks_df['Entertainment']= talks_df['related_tags'].str.contains("Entertainment")
talks_df['Business']= talks_df['related_tags'].str.contains("Busines")
talks_df['Disease']= talks_df['related_tags'].str.contains("Disease")
talks_df.head(10)


# Make a separate data frame that only has entries with Business and Entertainment as the tags.  
# 

# In[13]:

#entertain_df = talks_df['Entertainment'].apply(lambda x: x==True)
#bus_df = talks_df['Business'].apply(lambda x :x==True)

#new_df = entertain_df.append(bus_df)


#talks_df[bus_df]


new_df =talks_df.query('Entertainment==True & Business==True')
new_df

#new_df


# For each Tag, find the Mean, Median, and Mode for comments.
# 

# In[14]:

ent_df = talks_df.query('Entertainment == True')
print(ent_df['comments'].mean())
print(ent_df['comments'].median())
print(ent_df['comments'].mode())


# In[15]:

bus_df = talks_df.query('Business == True')
print(bus_df['comments'].mean())
print(bus_df['comments'].median())
print(bus_df['comments'].mode())


# # Problem 5
# 
# Finally, if you look at the url for any of these videos they are structured like this: http://www.ted.com/talks/scott_fraser_the_problem_with_eyewitness_testimony.html.  If you notice, the title of the TED Talk is the tag that comes after the http://www.ted.com/talks/, and ends wit .html. We want you to make a new column where the title is used to make a new column for url links.  A helpful hint is work with the functions offered under the strings package, i.e. string.contain, string.replace etc. 

# In[22]:

#title_str = talks_df['title'].replace(" ", "_")


talks_df['url']= talks_df['title']



talks_df['url']=talks_df['url'].str.replace(": ","_")

talks_df

talks_df['url']= "http://www.ted.com/talks/" + talks_df['url'] +".html"
talks_df


#talks_df['url']=talks_df.string

#talks_df['url'] = 

