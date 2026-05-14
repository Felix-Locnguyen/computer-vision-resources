import os
import cv2 
from PIL import Image
import numpy as np
from img2vec_pytorch import Img2Vec
from utils import get_face_landmarks
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

data_dir = 'Datasets/Emotion_Recognition'

# clean data
# output = []
# for emotion_idx, emotion in enumerate(os.listdir(data_dir)):
#     for img_path_ in os.listdir(os.path.join(data_dir,emotion)):
#         img_path = os.path.join(data_dir,emotion,img_path_)

#         img = cv2.imread(img_path)
#         face_landmarks = get_face_landmarks(img)

#         if len(face_landmarks) == 1404:
#             face_landmarks.append(int(emotion_idx))
#             output.append(face_landmarks)
#     np.savetxt('data.txt',np.asarray(output))

data= {}
for i ,category in enumerate(['train','test']):
    features = []
    labels = []
    for emotion_idx, emotion in enumerate(os.listdir(os.path.join(data_dir, category))):
        emotion_path = os.path.join(data_dir, category, emotion)
        for img_file in os.listdir(emotion_path):
            img = cv2.imread(os.path.join(emotion_path, img_file))
            img = img.flatten() 
            features.append(img)
            labels.append(emotion_idx)

    data[["training_data","validation_data"][i]] = features
    data[["training_label","validation_label"][i]] = labels

print("đọc xong data")
#train model
model = RandomForestClassifier(
    n_estimators=500,       # Tăng từ 200 → 500
    max_depth=20,           # Giới hạn độ sâu
    min_samples_split=5,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)
model.fit(data["training_data"], data["training_label"])

# testmodel
pred = model.predict(data["validation_data"])
print(classification_report(data["validation_label"],pred))

#save model
with open("model.p", "wb") as f:
    pickle.dump(model, f)