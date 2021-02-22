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
import datetime
import calendar

def definetimerange(data,startTime,endTime):
    '''counts the duration in seconds of current timestamp from the start time'''
    global time_range
    time_range=data[(data['Time']>startTime)&(data['Time']<endTime)]
    
def normalizetime(data,startTime):
    '''create a new column in dataframe where duration of current timestamp from start time is calculated in seconds'''
    global cleaned_time
    cleaned_time=(data['Timestamp']-calendar.timegm(datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S.000").utctimetuple())*1000)/1000
    
def normalizepressure(data):
    '''change the unit of Bar_Pressure of data recorded in S6 edge'''
    '''as the Bar_Pressure of S6 edge is recorded in hPa'''
    '''while Bar_Pressure of iphone is recorded in kPa'''
    '''to standardise the unit used'''
    global cleaned_pressure
    cleaned_pressure=data['Bar_Pressure']/10
    
def resizesample(data,frequency):
    '''resize the sample data according to ratio between 2 sets of data'''
    '''S6 edge has far more rows than iphone'''
    '''return every n-th row of data in S6 edge'''
    #naming method follows "'data'_resized"
    return data.iloc[::frequency, :]

def datapreparation(data, start_time, end_time, resize=1, neednormalizepressure = False):
    '''data preprocessing pipeline'''
    '''resize, select start and end time, reset index, get duration, change unit of Bar_Pressure if needed'''
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
    '''visualise 2 sets of data in single plot'''
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
    '''visualise all variables and differentiate between 'MRT' and 'Idle' modes'''
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
    '''get a list of timestamps when 'Mode' changed'''
    '''the list serves as the key to append the 'Station' later'''
    totalNumberOfModeChanged = 0
    timestampList = [[data['Mode'][0],data['Time'][0],data['Cleaned_Time'][0]]] #list of list
    timeStampLastMode = data['Cleaned_Time'][0]
    durationOfLastMode = 0
    current_mode = data['Mode'][0]
    for i in range(len(data)):
        mode = data['Mode'][i]
        #detect when 'Mode' changed
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
    #print("Total number of Mode changed is :",totalNumberOfModeChanged)
    return timestampList

def findErrorDuration(timestampList):
    '''get a list of timestamps where errors occur'''
    '''error is defined as whenever the duration of a 'Mode' is less than 20s'''
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

#not useful anymore
def findErrorDuration2(timestampList):
    '''get a list of timestamps where errors occur'''
    '''error is defined as whenever the duration of a 'Mode' is less than 32s'''
    errorCount = 0
    for item in timestampList:
        if item[2] < 32:
          errorCount+=1
          print([item[1],item[2]])
    print("Total number of error entries is :",errorCount)
    return errorCount

def removeBackwardTimestampError(modeList):
    '''remove backward timestamp error where duration less than 0'''
    '''append the correct end time after removing a row'''
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

def recalculateDuration(modelist):
    '''calculate the duration using the start time and end time appended in modelist'''
    '''need to change the data type to timestamp first for some datasets'''
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
    '''remove duration error where the duration of a 'Mode' is less than 5s'''
    '''return a correct modelist where all the duration >5s'''
    '''but ignoring those error rows'''
    newlist = []
    for i in range(len(modelist)-1):
        if modelist[i][2] < 5: #less than 5s
          pass
        else:
          newlist.append(modelist[i])
    newlist.append(modelist[-1]) #add last item in
    return newlist

#seems not useful anymore
def selectTimestampKey(modelist):
    newlist = []
    for i in modelist:
        newlist.append(i[1])
    return newlist

def findRepetitiveMode(modelist):
    '''generate a list of repetitive 'Mode'''
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
    '''generate a new modelist without repetitive 'Mode' '''
    newlist = []
    #print("remove starting here!")
    for i in range(len(modelist)-1):
        if modelist[i] in repetitivelist:
          print(modelist[i],"is going to be removed")
          newlist[-1][3] = modelist[i][3]
        else:
          newlist.append(modelist[i])
    #print("newlist length is:", len(newlist))
    return newlist

def checkTimestampIsString(modelist):
    '''change the datatype of timestamp into string'''
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
    '''Error Removing Pipeline'''
    '''get mode changed, remove backward timestamp error, recalculate duration, remove repetitive error, recalculate duration'''
    
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
    '''append stations to the modelist generated'''
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
    '''add 'Station' column to dataframe using the list of timestamp keys generated'''
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
    '''fill empty rows of 'Station' with the previous non-empty 'Station' '''
    temp = data['Station'][0]
    for i in range(len(data['Station'])):
        if data['Station'][i] != '0':
          temp = data['Station'][i]
        else:
          data['Station'][i] = temp
    return data

def modifyColumnStation(data,modelist):
    '''Modify 'Station' column pipeline'''
    '''combine 2 functions that works on dataframe together'''
    data1 = addStationToDf(data,modelist)
    print("add station done!!!")
    data2 = fillEmptyStationToDf(data1)
    print("fill empty done!!!")
    return data2

def visualizationAfterClustering(data1, data2, data3, data4, data5, data6):
    '''visualise the clustered variables'''
    plt.figure(figsize=(20,72))
    for i, col in enumerate(['Acc_Lin_X', 'Acc_Lin_Y', 'Acc_Lin_Z', 'Acc_X', 'Acc_Y','Acc_Z', 'Bar_Pressure', 'Gyr_X', 'Gyr_Y', 'Gyr_Z', 'Mag_X', 'Mag_Y','Mag_Z'],start=1):
        plt.subplot(8,2,i)
        plt.plot(data1[col],'.y',label='Cluster 1')
        if data2 is not None:
          plt.plot(data2[col],'.r',label='Cluster 2')
        if data3 is not None:
          plt.plot(data3[col],'.g',label='Cluster 3')
        if data4 is not None:
          plt.plot(data4[col],'.b',label='Cluster 4')
        if data5 is not None:
          plt.plot(data5[col],'.c',label='Cluster 5')
        if data6 is not None:
          plt.plot(data6[col],'.m',label='Cluster 6')
        plt.legend()
        plt.xlabel('Time') #actually is the index count
        plt.title(col)

def silhouetteAnalysis(data):
    '''Calculate silhouette scores for n clusters and visualise the clustered data'''
    range_n_clusters = [2, 3, 4, 5, 6]
    for n_clusters in range_n_clusters:
          # Create a subplot with 1 row and 2 columns
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.set_size_inches(18, 7)

        # The 1st subplot is the silhouette plot
        # The silhouette coefficient can range from -1, 1 but in this example all
        # lie within [-0.1, 1]
        ax1.set_xlim([-0.1, 1])
        # The (n_clusters+1)*10 is for inserting blank space between silhouette
        # plots of individual clusters, to demarcate them clearly.
        ax1.set_ylim([0, len(data) + (n_clusters + 1) * 10])

        # Initialize the clusterer with n_clusters value and a random generator
        # seed of 10 for reproducibility.
        clusterer = KMeans(n_clusters=n_clusters, random_state=10)
        cluster_labels = clusterer.fit_predict(data)

        # The silhouette_score gives the average value for all the samples.
        # This gives a perspective into the density and separation of the formed
        # clusters
        silhouette_avg = silhouette_score(data, cluster_labels)
        print("For n_clusters =", n_clusters,
              "The average silhouette_score is :", silhouette_avg)

        # Compute the silhouette scores for each sample
        sample_silhouette_values = silhouette_samples(data, cluster_labels)

        y_lower = 10
        for i in range(n_clusters):
            
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[cluster_labels == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / n_clusters)
            ax1.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

        ax1.set_title("The silhouette plot for the various clusters.")
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
        ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

        ax1.set_yticks([])  # Clear the yaxis labels / ticks
        ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

        # 2nd Plot showing the actual clusters formed
        colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
        ax2.scatter(data[:, 0], data[:, 1], marker='.', s=30, lw=0, alpha=0.7,
                  c=colors, edgecolor='k')

        # Labeling the clusters
        centers = clusterer.cluster_centers_
        # Draw white circles at cluster centers
        ax2.scatter(centers[:, 0], centers[:, 1], marker='o',
                    c="white", alpha=1, s=200, edgecolor='k')

        for i, c in enumerate(centers):
            ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
                        s=50, edgecolor='k')

        ax2.set_title("The visualization of the clustered data.")
        ax2.set_xlabel("Feature space for the 1st feature")
        ax2.set_ylabel("Feature space for the 2nd feature")

        plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                      "with n_clusters = %d" % n_clusters),
                     fontsize=14, fontweight='bold')

  plt.show()
