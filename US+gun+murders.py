
# coding: utf-8

# # IMPORTING ALL PACKAGES

# In[2]:


import pandas as pd
get_ipython().magic('matplotlib inline')


# # IMPORT FILE, CHECK HEAD, CHECK FOR NULLS

# In[3]:


mass_shootings = pd.read_csv('D:/MS/USF/fall 2018/us-mass-shootings-last-50-years/shooting.csv',encoding='latin1')


# In[4]:


mass_shootings.head()


# In[12]:


mass_shootings.isnull().sum()


# In[13]:


mass_shootings[mass_shootings['Summary'].isnull()]


# # EXTRACT YEAR AND MONTH. SAVING THIS CSV.

# In[14]:


mass_shootings.Date = pd.to_datetime(mass_shootings.Date)


# In[15]:


mass_shootings['year'] = mass_shootings.Date.dt.year


# In[16]:


mass_shootings['month'] = mass_shootings.Date.dt.month


# In[17]:


mass_shootings['week'] = mass_shootings.Date.dt.week


# In[18]:


mass_shootings['day'] = mass_shootings.Date.dt.weekday_name


# In[19]:


#df['weekday'] = df[['datetime']].apply(lambda x: dt.datetime.strftime(x['datetime'], '%A')


# In[20]:


mass_shootings.tail()


# In[21]:


mass_shootings.to_csv('D:/MS/USF/fall 2018/us-mass-shootings-last-50-years/mass_shootings.csv')


# # YEARWISE FATALITY CHECK

# In[22]:


yearwise = mass_shootings.groupby('year')[['Fatalities']].sum()


# In[23]:


#counts number of rows for every year entry
#mass_shootings.groupby('year')[['Fatalities']].count()


# In[24]:


type(yearwise)


# In[25]:


yearwise


# In[26]:


yearwise.plot(kind='line',title='year wise fatality count',figsize=(10,7))


# ## MONTH WISE FATALITY CHECK

# In[27]:


monthwise = mass_shootings.month.value_counts().sort_index()


# In[28]:


monthwise


# In[29]:


monthwise.plot(kind='bar',title= 'monthwise instance of shootings')


# In[31]:


monthwise_fatalities = mass_shootings.groupby('month')[['Fatalities']].sum()
monthwise_fatalities.plot(kind='bar',title='killings by month')


# In[32]:


monthwise_fatalities['pmf']=monthwise_fatalities['Fatalities']/sum(monthwise_fatalities['Fatalities'])


# In[33]:


monthwise_fatalities['pmf'].plot(kind='bar',title  = 'monthwise killings')


# # WEEK WISE ANALYSIS

# In[34]:


weekwise = mass_shootings.groupby('week')[['Fatalities']].sum()

weekwise


# In[35]:


weekwise.plot(kind='bar',figsize=(15,7))


# #weekwise['week'] = weekwise.index
# 
# weekwise.reset_index(level=0,inplace=True)
# weekwise

# test = weekwise.filter(['week','Fatalities'],axis=1)

# test.groupby('week')['Fatalities'].sum().hist(cumulative=True, normed=1, bins=100)

# # DAY WISE ANALYSIS

# In[36]:


daywise=mass_shootings.groupby('day')[['Fatalities']].sum()


# In[37]:


daywise.plot(kind='bar')


# ## SEX WISE ANALYSIS

# In[38]:


mass_shootings.Gender.value_counts()


# In[39]:


mass_shootings.Gender[mass_shootings.Gender=='M'] = 'Male'


# In[40]:


mass_shootings.Gender.value_counts()


# In[41]:


mass_shootings.head()


# In[42]:


mass_shootings.Gender[mass_shootings.Gender=='M/F'] = 'Male/Female'


# In[43]:


test = mass_shootings.Gender.value_counts()


# In[44]:


test


# In[45]:


test.plot(kind='bar',title= 'Number of shooting instances - sexwise')


# In[46]:


sexwisefatalities = mass_shootings.groupby('Gender')[['Fatalities']].sum()


# In[47]:


sexwisefatalities.plot(kind = 'bar', title = 'sexwise killings comparator')


# In[48]:


sexwisefatalities['pmf'] = (sexwisefatalities.Fatalities) / sum(sexwisefatalities.Fatalities)
sexwisefatalities['pmf'].plot(kind='bar',title='pmf')


# ## RACEWISE ANALYSIS 

# In[49]:


mass_shootings.Race.value_counts()


# In[50]:


mass_shootings.Race[mass_shootings.Race == 'White American or European American']= 'White'
mass_shootings.Race[mass_shootings.Race == 'white']= 'White'
#mass_shootings.Race[mass_shootings.Race == 'white']= 'White'
mass_shootings.Race[mass_shootings.Race == 'Native American or Alaska Native']= 'White'
mass_shootings.Race[mass_shootings.Race == 'White American or European American/Some other Race']= 'White'



mass_shootings.Race[mass_shootings.Race == 'Black American or African American']= 'Black'
mass_shootings.Race[mass_shootings.Race == 'black']= 'Black'
mass_shootings.Race[mass_shootings.Race == 'Black American or African American/Unknown']= 'Black'


mass_shootings.Race[mass_shootings.Race == 'Asian American/Some other race']= 'Asian'
mass_shootings.Race[mass_shootings.Race == 'Asian American']= 'Asian'


