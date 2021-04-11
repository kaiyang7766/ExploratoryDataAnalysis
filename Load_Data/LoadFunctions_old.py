# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:31:58 2021

@author: Ang Kai Yang
"""
import matplotlib.pyplot as plt
#Pipeline functions
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
      
      #insert end time for previous mode as current timestamp
      timestampList[-1].append(data['Time'][i])

      #insert new entries
      timestampList.append([mode,data['Time'][i],0]) #0 is just preparation for adding duration in the next loop

      #update new count
      current_mode = mode
      timeStampLastMode = data['Cleaned_Time'][i]
#  print("Total number of Mode changed is :",totalNumberOfModeChanged)
  return timestampList

def findErrorDuration(timestampList):
  errorCount = 0
  global errorList
  errorList = []
  for item in timestampList:
    if item[2] < 20:
      errorCount+=1
      errorList.append([item[1],item[2]])
  print("Total number of error entries is :",errorCount)
  print(errorList)
  return errorCount, errorList

def findErrorDuration2(timestampList):
  errorCount = 0
  for item in timestampList:
    if item[2] < 32:
      errorCount+=1
      print([item[1],item[2]])
  print("Total number of error entries is :",errorCount)
  return errorCount

def removeBackwardTimestampError(modeList):
  newModeList = [modeList[0]]
  removeList = []
  currentTime = modeList[0][1]
  modeList.pop(0)
  while modeList != []:
    if modeList[0][1] <= currentTime:
      removeList.append(modeList[0])
      modeList.remove(modeList[0])
    else:
      newModeList.append(modeList[0])
      currentTime = modeList[0][1]
      newModeList[-2][3] = currentTime
      modeList.remove(modeList[0])
  return newModeList

import datetime
def recalculateDuration(modelist):
  for i in range(len(modelist)-1):
    if isinstance(modelist[0][1],str) == True:
      endtime = datetime.datetime.strptime(modelist[i][3], '%Y-%m-%d %H:%M:%S')
      starttime = datetime.datetime.strptime(modelist[i][1], '%Y-%m-%d %H:%M:%S')
    else:
      endtime = modelist[i][3]
      starttime = modelist[i][1]
    time = endtime - starttime
    modelist[i][2] = time.total_seconds()
  return modelist

def removeErrorDuration(modelist):
  newlist = []
  for i in range(len(modelist)-1):
    if modelist[i][2] < 5: #less than 5 seconds
      pass
    else:
      newlist.append(modelist[i])
  newlist.append(modelist[-1]) #add last item in
  return newlist

def selectTimestampKey(modelist):
  newlist = []
  for i in modelist:
    newlist.append(i[1])
  return newlist

def findRepetitiveMode(modelist):
  repetitivelist = []
  mode = modelist[0][0]
  for i in range(1,len(modelist)):
    if modelist[i][0] == mode:
      print("Repetitve mode error at ",modelist[i])
      repetitivelist.append(modelist[i])
    else:
      mode = modelist[i][0]
  return repetitivelist

def removeRepetitiveMode(modelist, repetitivelist):
  newlist = []
  print("remove starting here!")
  for i in range(len(modelist)-1):
    if modelist[i] in repetitivelist:
      print(modelist[i],"is going to be removed")
      newlist[-1][3] = modelist[i][3]
    else:
      newlist.append(modelist[i])
#  print("newlist length is:", len(newlist))
  return newlist

def checkTimestampIsString(modelist):
  newlist = []
  if isinstance(modelist[0][1], str) == False:
    for i in range(len(modelist)-1):
      modelist[i][1] = str(modelist[i][1])
      modelist[i][3] = str(modelist[i][3])
      newlist.append(modelist[i])
    newlist.append(modelist[-1])
    newlist[-1][1] = str(newlist[-1][1])
    return newlist
  return modelist

def errorRemovingPipeline(data):
  modeChangedList = modeChanged(data)
  print("The length after modeChanged is :", len(modeChangedList))

  newModeChangedList = removeBackwardTimestampError(modeChangedList)
  print("The length after removeBackwardTimestampError is :", len(newModeChangedList))

  recalculatedModeList = recalculateDuration(newModeChangedList)
  print("The length after first recalculated is :", len(recalculatedModeList))

  recalculatedAndRemovedList = removeErrorDuration(recalculatedModeList)

  repetitiveList = findRepetitiveMode(recalculatedAndRemovedList)
  if repetitiveList != []:
    recalculatedAndRemovedList = removeRepetitiveMode(recalculatedAndRemovedList, repetitiveList)

  print("The length after recalculated and repetitive mode removed is :", len(recalculatedAndRemovedList))
  finalList = checkTimestampIsString(recalculatedAndRemovedList)

  finalList[-1].append('0')

  return finalList

def appendStation(modelist,stationlist):
  tempStationList = stationlist[:] #copy without referencing, if not stationlist will get pop and cannot be reused
  for item in modelist:
    if item[0] == "Idle" or item[0] == "PMD": #put PMD because TE line got PMD as Idle
      print(tempStationList[0])
      item.append(tempStationList[0])
      tempStationList.pop(0)
    else:
      item.append("Moving")
  return modelist

def addStationToDf(data,modelist):
  data['Station'] = '0'
  while modelist != []:
    for i in range(len(data['Time'])):
      if str(data['Time'][i]) == modelist[0][1]:
        data['Station'][i] = modelist[0][4]
        print(data['Station'][i],'is added!!!')
        modelist.pop(0)
        break
  return data

def fillEmptyStationToDf(data):
  temp = data['Station'][0]
  for i in range(len(data['Station'])):
    if data['Station'][i] != '0':
      temp = data['Station'][i]
    else:
      data['Station'][i] = temp
  return data

#combine 2 functions together
def modifyColumnStation(data,modelist):
  data1 = addStationToDf(data,modelist)
  print("add station done!!!")
  data2 = fillEmptyStationToDf(data1)
  print("fill empty done!!!")
  return data2
