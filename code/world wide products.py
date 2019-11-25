# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:32:29 2019

@author: a335s717
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seabornInstance 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
#from sklearn import datasets 
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import Imputer
from fbprophet import Prophet

### new ones
import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import statsmodels.api as sm
import matplotlib
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

#======================================================== Import dataset
df = pd.read_csv('https://raw.githubusercontent.com/aminshojaei/world-wide-product/master/Historical%20Product%20Demand.csv', low_memory = False)

#=======================================================Cleaning dataset

stats = df.describe()
#Lets plot the no of products for each category
ax = df.groupby('Product_Category')['Product_Code'].nunique() 


#Now lets plot the order_demand for each category
ax_1 = df.groupby('Product_Category')['Order_Demand'].nunique()


product_count = df.groupby(['Product_Code']).size().reset_index(name='counts').sort_values(['counts'],ascending=False)


dates = [pd.to_datetime(date) for date in df['Date']]
dates.sort()



df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

isnull = df.isnull().any()

df = df.dropna(subset=['Date'])


df=df.set_index('Date')

df['Order_Demand']=pd.to_numeric(df['Order_Demand'],errors='coerce')

df.dropna(subset=['Order_Demand'],inplace=True)
y =df['Order_Demand']


































#
#
#
#
#
##Historical_product.shape          #Number of rows and columns
#x= Historical_product['Warehouse'].unique()
#print(x)
#
#Historical_product=Historical_product.dropna(how='any')
#statics = Historical_product.describe()     # some quick summary

