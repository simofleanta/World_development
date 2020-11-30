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

economic=pd.read_csv('unemployment.csv')
print(economic.columns)
df_economic=DataFrame(economic.head(10))
print(df_economic.head(10))

economic=pd.read_csv('Inflation_forecast.csv')
print(economic.columns)
df_inflation=DataFrame(economic.head(10))
print(df_inflation.head(10))


#merged the two datasets 
inflation_unemployment=pd.merge(df_inflation,df_economic)
print(inflation_unemployment)

#getting rid of mess in my table
#data taken from ins bnr
#data showing unemployment unregistered and supported 

Inflation_Unemployed_Table=inflation_unemployment[['Year','Months','Term','IPC','Constant_taxes','Annual_inflation_target','Number_unemployd']].copy()
print(Inflation_Unemployed_Table)



#may be corrs






