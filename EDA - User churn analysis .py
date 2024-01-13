#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import packages for data manipulation
import pandas as pd
import numpy as np


# In[2]:


# Load dataset into dataframe
df = pd.read_csv('waze_dataset.csv')


# In[3]:


#inspecting the data set for missing values 
df.head(10)


# In[4]:


#analysing the data summary (rows , columns , and thier data types)
df.info()


# In[5]:


#Isolate rows with null values 
null_values = df['label'].isnull()
null_df = df[null_values]
#Display summary stats of rows with null values
null_df.describe()


# In[6]:


# Isolate rows without null values
not_null_df = df[df['label'].notnull()]
# Display summary stats of rows without null values
not_null_df.describe()


# In[7]:


#Comparing summary statistics of the observations with missing retention labels with those that aren't missing any values reveals nothing remarkable. The means and standard deviations are fairly consistent between the two groups.
#Next, check the two populations with respect to the device variable.
# Get count of null values by device
null_df['device'].value_counts()


# In[8]:


# Calculate % of iPhone nulls and Android nulls
null_df['device'].value_counts(normalize=True)


# In[9]:


# Calculate % of iPhone users and Android users in full dataset
df['device'].value_counts(normalize=True)


# In[10]:


"""The percentage of missing values by each device is consistent with their representation in the data overall.

There is nothing to suggest a non-random cause of the missing data."""


# In[11]:


# Calculate counts of churned vs. retained
print(df['label'].value_counts())
print(df['label'].value_counts(normalize=True))


# In[12]:


"""This dataset contains 82% retained users and 18% churned users."""


# In[13]:


# Calculate median values of all columns for churned and retained users
df.groupby('label').median(numeric_only=True)


# In[14]:


# Group data by `label` and calculate the medians
medians_by_label = df.groupby('label').median(numeric_only=True)
print('Median kilometers per drive:')
# Divide the median distance by median number of drives
medians_by_label['driven_km_drives'] / medians_by_label['drives']


# In[15]:


# Divide the median distance by median number of driving days
print('Median kilometers per driving day:')
medians_by_label['driven_km_drives'] / medians_by_label['driving_days']


# In[16]:


# Divide the median number of drives by median number of driving days
print('Median drives per driving day:')
medians_by_label['drives'] / medians_by_label['driving_days']


# In[17]:


# For each label, calculate the number of Android users and iPhone users
df.groupby(['label', 'device']).size()


# In[18]:


# For each label, calculate the percentage of Android users and iPhone users
df.groupby('label')['device'].value_counts(normalize=True)


# In[28]:


import matplotlib.pyplot as plt 
import seaborn as sns


# In[31]:


def plot_histogram(column_str, median_text=True, **kwargs):    # **kwargs = any keyword arguments
                                                             # from the sns.histplot() function
    median=round(df[column_str].median(), 1)
    plt.figure(figsize=(6,4))
    ax = sns.histplot(x=df[column_str], **kwargs)            # Plot the histogram
    plt.axvline(median, color='red', linestyle='--')         # Plot the median line
    if median_text==True:                                    # Add median text unless set to False
        ax.text(0.25, 0.85, f'median={median}', color='green',
            ha='left', va='top', transform=ax.transAxes)
    else:
        print('Median:', median)
    plt.title(f'{column_str} histogram');
    
def plot_boxplot( column_str, showfliers=True, **kwargs):
    # Create the boxplot
    plt.figure(figsize=(6,4))
    ax = sns.boxplot(x=df[column_str], showfliers=showfliers, **kwargs)
    plt.title(f'{column_str} Boxplot')
    plt.show()


# In[32]:


plot_histogram('sessions')
plot_boxplot('sessions')


# In[33]:


plot_histogram('drives')
plot_boxplot('drives')


# In[34]:


plot_histogram('total_sessions')
plot_boxplot('total_sessions')


# In[35]:


plot_histogram('n_days_after_onboarding')
plot_boxplot('n_days_after_onboarding')


# In[36]:


plot_histogram('driven_km_drives')
plot_boxplot('driven_km_drives')


# In[37]:


plot_histogram('duration_minutes_drives')
plot_boxplot('duration_minutes_drives')


# In[38]:


plot_histogram('activity_days')
plot_boxplot('activity_days')


