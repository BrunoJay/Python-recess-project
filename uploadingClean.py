# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:10:52 2019

@author: OKELLO MARVIN
"""

import pandas as pd
import numpy as np

# The first step is to load the data from the csv files into the IDE

#Importing from the accident excel file
ac=pd.read_excel("Accidents0515.xlsx")

#Importing from the casuality excel file
cs=pd.read_excel("Casualties0515.xlsx")

#Importing from the Vehicle excel file
vs=pd.read_excel("Vehicles0515.xlsx")

#Clean each dataframe and remain with the features that you want to use

"""Dealing with the ac variable which contains accident data"""

#Dropping some cells that wont be used
ac1=ac.drop(['1st_Road_Class','Police_Force','Local_Authority_(District)','Local_Authority_(Highway)','Junction_Control','Did_Police_Officer_Attend_Scene_of_Accident','1st_Road_Number','2nd_Road_Class','2nd_Road_Number','Pedestrian_Crossing-Human_Control','Pedestrian_Crossing-Physical_Facilities','Special_Conditions_at_Site','Carriageway_Hazards','LSOA_of_Accident_Location'],axis='columns',inplace=False)

# check if there exist nan values
print(ac1.isna().values.any())
#showing the number of missing values
print(ac1.isna().sum())

# Converting the Accident_Severity to be 0- slight and serious and 1-fatal
ac1['Accident_Severity'].replace(2,0,inplace=True)
ac1['Accident_Severity'].replace(3,0,inplace=True)


"""Dealing with the cs variable which contains all value about casualties"""

#Dropping some cells that wont be used
cs1=cs.drop(['Pedestrian_Movement','Vehicle_Reference','Casualty_Reference','Sex_of_Casualty','Age_of_Casualty','Car_Passenger','Bus_or_Coach_Passenger','Pedestrian_Road_Maintenance_Worker','Casualty_Type','Casualty_Home_Area_Type'],axis='columns',inplace=False)

# check if there exist nan values
print(cs1.isna().values.any())
print(cs1.isna().sum())

#dropping the Accident_Index in cs dataframe
cs2=cs1.drop(['Accident_Index'],axis='columns',inplace=False)


# Converting the Casualty_Severity to be 0- slight and serious and 1-fatal
cs2['Casualty_Severity'].replace(2,0,inplace=True)
cs2['Casualty_Severity'].replace(3,0,inplace=True)


"""Dealing with the vs variable which contains all value about Vehicles"""

#Dropping some cells that wont be used
vs1=vs.drop(['Vehicle_Reference','Towing_and_Articulation','Junction_Location','Vehicle_Leaving_Carriageway','Hit_Object_off_Carriageway','Was_Vehicle_Left_Hand_Drive?','Age_of_Driver','Vehicle_Location-Restricted_Lane','Age_Band_of_Driver','Engine_Capacity_(CC)','Propulsion_Code','Driver_IMD_Decile','Driver_Home_Area_Type'],axis='columns',inplace=False)
# check if there exist nan values
print(vs1.isna().values.any())
print(vs1.isna().sum())

#dropping the Accident_Index in vs dataframe
vs2=vs1.drop(['Accident_Index'],axis='columns',inplace=False)


#concatenating the dataframes from all the 3 dataframes
#concatenate the dataframe now to join ac and cs (which lacks the accident_index because they would clash with that of ac)
all_data=pd.concat([ac1,cs2],axis='columns')

#concatenate the dataframe now to join all_data and vs (which lacks the accident_index because they would clash with that of all_data)
all_data_1=pd.concat([all_data,vs2],axis='columns')

#drop rows with missing value and check if there are any missing values afterwards
all_data_2=all_data_1.dropna()
print(all_data_2.isna().values.any())
print(all_data_2.isna().sum())

