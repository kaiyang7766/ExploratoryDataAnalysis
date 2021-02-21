# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:31:58 2021

@author: Ang Kai Yang
"""
#Pipeline functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime
import calendar
def definetimerange (data,startTime,endTime):
    global time_range
    time_range=data[(data['Time']>startTime)&(data['Time']<endTime)]
def normalizetime (data,startTime):
    global cleaned_time
    cleaned_time=(data['Timestamp']-calendar.timegm(datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S.000").utctimetuple())*1000)/1000
def normalizepressure (data):
    global cleaned_pressure
    cleaned_pressure=data['Bar_Pressure']/10
    
def resizesample(data,frequency):
  #naming method follows "'data'_resized"
  return data.iloc[::frequency, :]

def datapreparation(data, start_time, end_time, resize=1, neednormalizepressure = False):
  #resize the sample if too large, only keep every nth row
  data = resizesample(data,resize)

 #select the rows needed according to start time end time
  data = data[(data['Time']>start_time)&(data['Time']<end_time)]

  #reset index due to duplicated index while merging data
  data = data.reset_index()

  #normalize time
  normalizetime(data,start_time) #cleaned time series is created with column name 'Timestamp'

  #insert new column 'Cleaned Time' into dataset
  data['Cleaned_Time'] = cleaned_time

  #normalise pressure
  if neednormalizepressure == True:
    normalizepressure (data)
    data['Bar_Pressure'] = cleaned_pressure
  return data

def visualisation(data1, data2, name):
  f, axes = plt.subplots(1, 1, figsize=(16,8))
  plt.plot(data1['Cleaned_Time'],data1['Bar_Pressure'],label='S6 Edge')
  if data2 is not None:
    plt.plot(data2['Cleaned_Time'],data2['Bar_Pressure'],label='iPhone 12 Pro')
  plt.title(name)
  plt.legend()
  plt.ylabel('Bar pressure (kPa)')
  plt.xlabel('Time (s)')
  plt.show()

def totalvisualization(data):
    data_idle=data[~data.Mode.str.contains('MRT')]
    data_mrt=data[~data.Mode.str.contains('Idle')]
    plt.figure(figsize=(20,72))
    for i, col in enumerate(['Acc_Lin_X', 'Acc_Lin_Y', 'Acc_Lin_Z', 'Acc_X', 'Acc_Y','Acc_Z', 'Bar_Pressure', 'Gyr_X', 'Gyr_Y', 'Gyr_Z','Loc_Altitude', 'Loc_Latitude', 'Loc_Longitude', 'Mag_X', 'Mag_Y','Mag_Z'],start=1):
        plt.subplot(8,2,i)
        plt.plot(data_mrt['Cleaned_Time'],data_mrt[col],'.y',label='MRT')
        plt.plot(data_idle['Cleaned_Time'],data_idle[col],'.b',label='Idle')
        plt.legend()
        plt.xlabel('Time (s)')
        plt.title(col)
  
def modeChanged(data):
  totalNumberOfModeChanged = 0
  timestampList = [[data['Mode'][0],data['Time'][0],data['Cleaned_Time'][0]]] #list of list
  timeStampLastMode = data['Cleaned_Time'][0]
  durationOfLastMode = 0
  current_mode = data['Mode'][0]
  for i in range(len(data)):
    mode = data['Mode'][i]
    if mode != current_mode:
      totalNumberOfModeChanged += 1
      duration = data['Cleaned_Time'][i] - timeStampLastMode
      timestampList[-1][2] = duration #only after next change of mode we are able to calculate the duration of last mode, without this the mode and duration output will be interchanged
      timestampList.append([mode,data['Time'][i],0]) #0 is just preparation for adding duration in the next loop

      #update new count
      current_mode = mode
      timeStampLastMode = data['Cleaned_Time'][i]
  print("Total number of Mode changed is :",totalNumberOfModeChanged)
  return totalNumberOfModeChanged, timestampList

def findErrorDuration(timestampList):
  errorCount = 0
  for item in timestampList:
    if item[2] < 20:
      errorCount+=1
      print([item[1],item[2]])
  print("Total number of error entries is :",errorCount)
  return errorCount

def findErrorDuration2(timestampList):
  errorCount = 0
  for item in timestampList:
    if item[2] < 32:
      errorCount+=1
      print([item[1],item[2]])
  print("Total number of error entries is :",errorCount)
  return errorCount
