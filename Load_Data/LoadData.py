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

def loaddowntown_iphone12pro():
    iphoneblue_url1='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/iphoneblue1.csv'
    iphoneblue_url2='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/iphoneblue2.csv'
    iphoneblue_url3='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/iphoneblue3.csv'
    iphoneblue_url4='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/iphoneblue4.csv'
    iphoneblue_url5='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/iphoneblue5.csv'
    iphoneblue_url6='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/iphoneblue6.csv'
    iphoneblue_url7='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/iphoneblue7.csv'
    iphoneblue1=pd.read_csv(iphoneblue_url1)
    iphoneblue2=pd.read_csv(iphoneblue_url2)
    iphoneblue3=pd.read_csv(iphoneblue_url3)
    iphoneblue4=pd.read_csv(iphoneblue_url4)
    iphoneblue5=pd.read_csv(iphoneblue_url5)
    iphoneblue6=pd.read_csv(iphoneblue_url6)
    iphoneblue7=pd.read_csv(iphoneblue_url7)
    frames=[iphoneblue1,iphoneblue2,iphoneblue3,iphoneblue4,iphoneblue5,iphoneblue6,iphoneblue7]
    global bukitPanjangToExpo_iphone12pro
    bukitPanjangToExpo_iphone12pro=pd.concat(frames)

def loadbrown_s6edge():
    s6brown_url='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Brown1.csv'
    global woodlandNorthToWoodlandSouth_s6edge
    woodlandNorthToWoodlandSouth_s6edge=pd.read_csv(s6brown_url)

def loadbrown_iphone12pro():
    iphone_brown_url='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/iphone12_brown.csv'
    global woodlandNorthToWoodlandSouth_iphone12pro
    woodlandNorthToWoodlandSouth_iphone12pro=pd.read_csv(iphone_brown_url)

def loadpurple_s6edge():
    s6purple_url1='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Purple1.xlsx'
    s6purple_url2='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Purple2.xlsx'
    s6purple_url3='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Purple3.xlsx'
    s6purple_url4='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Purple4.xlsx'
    s6purple_url5='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/S6edge%20-%20Purple5.xlsx'
    s6purple1=pd.read_excel(s6purple_url1)
    s6purple2=pd.read_excel(s6purple_url2)
    s6purple3=pd.read_excel(s6purple_url3)
    s6purple4=pd.read_excel(s6purple_url4)
    s6purple5=pd.read_excel(s6purple_url5)
    frames=[s6purple1,s6purple2,s6purple3,s6purple4,s6purple5]
    global harbourFrontToPunggol_s6edge
    harbourFrontToPunggol_s6edge=pd.concat(frames)

def loadpurple_iphone12pro():
    iphonepurple_url1='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/Iphone12pro%20-%20Purple%200.xlsx?raw=true'
    iphonepurple_url2='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/Iphone12pro%20-%20Purple%201.xlsx?raw=true'
    iphonepurple_url3='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/Iphone12pro%20-%20Purple%202.xlsx?raw=true'
    iphonepurple_url4='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/Iphone12pro%20-%20Purple%203.xlsx?raw=true'
    iphonepurple_url5='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/Iphone12pro%20-%20Purple%204.xlsx?raw=true'
    iphonepurple_url6='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/Iphone12pro%20-%20Purple%205.xlsx?raw=true'
    iphonepurple_url7='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/Iphone12pro%20-%20Purple%206.xlsx?raw=true'
    iphonepurple1=pd.read_excel(iphonepurple_url1)
    iphonepurple2=pd.read_excel(iphonepurple_url2)
    iphonepurple3=pd.read_excel(iphonepurple_url3)
    iphonepurple4=pd.read_excel(iphonepurple_url4)
    iphonepurple5=pd.read_excel(iphonepurple_url5)
    iphonepurple6=pd.read_excel(iphonepurple_url6)
    iphonepurple7=pd.read_excel(iphonepurple_url7)
    frames = [iphonepurple1,iphonepurple2,iphonepurple3,iphonepurple4,iphonepurple5,iphonepurple6,iphonepurple7]
    global purple
    purple = pd.concat(frames)

