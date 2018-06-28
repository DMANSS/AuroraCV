import numpy
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    #img = cv2.imread('kol.jpg')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image = frame.copy()
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        #roi_gray = gray[y:y + h, x:x + w]
        #roi_color = img[y:y + h, x:x + w]
        for_eyes = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(for_eyes)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(image, (ex + x, ey + y), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)

    cv2.imshow("Tracking", image)

    # Выход по клавише esc
    k = cv2.waitKey(1) & 0xff
    if k == 27: break