# In[39]:


plot_histogram('driving_days')
plot_boxplot('driving_days')


# In[40]:


#pie plot needs to be plotted for categorical varibles.
fig = plt.figure(figsize=(4,4))
data=df['device'].value_counts()
plt.pie(data,
        labels=[f'{data.index[0]}: {data.values[0]}',
                f'{data.index[1]}: {data.values[1]}'],
        autopct='%1.1f%%'
        )
plt.title('Users by device');
fig = plt.figure(figsize=(4,4))
data=df['label'].value_counts()
plt.pie(data,
        labels=[f'{data.index[0]}: {data.values[0]}',
                f'{data.index[1]}: {data.values[1]}'],
        autopct='%1.1f%%'
        )
plt.title('Count of retained vs. churned');


# In[41]:


#plotting histogram to visualize relationship between driving_days and active_days
plt.figure(figsize=(12,4))
label=['driving days', 'activity days']
plt.hist([df['driving_days'], df['activity_days']],
         bins=range(0,33),
         label=label)
plt.xlabel('days')
plt.ylabel('count')
plt.legend()
plt.title('driving_days vs. activity_days');


# In[42]:


#calculating max for both the variables
print(df['driving_days'].max())
print(df['activity_days'].max())


# In[43]:


#plot scatter plot for driving_days and activity_days for checking validity.
sns.scatterplot(data=df, x='driving_days', y='activity_days')
plt.title('driving_days vs. activity_days')
plt.plot([0,31], [0,31], color='red', linestyle='--');


# In[44]:


#plotting histogram for retention by device 
plt.figure(figsize=(5,4))
sns.histplot(data=df,
             x='device',
             hue='label',
             multiple='dodge',
             shrink=0.9
             )
plt.title('Retention by device histogram');


# In[45]:


#examining retention by kilometers driven per driving day 
# 1. Create `km_per_driving_day` column
df['km_per_driving_day'] = df['driven_km_drives'] / df['driving_days']

# 2. Call `describe()` on the new column
df['km_per_driving_day'].describe()

# 3. Convert infinite values to zero
df.loc[df['km_per_driving_day']==np.inf, 'km_per_driving_day'] = 0

# 4. Confirm that it worked
df['km_per_driving_day'].describe()


# In[46]:


#plot histogram for new km_per_driving_day
plt.figure(figsize=(12,5))
sns.histplot(data=df,
             x='km_per_driving_day',
             bins=range(0,1201,20),
             hue='label',
             multiple='fill')
plt.ylabel('%', rotation=0)
plt.title('Churn rate by mean km per driving day')


# In[47]:


#plot histogram for churn rate for each number of driving days
plt.figure(figsize=(12,5))
sns.histplot(data=df,
             x='driving_days',
             bins=range(1,32),
             hue='label',
             multiple='fill',
             discrete=True)
plt.ylabel('%', rotation=0)
plt.title('Churn rate per driving day')


# In[48]:


#proportion of sessions that occurred in the last month 
df['percent_sessions_in_last_month'] = df['sessions'] / df['total_sessions']
df['percent_sessions_in_last_month'].median()


# In[49]:


#plot histogram for percent_sessions_in_last_month 
plot_histogram('percent_sessions_in_last_month',
             hue=df['label'],
             multiple='layer',
             median_text=False)


# In[50]:


df['n_days_after_onboarding'].median()


# In[51]:


#plotting histogram for people who had 40% or more of their total sessions in the last month.
data = df.loc[df['percent_sessions_in_last_month']>=0.4]
plt.figure(figsize=(5,3))
sns.histplot(x=data['n_days_after_onboarding'])
plt.title('Num. days after onboarding for users with >=40% sessions in last month');


# In[53]:


#handling outliers 
def outlier(column_name, percentile):
    # Calculate threshold
    threshold = df[column_name].quantile(percentile)
    # Impute threshold for values > than threshold
    df.loc[df[column_name] > threshold, column_name] = threshold

    print('{:>25} | percentile: {} | threshold: {}'.format(column_name, percentile, threshold))


# In[54]:


for column in ['sessions', 'drives', 'total_sessions',
               'driven_km_drives', 'duration_minutes_drives']:
               outlier(column, 0.95)


# In[55]:


df.describe()


# In[ ]:




