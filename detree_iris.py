
from sklearn import datasets
import numpy
import time

# showing datasets
#for i in dir(datasets):
 # print(i)
  #time.sleep(1)

[i for i in dir(datasets) if 'load' in i ]

from sklearn.datasets import load_iris
# now loading IRIS data only
iris=load_iris()
dir(iris)      # exploring variable

#iris.DESCR
# these are feature names 
iris.feature_names

# labels/answers
iris.target_names

# actual data with attributes
features=iris.data
type(features)
features.shape

# now time for target/label data that will be exactly same as no. of features
label=iris.target
label.shape

import matplotlib.pyplot as plt

SL=features[0:,0]
SW=features[0:,1]

plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
plt.scatter(SL,SW,label='sepal_data',marker='+')
plt.scatter(features[0:,2],features[0:,3],label="petal_data",marker='*')
plt.legend()

#  now time  for seperating  data   into two category  
# 1. --training  data
# 2. --testing  data -- Questions 
from   sklearn.model_selection   import  train_test_split
train_data,test_data,label_train,label_test=train_test_split(features,label,test_size=0.1)

from sklearn.tree import DecisionTreeClassifier
#  calling  decisiontree classifier  
clf=DecisionTreeClassifier()

#  now time for  training  clf 
trained=clf.fit(train_data,label_train)

#  now predicting  flowers
predicted_flowers=trained.predict(test_data)

predicted_flowers   #answer

label_test      #actual answer

from sklearn.metrics import accuracy_score
#  find  accuracy  score  
accuracy_score(label_test,predicted_flowers)
