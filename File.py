import json
import os
import sys
import time
import csv
import pandas as pd
import crontab

# get the current time
now = time.time()
timestart = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This cronjob program started running at: ', timestart)

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# create a new dictionary with dummy data
health_data = pd.read_json('https://health.data.ny.gov/resource/9ma3-vsuk.json')
healh_data

# save data to local csv file
covid_data.to_csv('Data/health_data.csv', index = None )

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))


# time end
now = time.time()
endTime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This program started running at: ', endTime)