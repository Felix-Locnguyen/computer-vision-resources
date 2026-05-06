import cv2
import os
import pytesseract
from easyocr import Reader
from PIL import Image
import boto3 
# Configure Tesseract path (update if installed in different location)
"""
Note: Có thể lấy data ảnh chứa text ở trang coco-text
https://bgshih.github.io/cocotext/
"""

img_path = os.path.join("Datasets","Images","thumbnail.jpg")

def read_text_tesseract(image_path):
    text = pytesseract.image_to_string(Image.open(img_path),lang='eng')
    return text


def read_text_easyocr(image_path):
  text = ''
  results = reader.readtext(Image.open(image_path))
  for result in results:
    text = text + result[1] +  ' '

  text = text[:-1]
  return text


def read_text_textract(image_path):

  with open(image_path, 'rb') as im:
    response = textract_client.detect_document_text(Document={'Bytes':im.read()})

  text = ''
  for item in response['Blocks']:
    if item['BlockType'] == 'LINE':
      text = text + item['Text'] + ' '

  text = text[:-1]

  return text


### Compare performances ###
import os


def jaccard_similarity(sentence1, sentence2):
    # Tokenize sentences into sets of words
    set1 = set(sentence1.lower().split())
    set2 = set(sentence2.lower().split())

    # Calculate Jaccard similarity (Tính giao và hợp)
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))

    # Avoid division by zero if both sets are empty
    similarity = intersection_size / union_size if union_size != 0 else 0.0
    return similarity


score_tesseract = 0
score_easyocr = 0
score_textract = 0
for image_path_ in os.listdir('./Datasets/Images'):
   image_path = os.path.join('./Datasets/Images',image_path_)

   gt = image_path[:-4].replace("_"," ")

   score_tesseract += jaccard_similarity(gt, read_text_tesseract(image_path).lower().replace('\n', '').replace('!', '').replace('?', '').replace('.', ''))
   score_easyocr += jaccard_similarity(gt, read_text_easyocr(image_path).lower().replace('\n', '').replace('!', '').replace('?', '').replace('.', ''))
   score_textract += jaccard_similarity(gt, read_text_textract(image_path).lower().replace('\n', '').replace('!', '').replace('?', '').replace('.', ''))

print('score tesseract:', score_tesseract / 100)
print('score_easyocr:', score_easyocr / 100)
print('score_textract:', score_textract / 100)