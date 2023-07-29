#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import numpy as mp
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# # Importing data
# ### Looking through the data and cleaning it to have no nulls, also deciding what columns are relevant

# In[2]:


#import data
df_meta = pd.read_csv('metadata.csv')
df_meta.info(verbose=True,show_counts=True)


# In[3]:


#Cleaning data-- selected relevant columns to our focus
df_mk = df_meta[["DATE","DAYOFWEEK","DAYOFYEAR","WEEKOFYEAR","MONTHOFYEAR","YEAR","HOLIDAYM","WDWMEANTEMP","MKHOURSEMH","WEATHER_WDWPRECIP","EPHOURSEMH","HSHOURSEMH","AKHOURSEMH"]]


# In[4]:


df_mk.info(verbose=True,show_counts=True)


# # Magic Kingdom Rides

# In[5]:


# Big Thunder Mountain
df_btm = pd.read_csv('big_thunder_mtn.csv')
df_btm.dropna()
df_btm = df_btm[df_btm.SPOSTMIN != -999.0]
df_btm = df_btm.groupby('date')['SPOSTMIN'].mean()
df_btm = pd.DataFrame(df_btm).reset_index()
df_btm = df_btm.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_btm["Park"]="MK"
df_btm["Attraction"]="Big Thunder Mountain"
df_btm = pd.merge(left=df_mk,right=df_btm,how="inner",on='DATE')


# In[6]:


# Seven Dwarfs Mine Train
df_7d = pd.read_csv('7_dwarfs_train.csv')
df_7d.dropna()
df_7d = df_7d[df_7d.SPOSTMIN != -999.0]
df_7d = df_7d.groupby('date')['SPOSTMIN'].mean()
df_7d = pd.DataFrame(df_7d).reset_index()
df_7d = df_7d.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_7d["Park"]="MK"
df_7d["Attraction"]="Seven Dwarfs Mine Train"
df_7d = pd.merge(left=df_mk,right=df_7d,how="inner",on='DATE')


# In[7]:


# Splash Mountain
df_splash = pd.read_csv('splash_mountain.csv')
df_splash.dropna()
df_splash = df_splash[df_splash.SPOSTMIN != -999.0]
df_splash = df_splash.groupby('date')['SPOSTMIN'].mean()
df_splash = pd.DataFrame(df_splash).reset_index()
df_splash = df_splash.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_splash["Park"]="MK"
df_splash["Attraction"]="Splash Mountain"
df_splash = pd.merge(left=df_mk,right=df_splash,how="inner",on='DATE')


# In[8]:


# Peter Pan's Flight
df_ppf = pd.read_csv('peter_pan_s_flight.csv')
df_ppf.dropna()
df_ppf = df_ppf[df_ppf.SPOSTMIN != -999.0]
df_ppf = df_ppf.groupby('date')['SPOSTMIN'].mean()
df_ppf = pd.DataFrame(df_ppf).reset_index()
df_ppf = df_ppf.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_ppf["Park"]="MK"
df_ppf["Attraction"]="Peter Pan's Flight"
df_ppf = pd.merge(left=df_mk,right=df_ppf,how="inner",on='DATE')


# In[9]:


# Space Mountain
df_space = pd.read_csv('space_mountain.csv')
df_space.dropna()
df_space = df_space[df_space.SPOSTMIN != -999.0]
df_space = df_space.groupby('date')['SPOSTMIN'].mean()
df_space = pd.DataFrame(df_space).reset_index()
df_space = df_space.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_space["Park"]="MK"
df_space["Attraction"]="Space Mountain"
df_space = pd.merge(left=df_mk,right=df_space,how="inner",on='DATE')


# # Epcot

# In[10]:


# Soarin
df_soar = pd.read_csv('soarin.csv')
df_soar.dropna()
df_soar = df_soar[df_soar.SPOSTMIN != -999.0]
df_soar = df_soar.groupby('date')['SPOSTMIN'].mean()
df_soar = pd.DataFrame(df_soar).reset_index()
df_soar = df_soar.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_soar["Park"]="EP"
df_soar["Attraction"]="Soarin"
df_soar = pd.merge(left=df_mk,right=df_soar,how="inner",on='DATE')


# In[11]:


