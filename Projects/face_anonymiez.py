import cv2
import numpy 
import os

img_path = r"./Datasets/Images/demo.jpg"
# read image
img = cv2.imread(img_path)


# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# detect faces
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

print(f"Found {len(faces)} face(s)")

# blur faces
blurred_img = img.copy()
for (x, y, w, h) in faces:
    # Blur the face region
    face_roi = blurred_img[y:y+h, x:x+w]
    blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 0)
    blurred_img[y:y+h, x:x+w] = blurred_face
    
    # Draw rectangle around face (optional)
    cv2.rectangle(blurred_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# save image
cv2.imwrite('./Datasets/Images/demo_anonymized.jpg', blurred_img)
print("Anonymized image saved to ./Datasets/Images/demo_anonymized.jpg")

cv2.imshow('Original', img)
cv2.imshow('Anonymized', blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        # detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # blur faces
        blurred_frame = frame.copy()
        for (x, y, w, h) in faces:
            # Blur the face region
            face_roi = blurred_frame[y:y+h, x:x+w]
            blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 0)
            blurred_frame[y:y+h, x:x+w] = blurred_face
            
            # Draw rectangle around face (optional)
            cv2.rectangle(blurred_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        cv2.imshow('frame',blurred_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()