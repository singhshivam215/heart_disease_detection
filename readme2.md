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

![image](https://user-images.githubusercontent.com/68596059/88143353-b23d5e80-cc14-11ea-9d45-7e05685c4c57.png)


Output
![image](https://user-images.githubusercontent.com/68596059/88143652-37287800-cc15-11ea-8e02-6f10e0ecaf46.png)


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

Out[2]: 
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BB79860>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BBED8D0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BC20E80>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BC59470>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BC88A20>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BCC3048>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BA55518>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BD17B00>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BD17B38>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BD85668>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BDB6C18>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BDF3208>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BE257B8>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BE55D68>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BE93358>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000015B1BEC3908>]],
      dtype=object)
      prinstscreen()
      
￼![image](https://user-images.githubusercontent.com/68596059/88142208-b9fc0380-cc12-11ea-9b1f-4f6607fcd092.png)

