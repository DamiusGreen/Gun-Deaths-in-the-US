
# coding: utf-8

# In[133]:


import csv
import datetime

f = open("guns.csv","r")
data = list(csv.reader(f))
headers = data[1:]


# In[134]:


years = [items[1] for items in headers]
year_counts = {}
for item in years:
    if item not in year_counts:
        year_counts[item] = 1
    else:
        year_counts[item] += 1
#print(year_counts)


# 
# dates = [datetime.datetime(year = int(item[1]), month = int(item[2]), day = 1) for item in headers]
# date_counts = {}
# for date in dates:
#     if date not in date_counts:
#         date_counts[date] = 1
#     else:
#         date_counts[date] += 1
# #print(date_counts)

# In[135]:


total_sex = [sex[5] for sex in headers]
sex_counts = {}
for sex in total_sex:
    if sex not in sex_counts:
        sex_counts[sex] = 1
    sex_counts[sex] += 1
    
total_race = [race[7] for race in headers]
race_counts = {}
for race in total_race:
    if race not in race_counts:
        race_counts[race] = 1
    race_counts[race] += 1
    
print(sex_counts)
print(race_counts)


# So far we've covered importing the guns.csv data, removing the headers from that data. We've counted gun deaths by year, explored gun deaths by month and year using the datetime module, and we've sorted our data gun deaths by race and sex.
# 
# 

# In[136]:


with open("census.csv","r") as fi:
    census = list(csv.reader(fi))
print(census)


# In[137]:


mapping = {'Native American/Native Alaskan': 3739506 + 674625, 
           'Black': 40250635, 
           'White': 197318956, 
           'Asian/Pacific Islander': 15159516, 
           'Hispanic': 44618105
          }
race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000
print(race_per_hundredk)


# intents = [intent[3] for intent in data]
# homicide_race_counts = {}
# for i, race in enumerate(total_race):
#     if race not in homicide_race_counts:
#         homicide_race_counts[race] = 0
#     if intents[i] == "Homicide":
#         homicide_race_counts[race] += 1
# #print(homicide_race_counts)
# 
# race_per_hundredk = {}
# for k,v in homicide_race_counts.items():
#     race_per_hundredk[k] = (v / mapping[k]) * 100000
# print(race_per_hundredk)
#         

# In[139]:


intents = [intent[3] for intent in data]
homicide_race_counts = {}
for i, race in enumerate(total_race):
    if race in homicide_race_counts:
        if intents[i] == "Homicide":
            homicide_race_counts[race] += 1
    else:
        homicide_race_counts[race] = 0
        
race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000
print(race_per_hundredk)
        
#print(homicide_race_counts)