# Spaceship Earth
df_spaceship = pd.read_csv('spaceship_earth.csv')
df_spaceship.dropna()
df_spaceship = df_spaceship[df_spaceship.SPOSTMIN != -999.0]
df_spaceship = df_spaceship.groupby('date')['SPOSTMIN'].mean()
df_spaceship = pd.DataFrame(df_spaceship).reset_index()
df_spaceship = df_spaceship.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_spaceship["Park"]="EP"
df_spaceship["Attraction"]="Spaceship Earth"
df_spaceship = pd.merge(left=df_mk,right=df_spaceship,how="inner",on='DATE')


# # Hollywood Studios

# In[12]:


# Alien Swirling Saucers
df_alien = pd.read_csv('alien_saucers.csv')
df_alien.dropna()
df_alien = df_alien[df_alien.SPOSTMIN != -999.0]
df_alien = df_alien.groupby('date')['SPOSTMIN'].mean()
df_alien = pd.DataFrame(df_alien).reset_index()
df_alien = df_alien.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_alien["Park"]="HS"
df_alien["Attraction"]="Alien Swirling Saucers"
df_alien = pd.merge(left=df_mk,right=df_alien,how="inner",on='DATE')


# In[13]:


# Rock n Rollercoaster
df_rockn = pd.read_csv('rock_n_rollercoaster.csv')
df_rockn.dropna()
df_rockn = df_rockn[df_rockn.SPOSTMIN != -999.0]
df_rockn = df_rockn.groupby('date')['SPOSTMIN'].mean()
df_rockn = pd.DataFrame(df_rockn).reset_index()
df_rockn = df_rockn.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_rockn["Park"]="HS"
df_rockn["Attraction"]="Rock n Rollercoaster"
df_rockn = pd.merge(left=df_mk,right=df_rockn,how="inner",on='DATE')


# In[14]:


# Slinky Dog Dash
df_slinky = pd.read_csv('slinky_dog.csv')
df_slinky.dropna()
df_slinky = df_slinky[df_slinky.SPOSTMIN != -999.0]
df_slinky = df_slinky.groupby('date')['SPOSTMIN'].mean()
df_slinky = pd.DataFrame(df_slinky).reset_index()
df_slinky = df_slinky.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_slinky["Park"]="HS"
df_slinky["Attraction"]="Slinky Dog Dash"
df_slinky = pd.merge(left=df_mk,right=df_slinky,how="inner",on='DATE')


# In[15]:


# Toy Story Mania
df_tsm = pd.read_csv('toy_story_mania.csv')
df_tsm.dropna()
df_tsm = df_tsm[df_tsm.SPOSTMIN != -999.0]
df_tsm = df_tsm.groupby('date')['SPOSTMIN'].mean()
df_tsm = pd.DataFrame(df_tsm).reset_index()
df_tsm = df_tsm.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_tsm["Park"]="HS"
df_tsm["Attraction"]="Toy Story Mania"
df_tsm = pd.merge(left=df_mk,right=df_tsm,how="inner",on='DATE')


# # Animal Kingdom

# In[16]:


# Avatar Flight of Passage
df_avatar = pd.read_csv('flight_of_passage.csv')
df_avatar.dropna()
df_avatar = df_avatar[df_avatar.SPOSTMIN != -999.0]
df_avatar = df_avatar.groupby('date')['SPOSTMIN'].mean()
df_avatar = pd.DataFrame(df_avatar).reset_index()
df_avatar = df_avatar.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_avatar["Park"]="AK"
df_avatar["Attraction"]="Avatar"
df_avatar = pd.merge(left=df_mk,right=df_avatar,how="inner",on='DATE')


# In[17]:


# Dinosaur
df_dino = pd.read_csv('dinosaur.csv')
df_dino.dropna()
df_dino = df_dino[df_dino.SPOSTMIN != -999.0]
df_dino = df_dino.groupby('date')['SPOSTMIN'].mean()
df_dino = pd.DataFrame(df_dino).reset_index()
df_dino = df_dino.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_dino["Park"]="AK"
df_dino["Attraction"]="Dinosaur"
df_dino = pd.merge(left=df_mk,right=df_dino,how="inner",on='DATE')


# In[18]:


# Expedition Everest
df_expe = pd.read_csv('expedition_everest.csv')
df_expe.dropna()
df_expe = df_expe[df_expe.SPOSTMIN != -999.0]
df_expe = df_expe.groupby('date')['SPOSTMIN'].mean()
df_expe = pd.DataFrame(df_expe).reset_index()
df_expe = df_expe.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_expe["Park"]="AK"
df_expe["Attraction"]="Expedition Everest"
df_expe = pd.merge(left=df_mk,right=df_expe,how="inner",on='DATE')


# In[19]:


