import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('royalty_free_test.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for x,y,w,h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,225,0), 2)

cv2.imshow('img', img)
cv2.waitKey()

# Uncomment the following line to save the image with detected faces with name 'faces_detected.jpg'
# cv2.imwrite('faces_detected.jpg', img)