# Heart Disease Prediction
## Introduction
This project is identify that wheather a man is suffering from heart disease oor not. i will be using different machine learning  classification model to classify that.The models are 
1. K Neighbors classification Model
2. Support Vector Classification Model
3. Decision Tree Classification Model
4. Random Forest Classification Model

## import libraries
Lets first import some useful library like numpy , pandas,matplotlib. I use pyplot subpackage from matplotlib.

*numpy* It can be utilised for mathematical operation on arrays such as trigonometric ,statistical ,and algebric operation.
*pandas-* It is use for data manipulation and analysis.
*matplot.pyplot-* It is a plotting library in python.

code

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

Output

In [1]: import numpy as np

   ...: import matplotlib.pyplot as plt
   
   ...: import pandas as pd

## Import dataset and dataset analysis
Then dataset is loaded into the variable dataset.After that dataset is analyzed by by using info(), describe() methods and plot a histogram by using hiist() method.

code

dataset = pd.read_csv('datasets_33180_43520_heart.csv')

dataset.info()

dataset.describe()

dataset.hist()

dataset = pd.read_csv('datasets_33180_43520_heart.csv')
dataset.info()
dataset.describe()
dataset.hist()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 303 entries, 0 to 302
Data columns (total 14 columns):
age         303 non-null int64
sex         303 non-null int64
cp          303 non-null int64
trestbps    303 non-null int64
chol        303 non-null int64
fbs         303 non-null int64
restecg     303 non-null int64
thalach     303 non-null int64
exang       303 non-null int64
oldpeak     303 non-null float64
slope       303 non-null int64
ca          303 non-null int64
thal        303 non-null int64
target      303 non-null int64
dtypes: float64(1), int64(13)
memory usage: 33.2 KB