# Kilimanjaro safari
df_kili = pd.read_csv('kilimanjaro_safaris.csv')
df_kili.dropna()
df_kili = df_kili[df_kili.SPOSTMIN != -999.0]
df_kili = df_kili.groupby('date')['SPOSTMIN'].mean()
df_kili = pd.DataFrame(df_kili).reset_index()
df_kili = df_kili.rename(columns={"date":"DATE","SPOSTMIN":"WaitTime"})
df_kili["Park"]="AK"
df_kili["Attraction"]="Kilimanjaro Safari"
df_kili = pd.merge(left=df_mk,right=df_kili,how="inner",on='DATE')


# ## Concat attraction dataframes into a main set

# In[20]:


df_main=pd.concat([df_btm,df_7d,df_splash,df_ppf,df_space,df_soar,
                   df_spaceship,df_alien,df_rockn,df_slinky,
                   df_tsm,df_avatar,df_dino,df_kili,df_expe])
df_main.dropna()
df_main.info(verbose=True)


# In[21]:


OUTPUT = df_main[['DATE','Attraction','Park','WaitTime','HOLIDAYM','DAYOFWEEK','DAYOFYEAR','WEEKOFYEAR','MONTHOFYEAR','WDWMEANTEMP']]
OUTPUT.sample(5)


# ## Question 1: How much does a holiday impact that day and surrounding days’ wait times?

# In[22]:


a = df_main.groupby(['HOLIDAYM'])['WaitTime'].mean()
df_holiday = pd.DataFrame(a).reset_index()
df_holiday


# In[23]:


df_holiday.plot(x='HOLIDAYM',y='WaitTime')


# In[38]:


with sns.color_palette("magma"):
    sns.barplot(data=df_holiday, x="HOLIDAYM", y="WaitTime").set_ylim(40,70)


# ## Question 2: How did COVID affect wait times?

# In[25]:


b = df_main.groupby(['YEAR'])['WaitTime'].mean()
df_yr = pd.DataFrame(b).reset_index()
df_yr


# In[26]:


df_yr.plot(x='YEAR',y='WaitTime')


# In[41]:


with sns.color_palette("magma"):
    sns.barplot(data=df_yr, x="YEAR", y="WaitTime").set_ylim(30,70)


# ## Question 3: What is the ideal month, day of week, and day of the year for each park based on wait times?

# In[55]:


month = df_main.groupby(['Park','MONTHOFYEAR'])['WaitTime'].mean()
df_month = pd.DataFrame(month).reset_index()
df_month.sort_values(by=['WaitTime'])


# In[40]:


day = df_main.groupby(['Park','DAYOFWEEK'])['WaitTime'].mean()
df_day = pd.DataFrame(day).reset_index()
df_day.sort_values(by=['WaitTime'])
# Some parks, not much of a time difference in day of week (see Epcot), max time difference is in Magic Kingdom 
# where day 1 and 7 have 10 min difference


# In[30]:


best = df_main.groupby(['Park','DAYOFYEAR'])['WaitTime'].mean()
df_best = pd.DataFrame(best).reset_index()
df_best[df_best['Park']=="EP"].sort_values(by=['WaitTime'])
# Epcot's best: 251
# Epcot's worst: 364


# In[31]:


df_best[df_best['Park']=="MK"].sort_values(by=['WaitTime'])
# MK best: 251
# MK worst: 364


# In[32]:


df_best[df_best['Park']=="AK"].sort_values(by=['WaitTime'])
# AK best: 253
# AK worst: 363


# In[33]:


df_best[df_best['Park']=="HS"].sort_values(by=['WaitTime'])
# HS best: 242
# HS worst: 362


# In[34]:


rides = df_main.groupby(['Attraction'])['WaitTime'].mean()
df_rides = pd.DataFrame(rides).reset_index()
df_rides.sort_values(by=['WaitTime'])


# ## Question 4: Are there any strong correlations between the weather, hours of the parks, holiday proximity, or other variables available in the data and wait time?

# In[48]:


corr = df_main.corr()
corr.style.background_gradient(cmap='Oranges')


# In[54]:


fig, ax = plt.subplots()
sns.heatmap(df_main.corr(method='pearson'), fmt='.4f', 
            cmap=plt.get_cmap('Oranges'), cbar=False, ax=ax)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0.3)
plt.savefig('result.png')


# Results: 
# -Holidays have large impact on wait times.
# -COVID didn’t change wait times much.
# -The optimal time to visit Disney is early September
# -No major correlations in variables to wait times.
