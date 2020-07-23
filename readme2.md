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

![image](https://user-images.githubusercontent.com/68596059/88156858-a14a1880-cc27-11ea-8ffe-3d872f6fe4ab.png)

Output

![image](https://user-images.githubusercontent.com/68596059/88144809-211bb700-cc17-11ea-8e24-34fc5dd5b1a8.png)

Out[2]: 
![image](https://user-images.githubusercontent.com/68596059/88145210-b5861980-cc17-11ea-866b-3e43ec7e3777.png)

      
￼![image](https://user-images.githubusercontent.com/68596059/88142208-b9fc0380-cc12-11ea-9b1f-4f6607fcd092.png)

## Data Processing
After that, i need to convert some categorical variable into dummy variable.For that , i will use get_dummies method.and then i will use StanderdScaler() from sklearn to scale my dataset.

Code

![image](https://user-images.githubusercontent.com/68596059/88146505-98eae100-cc19-11ea-9b9d-638cb6769f63.png)


## Train-test dataset split

Next, i will import train_test_split to split the dataset into train and test dataset. then i will import all model of classification.

Code 

![image](https://user-images.githubusercontent.com/68596059/88147581-0ba88c00-cc1b-11ea-855c-6c96aeff62e3.png)


## K Neighbors Classifier
In this model we classify a data based on k nearest data point. so score value varies with k.Thats why i will plot a graph of score with different values of k and check when do i achive the best score. At first i import KNeighborsClassifier from sklearn.neighbors . then I will use k_score array to store the score for different k values. After that i will plot the graph.

Code

![image](https://user-images.githubusercontent.com/68596059/88149684-0993fc80-cc1e-11ea-989e-c28a06036d24.png)


Code(graph plot)

![image](https://user-images.githubusercontent.com/68596059/88150021-78715580-cc1e-11ea-946f-0b0e432481e6.png)


Output

![image](https://user-images.githubusercontent.com/68596059/88150993-bc188f00-cc1f-11ea-86b6-34bf6fcd0a1c.png)


From the above picture , it is clear that  the maximum score is achived for the 8 neighbors. So we will predict test dataset for neighbors value 8.And the maximum score is 87%.
After that i will construct a confusion matrix.

![image](https://user-images.githubusercontent.com/68596059/88155381-a4dca000-cc25-11ea-82e1-c6321ecdc946.png)

Confusion Matrix

![image](https://user-images.githubusercontent.com/68596059/88155779-25030580-cc26-11ea-9e4f-f5f61bc81894.png)


## Support Vector Classifier

In this model we classify one data point based on kernels.So score value depends on kernel. Thats why i will plot agraph of score with different kernel like linear,poly,rbf and sigmoid and check whenn do i achieve the maximum score.At first  i will import SVC  from sklearn.svm . Then i will train dataset on different kernel and plot graph.I will use s_score array to store the score with different kernel.

Code

![image](https://user-images.githubusercontent.com/68596059/88178474-14fc1d80-cc48-11ea-8572-73fc7e6d0e08.png)


Code(Graph plot)

![image](https://user-images.githubusercontent.com/68596059/88178808-95bb1980-cc48-11ea-839d-efc3962a559d.png)

Output

![image](https://user-images.githubusercontent.com/68596059/88179102-0104eb80-cc49-11ea-92e7-a7853b87c05f.png)

from the abbove graph , i clearly see that the maximum score is achieved by rbf kernel.So i will predict the dataset in rbf kernel mode  And then construct a confusion matrix.
Code

![image](https://user-images.githubusercontent.com/68596059/88180206-ab314300-cc4a-11ea-8fb9-057dcda31311.png)

Confussion Matrix

![image](https://user-images.githubusercontent.com/68596059/88180573-33174d00-cc4b-11ea-9856-92f5e3a6a1a3.png)


## Decision Tree Classifier 

In this model we classify one datapoint based on decision tree.And score depends on max feature.Thats why i will plot a graph of score with different max_feature.At first i will import DecisionTreeClassifier from sklearn.tree. Then i will train dataset in max_feature and append the score into d_tree array.After that we will plot graph.Then i will chechk when do i achieve the maximum score.


Code 

![image](https://user-images.githubusercontent.com/68596059/88259017-16c4f000-ccdf-11ea-9065-22abec215e9f.png)

Code(Graph Plot)

![image](https://user-images.githubusercontent.com/68596059/88259259-918e0b00-ccdf-11ea-8b2f-a32787cc1c8f.png)




