import cv2
import sys
import time

class Videocam():

    def __init__(self):
        self.detect()



    def detect(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Камера не в 0 порту")
            sys.exit()

        tracker = cv2.TrackerMedianFlow_create()

        ok, frame = cap.read()
        if not ok:
            print('Ошибка чтения видео')
            sys.exit()

        bbox = (287, 23, 86, 320)
        bbox = cv2.selectROI(frame, False)
        ok = tracker.init(frame, bbox)
        while True:
            # Читаем новый фрейм
            ok, frame = cap.read()
            if not ok:
                break

            # Запуск таймера
            timer = cv2.getTickCount()

            # Обновляем трекер
            ok, bbox = tracker.update(frame)

            # Вычисляем fps
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            # рисуем рамку
            if ok:
                # объект найден
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            else:
                # Объект не найден
                cv2.putText(frame, "Cant find any", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

            # HUD трекера( какой трекер используется)
            cv2.putText(frame, "MedianFlowTracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

            # HUD fps
            cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

            face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

            image = frame.copy()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # roi_gray = gray[y:y + h, x:x + w]
                # roi_color = img[y:y + h, x:x + w]
                for_eyes = gray[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(for_eyes)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(image, (ex + x, ey + y), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)

            # Вывод
            #cv2.imshow("Tracking", frame)
            cv2.imshow("Faces", image)

            # Выход по клавише esc
            k = cv2.waitKey(1) & 0xff
            if k == 27: break

v1 = Videocam()
v1.detect()