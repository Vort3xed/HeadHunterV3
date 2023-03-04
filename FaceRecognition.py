import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

input_folder = 'frames'
output_folder = 'faces'

for file_name in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, file_name))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

        face_img = img[y:y + h, x:x + w]

        output_path = os.path.join(output_folder, f"{file_name}_{x}_{y}.jpg")
        cv2.imwrite(output_path, face_img)

    output_path = os.path.join(output_folder, f"{file_name}_detected.jpg")
    cv2.imwrite(output_path, img)