from img2vec_pytorch import Img2Vec
import os
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import pickle

# prepare data
img2vec = Img2Vec()

data_dir = "Datasets/dataset2"
train_dir = os.path.join(data_dir,"train")
val_dir = os.path.join(data_dir,"val")

features = []
labels = []
data ={}

for j, dir_ in enumerate([train_dir,val_dir]):
    for category in os.listdir(dir_):
        for img_path in os.listdir(os.path.join(dir_, category)):
            img_path_ = os.path.join(dir_,category,img_path)
            img = Image.open(img_path_)

            img = img.convert("RGB")
            img_feature = img2vec.get_vec(img)

            features.append(img_feature)
            labels.append(category)

    data[["training_data","validation_data"][j]] = features
    data[["training_label","validation_label"][j]] = labels


# train model
model = RandomForestClassifier()
model.fit(data['training_data'],data['training_label'])

# test model 
model_pred = model.predict(data["validation_data"])
print(classification_report(data['validation_label'],model_pred))

# save model
pickle.dump(model,open("./model.p","wb"))