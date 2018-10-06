
# coding: utf-8

# In[1]:


import numpy as np
temp_max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])


# In[2]:


temp_max


# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

months = np.arange(12)

plt.plot(months, temp_max, 'ro')
plt.plot(months, temp_min, 'bo')

plt.xlabel('Month')
plt.ylabel('Min and max temperature')


# In[5]:


from scipy import optimize
def yearly_temps(times, avg, ampl, time_offset):
    return (avg + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))

res_max, cov_max = optimize.curve_fit(yearly_temps, months, temp_max, [20, 10, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months, temp_min, [-40, 20, 0])

print(res_max)
print(res_min)



days = np.linspace(0, 12, num=365)


# plt.figure()

plt.plot(months, temp_max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
# '-': solid line style


plt.plot(months, temp_min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')


plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')

plt.show()


# In[7]:


import pandas as pd

url="https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"
titanic = pd.read_csv(url)


# In[8]:


titanic


# In[9]:



count = titanic['sex'].value_counts()
male_count = count['male']
female_count = count['female']


# In[11]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
labels = 'Male' , 'Female'
sizes = [male_count, female_count]
#explode = (0.00, 0.05)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=60)
ax1.axis('equal') 
plt.show()


# In[13]:


#Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


#2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
grp = titanic.groupby(["age", "sex"])
grp_unstack = grp.mean()['fare']..unstack()


# In[14]:


grp_unstack


# In[18]:


d1 = grp_unstack.male.values # Mean Fare for all Male passengers by age
d2 = grp_unstack.female.values # Mean Fare for all Female passengers by age
d3 = grp_unstack.index.values # Age - Making Asge as Index

plt.figure(figsize=(15, 8))

plt.scatter(d3, d1, label='male', alpha=0.8,   cmap='viridis')
plt.scatter(d3, d2, label='female', alpha=0.8,   cmap='viridis')


#plt.scatter(d1, d3, label='male', alpha=0.8,   cmap='viridis')
#plt.scatter(d2, d3, label='female', alpha=0.8,   cmap='viridis')

plt.title('Scatter Plot of Age vs. Fare')

plt.ylabel('Fare Paid By Passenger')
plt.xlabel('Age of Passenger');
plt.legend()

