from img2vec_pytorch import Img2Vec
from PIL import Image
import pickle

with open('./model.p','rb') as f:
    model = pickle.load(f)

img2vec = Img2Vec()
img_path = r"./Datasets/Images/rain.jpg"

img = Image.open(img_path)

features = img2vec.get_vec(img)

predict = model.predict([features])
print(predict)