mass_shootings.Race[mass_shootings.Race == 'Some other race']= 'Unknown'
mass_shootings.Race[mass_shootings.Race == 'Other']= 'Unknown'



# In[51]:


racewise = mass_shootings.Race.value_counts()
racewise


# In[52]:


racewise.plot(kind='bar')


# In[53]:


racewisekillings = mass_shootings.groupby('Race')[['Fatalities']].sum()


# In[54]:


racewisekillings


# In[55]:


racewisekillings.plot(kind='bar')


# In[56]:


racewisekillings['pmf'] = racewisekillings['Fatalities']/sum(racewisekillings['Fatalities'])
racewisekillings['pmf'].plot(kind='bar')


# In[406]:


#racewisekillings.reset_index(inplace=True)


# # MENTAL HEALTH ANALYSIS

# ## LETS CONSIDER KNOWN CASES ONLY (I.E YES, NO OR UNCLEAR)

# In[57]:


mass_shootings['Mental Health Issues'].value_counts()


# In[58]:


mental_health = (mass_shootings['Mental Health Issues'] == 'Yes') | (mass_shootings['Mental Health Issues'] == 'No') | (mass_shootings['Mental Health Issues'] == 'Unclear')


# In[59]:


known_mass_shootings = mass_shootings[mental_health]


# In[60]:


mentalcounts = known_mass_shootings['Mental Health Issues'].value_counts()
mentalcounts


# In[61]:


mentalcounts.plot(kind='bar',title='mental health condition of the mass murderers')


# In[62]:


fatalities_MH = known_mass_shootings.groupby('Mental Health Issues')[['Fatalities']].sum()


# In[63]:


fatalities_MH.plot(kind='bar',title='fatality count based on mental health condition of mass murderer')


# # TESTING CORRELATIONS

# In[72]:


correlation = mass_shootings.filter(['Race','Mental Health Issues','Gender'])
correlation.head()
correlation=pd.get_dummies(correlation)


# In[73]:


correlation


# In[74]:


test=correlation.corr()


# In[75]:



import numpy as np
condition = (test > 0.20) | (test < -0.20)
condition
test[condition]


# In[79]:


correlation = mass_shootings.filter(['Race','Gender'])
correlation.head()
correlation=pd.get_dummies(correlation)
test=correlation.corr()

import numpy as np
condition = (test > 0.15) | (test < -0.15)
condition
test[condition]


# In[80]:


correlation = mass_shootings.filter(['Mental Health Issues','Gender'])
correlation.head()
correlation=pd.get_dummies(correlation)
test=correlation.corr()

import numpy as np
condition = (test > 0.15) | (test < -0.15)
condition
test[condition]


# In[81]:


correlation = mass_shootings.filter(['Mental Health Issues','Race'])
correlation.head()
correlation=pd.get_dummies(correlation)
test=correlation.corr()

import numpy as np
condition = (test > 0.15) | (test < -0.15)
condition
test[condition]


# In[539]:


from pygeocoder import Geocoder
rresults = Geocoder.reverse_geocode(mass_shootings['Latitude'][50], mass_shootings['Longitude'][50])


# In[540]:


rresults.city


# In[528]:


mass_shootings['Latitude']= mass_shootings['Latitude'].astype(float)
mass_shootings['Longitude']= mass_shootings['Longitude'].astype(float)


# # Learnings
# • There is a timeline on the tableau dashboard (https://us-east-1.online.tableau.com/t/tejbirsworkspace/views/USMassshootings/Finaldashboard?:embed=y&:showAppBanner=false&:showShareOptions=true&:display_count=no&:showVizHome=no#3) that gives us the number of injured and killed people over the years. 
# It is clearly seen that from 2010 onwards, there is a significant rise in the number of people affected by these activities. The deadliest years have been 2015 with 226 and 2014 with 193 reported dead people.
# 
# • Visualized mass shootings on US map-
# https://us-east-1.online.tableau.com/#/site/tejbirsworkspace/views/USMassshootings/Locationwisefatalities?:iid=10
# 
# From the map we can see that the states on east coast generally seem to be more affected by such attacks
# 
# • For the known values of gender and race, there is no real correlation. The  most interesting correlation coefficient is 0.19 for gender = male and race = black
# 
# • For the known values of gender and mental health issues, the  most interesting correlation coefficient is 0.16 for gender = male and mental health issues = yes
# 
# • For the known values of race and mental health issues, the  most interesting correlation coefficient is 0.31 for race = white and mental health issues = yes
# 
# •The deadliest day is Sunday which is closely followed by Wednesday. 250+ people lost their lives on each of these days.
#  The deadliest week is 23 with close to 80 killings being reported. This is closely followed by week 16 and 39 which reported 70  killings.
# The deadliest month is February with close to 175 reported dead in more than 50 different shootings. October and December also account for more than 150 killings each that take up 3rd and 2nd ranking in deadly months list.
# 
# • Of the known shooter mental conditions, more than 100 shooters had some mental health issue with them. These people ended up taking more than 600 lives. Most eye catching relevation has been the corelation of shooters with race = white and mental illness = yes with a coefficient of ~0.32
# 
# • More than 140 shooters have belonged to the white race.They killed almost 800 people (> 50% of total killings).
# 
# • Men have been involved in more than 90% of the total killings recorded killing more than 1200 people in the process.
# 
# 
# 
