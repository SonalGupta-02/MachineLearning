
# loading dataset
from sklearn.datasets import load_iris

#loading into variable
iris_data=load_iris()

# describing iris data internally
dir(iris_data)

#target output values--
iris_data.target_names

#now attribute of features of given data
iris_data.feature_names

#data with attributes
iris_features=iris_data.data

#extracting label as per faeures
label=iris_data.target

#  sep  data  into  training  and  testing
from   sklearn.model_selection   import   train_test_split

#help(train_test_split)
train_data,test_data,train_label,test_label=train_test_split(iris_features,label,test_size=0.2)

# importing   KNN   clf
from  sklearn.neighbors   import  KNeighborsClassifier

#   now  calling   KNN  
#   this is  by  default  value of K
kclf=KNeighborsClassifier(n_neighbors=5)

#   applying  traing  data  
ktrained=kclf.fit(train_data,train_label)

# now time for  prediction  
predict_output=ktrained.predict(test_data)
predict_output

test_label

#   calculating  accuracy score
from   sklearn.metrics   import  accuracy_score

acrknn=accuracy_score(test_label,predict_output)
acrknn

