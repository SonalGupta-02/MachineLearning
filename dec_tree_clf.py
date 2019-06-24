
import numpy as np
import pandas as pd

# for apple and orange
# 0 for apple and 1 for orange
features=[[100,'0'],[120,'0'],[130,'1'],[150,'1']]

# now answer accordingly
label=['apple','apple','orange','orange']

from sklearn.tree import DecisionTreeClassifier     #decision tree clf only

# calling decision tree clf
clf=DecisionTreeClassifier()

# now time for training data
trained=clf.fit(features,label)

# now predicting
trained.predict([[120,1]])