def loadcircle_s6edge():
    s6circle_url1='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle1.xlsx?raw=true'
    s6circle_url2='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle2.xlsx?raw=true'
    s6circle_url3='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle3.xlsx?raw=true'
    s6circle_url4='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle4.xlsx?raw=true'
    s6circle_url5='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle5.xlsx?raw=true'
    s6circle_url6='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle6.xlsx?raw=true'
    s6circle_url7='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle7.xlsx?raw=true'
    s6circle_url8='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle8.xlsx?raw=true'
    s6circle_url9='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle9.xlsx?raw=true'
    s6circle_url10='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle10.xlsx?raw=true'
    s6circle_url11='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle11.xlsx?raw=true'
    s6circle_url12='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle12.xlsx?raw=true'
    s6circle_url13='https://github.com/kaiyang7766/ExploratoryDataAnalysis/blob/main/S6edge%20-%20Circle13.xlsx?raw=true'
    s6circle1=pd.read_excel(s6circle_url1)
    s6circle2=pd.read_excel(s6circle_url2)
    s6circle3=pd.read_excel(s6circle_url3)
    s6circle4=pd.read_excel(s6circle_url4)
    s6circle5=pd.read_excel(s6circle_url5)
    s6circle6=pd.read_excel(s6circle_url6)
    s6circle7=pd.read_excel(s6circle_url7)
    s6circle8=pd.read_excel(s6circle_url8)
    s6circle9=pd.read_excel(s6circle_url9)
    s6circle10=pd.read_excel(s6circle_url10)
    s6circle11=pd.read_excel(s6circle_url11)
    s6circle12=pd.read_excel(s6circle_url12)
    s6circle13=pd.read_excel(s6circle_url13)
    frames=[s6circle1,s6circle2,s6circle3,s6circle4,s6circle5,s6circle6,s6circle7,s6circle8,s6circle9,s6circle10,s6circle11,s6circle12,s6circle13]
    global harbourfrontToDhobyGhautToMarinaBay_s6edge
    harbourfrontToDhobyGhautToMarinaBay_s6edge=pd.concat(frames)

def loadcircle_iphone11():
    circle_url1='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Circle%20Line%201.csv'
    circle_url2='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Circle%20Line%202.csv'
    circle_url3='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Circle%20Line%203.csv'
    circle_url4='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Circle%20Line%204.csv'
    circle_url5='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Circle%20Line%205.csv'
    circle_url6='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Circle%20Line%206.csv'
    circle_url7='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Circle%20Line%207.csv'
    circle_url8='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Circle%20Line%208.csv'
    circle_url9='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Circle%20Line%209.csv'
    circle1=pd.read_csv(circle_url1)
    circle2=pd.read_csv(circle_url2)
    circle3=pd.read_csv(circle_url3)
    circle4=pd.read_csv(circle_url4)
    circle5=pd.read_csv(circle_url5)
    circle6=pd.read_csv(circle_url6)
    circle7=pd.read_csv(circle_url7)
    circle8=pd.read_csv(circle_url8)
    circle9=pd.read_csv(circle_url9)
    frames=[circle1,circle2,circle3,circle4,circle5,circle6,circle7,circle8,circle9[:792]]
    global harbourfrontToDhobyGhautToMarinaBay_iphone11
    harbourfrontToDhobyGhautToMarinaBay_iphone11=pd.concat(frames)

loaddowntown_s6edge()
loaddowntown_iphone12pro()
loadbrown_s6edge()
loadbrown_iphone12pro()
loadpurple_s6edge()
loadpurple_iphone12pro()
loadcircle_s6edge()
loadcircle_iphone11()