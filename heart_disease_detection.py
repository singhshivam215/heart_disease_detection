# Classification template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('datasets_33180_43520_heart.csv')
dataset.info()
dataset.describe()
dataset.hist()
dataset=pd.get_dummies(dataset,columns=['sex','cp','fbs','restecg','exang','slope','ca','thal'])

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
col=['age','trestbps','chol','thalach','oldpeak']
dataset[col] = sc.fit_transform(dataset[col])
X = dataset.drop(['target'],axis=1)
y = dataset['target']

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state=0)


# Fitting classifier to the Training set
# Create your classifier here
from sklearn.neighbors import KNeighborsClassifier
k_score=[]
for i in range(1,21):
      k_classifier=KNeighborsClassifier(n_neighbors=i)
      k_classifier.fit(X_train,y_train)
      k_score.append(k_classifier.score(X_test,y_test))
# Predicting the Test set results
plt.plot([k for k in range(1,21)],k_score,color='blue' )
for i in range(1,21):
    plt.text(i,k_score[i-1],(i,k_score[i-1]))
plt.xlabel('Number of Neighbors')
plt.ylabel('scores')
plt.xticks([i in range(1,21)])
plt.title('k NEIGHBORS CLASSIFIER SCORE ')
k_classifier=KNeighborsClassifier(n_neighbors=8)
k_classifier.fit(X_train,y_train)
y_pred = k_classifier.predict(X_test)
print("the score in percentage {}% with 8 neighbors".format(k_score[7]*100))
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

from sklearn.svm import SVC
s_score=[]
kernels=['linear','poly','rbf','sigmoid']
for i in range(len(kernels)):
    if i==0:
         s_classifier=SVC(kernel=kernels[i])
    else:
        s_classifier=SVC(kernel=kernels[i],gamma='auto')
    s_classifier.fit(X_train,y_train)
    s_score.append(s_classifier.score(X_test,y_test))
    
from matplotlib.cm import rainbow
colors = rainbow(np.linspace(0,1,len(kernels)))
plt.bar(kernels,s_score,color=colors)
for i in range(len(kernels)):
    plt.text(i,s_score[i],s_score[i])
    plt.xlabel('kernels')
    plt.ylabel('scores')
    plt.title('Support vector classifier scores for different kernels')
    
s_classifier=SVC(kernel=kernels[0])
s_classifier.fit(X_train,y_train)
y1_pred = s_classifier.predict(X_test)
print("the score in percentage {}% with linear kernel".format(s_score[0]*100))
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm1= confusion_matrix(y_test, y1_pred)


from sklearn.tree import DecisionTreeClassifier
d_score=[]
for i in range(1,len(X.columns)+1):
    d_classifier=DecisionTreeClassifier(max_features=i,random_state=0)
    d_classifier.fit(X_train,y_train)
    d_score.append(d_classifier.score(X_test,y_test))
   
plt.plot([i for i in range(1,len(X.columns)+1)],d_score,color='blue')
for i in range(1,len(X.columns)+1):
    plt.text(i,d_score[i-1],(i,d_score[i-1]))
plt.xticks([i for i in range(1,len(X.columns)+1)])
plt.xlabel(' MAX FEATURES')
plt.ylabel('SCORES')
plt.title('DECISION TREE CLASSIFIER SCORE WITH DIFFERENT NUMBER OF MAXIMUM FEATURES')

d_classifier=DecisionTreeClassifier(max_features=18,random_state=0)
d_classifier.fit(X_train,y_train)
y3_pred=d_classifier.predict(X_test)
print("the score in percentage {}% with max feature 18".format(d_score[17]*100))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm2= confusion_matrix(y_test, y3_pred)

from sklearn.ensemble import RandomForestClassifier
r_score=[]
estimators=[10,100,200,500,1005]
for i in estimators:
    r_classifier= RandomForestClassifier(n_estimators=i,random_state=0)
    r_classifier.fit(X_train,y_train)
    r_score.append(r_classifier.score(X_test,y_test))
    
colors=rainbow(np.linspace(0,1,len(estimators)))
plt.bar([i for i in range(len(estimators))],r_score,color=colors,width=0.8)
for i in range(len(estimators)):
    plt.text(i,r_score[i],r_score[i])
plt.xticks(ticks=[i for i in range(len(estimators))],labels=[str[est] for est in estimators])
plt.xlabel('NUMBER OF ESTIMATORS')
plt.ylabel('SCORES')
plt.title('RANDOM FOREST CLASSIFIER SCORE WITH DIFFERENT EESTIMATORS')

r_classifier= RandomForestClassifier(n_estimators=100,random_state=0)
r_classifier.fit(X_train,y_train)
y4_pred=r_classifier.predict(X_test)
    
print("the score in percentage {}% with number of estimators=100".format(r_score[1]*100))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm3= confusion_matrix(y_test, y4_pred)

