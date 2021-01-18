import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px
import datetime

"""How would we solve a Community problem statement:

Many people live at blocks distance from thei office. It takes them 1 minute per block to the office and around 20 seconds per bloc by bike.
If it takes them various minutes more to walk to office than to ride thaen how many blocks distance do they travel to their offices?

Solutions? """

#open file
bike=pd.read_csv('Bikes_blocks.csv')
print(bike.columns)
bike_df=DataFrame(bike.head(60))
print(bike_df.head(60))

#check dtypes
print(bike_df.dtypes)
# if we hve null values 
print(bike_df.isnull)
#shape of data
print(bike_df.shape)
#data description
print(bike_df.describe())

#parse index
bike_df['year']=pd.to_datetime(bike_df['year'], infer_datetime_format=True)
indexeddf=bike_df.set_index(['year'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=bike_df['year']=pd.to_datetime(bike_df['year'], format='%d-%m-%y')

Day=bike_df['year'].dt.day_name()
Month=bike_df['year'].dt.month_name()
Year=bike_df['year'].dt.year

#subsetting timeseries
bike_df['Year']=bike_df['year'].dt.year
bike_df['Month']=bike_df['year'].dt.month_name()
bike_df['Day']=bike_df['year'].dt.day_name()
print(bike_df.head(3))

#-----------------------------

#calculations

#1 what is the number of blocks people walk to their office 
#2 as it takes a couple of minutes more thatn on the bike, people walk 1 minute per block and ride more blocks in 60 seconds 
#3 which leads to the fifference between number of blocks and the actual ride mintes 

#How many blocks can people ride in 60 seconds  given their minutes walk?
bike_df['Blocks_ride_minute']=60/bike_df.Seconds_per_Block

#What is the total minutes ride?
bike_df['Total_minutes_ride']=bike_df.No_blocks/bike_df.Blocks_ride_minute

#finally what is the difference between number of blocks and  minutes on byke to office ?
bike_df['Number_blocks_to_office']=bike_df.No_blocks-bike_df.Total_minutes_ride

#print desired columns for visuals
bikes_office=bike_df[['Year','Month','Day','Min_walk','No_blocks','Seconds_per_Block','Blocks_ride_minute','Total_minutes_ride','Number_blocks_to_office']].copy()
print(bikes_office)


#--------------------------------------------------

# PLots


#How far the people travel to their work?
f,axes = plt.subplots(1,2, figsize=(15, 10))
A=sns.scatterplot(bikes_office.Min_walk, bikes_office.Number_blocks_to_office, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

B=sns.scatterplot(bikes_office.Total_minutes_ride, bikes_office.Number_blocks_to_office, s=100, edgecolor='black', alpha=0.5,\
     palette='viridis',ax=axes[1])

plt.show()


#Filter for Thursday  

bike_day=bikes_office[bikes_office.Day=='Thursday']


#Which day is more frequently on th bike?

f,axes = plt.subplots(1,2, figsize=(15, 10))
C=sns.scatterplot(bike_day.Min_walk, bike_day.Total_minutes_ride, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

D=sns.boxplot(bikes_office.Day, bikes_office.Total_minutes_ride, palette='viridis',hue_order=[True,False],ax=axes[1])

plt.show()












 








