import os
from  skimage.io import imread
from skimage.transform import resize 
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import pickle
# prepare data
input_dir = "Datasets/clf-data"
categories = ["empty","not_empty"]

data = []
labels = []

for category_idx in categories:
    for file in os.listdir(os.path.join(input_dir,category_idx)):
        img_path = os.path.join(input_dir, category_idx, file)
        img = imread(img_path)
        img = resize(img,(15,15))
        data.append(img.flatten())

        labels.append(category_idx)

data = np.asarray(data)
labels = np.asarray(labels)

# train test split
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, stratify=labels, shuffle=True)
# train model
classifier = SVC()
parameters =[{"gamma": [0.01,0.001,0.0001],
              "C":[1,10,100,1000],
              }]
grid = GridSearchCV(classifier,parameters)
grid.fit(x_train,y_train)
print(grid.best_estimator_)
print(grid.best_params_)

# test model
best_estimator = grid.best_estimator_
y_predict = best_estimator.predict(x_test)
print(classification_report(y_test,y_predict))


# save model
pickle.dump(best_estimator,open("./model.p","wb"))