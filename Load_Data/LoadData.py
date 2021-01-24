# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:28:36 2021

@author: Ang Kai Yang
"""

import pandas as pd
def loaddowntown_s6edge():
  s6blue_url1='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Blue0.csv'
  s6blue_url2='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Blue1.csv'
  s6blue_url3='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Blue2.csv'
  s6blue_url4='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Blue3.csv'
  s6blue_url5='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Blue4.csv'
  s6blue_url6='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Blue5.csv'
  s6blue_url7='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Blue6.csv'
  s6blue_url8='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Blue7.csv'
  s6blue_url9='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Blue8.csv'
  s6blue_url10='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Blue9.csv'
  s6blue1=pd.read_csv(s6blue_url1)
  s6blue2=pd.read_csv(s6blue_url2)
  s6blue3=pd.read_csv(s6blue_url3)
  s6blue4=pd.read_csv(s6blue_url4)
  s6blue5=pd.read_csv(s6blue_url5)
  s6blue6=pd.read_csv(s6blue_url6)
  s6blue7=pd.read_csv(s6blue_url7)
  s6blue8=pd.read_csv(s6blue_url8)
  s6blue9=pd.read_csv(s6blue_url9)
  s6blue10=pd.read_csv(s6blue_url10)
  frames=[s6blue1,s6blue2,s6blue3,s6blue4,s6blue5,s6blue6,s6blue7,s6blue8,s6blue9,s6blue10]
  global bukitPanjangToExpo_s6edge
  bukitPanjangToExpo_s6edge=pd.concat(frames)

loaddowntown_s6edge()
bukitPanjangToExpo_s6edge