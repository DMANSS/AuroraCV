import cv2
import sys


class Detection:

    def start(self):
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

        # Задаем трекер.
        tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
        tracker_type = tracker_types[4]

        if int(minor_ver) < 3:
            tracker = cv2.Tracker_create(tracker_type)
        else:
            if tracker_type == 'BOOSTING':
                tracker = cv2.TrackerBoosting_create()
            if tracker_type == 'MIL':
                tracker = cv2.TrackerMIL_create()
            if tracker_type == 'KCF':
                tracker = cv2.TrackerKCF_create()
            if tracker_type == 'TLD':
                tracker = cv2.TrackerTLD_create()
            if tracker_type == 'MEDIANFLOW':
                tracker =cv2.TrackerMedianFlow_create()
            if tracker_type == 'GOTURN':
                tracker = cv2.TrackerGOTURN_create()

        # Захват камеры
        video = cv2.VideoCapture(0)

        if not video.isOpened():
            print("Камера не в 0 порту")
            sys.exit()

        # берем первый кадр
        ok, frame = video.read()
        if not ok:
            print('Ошибка чтения видео')
            sys.exit()

        # Рамкой выделяем объект
        bbox = (287, 23, 86, 320)

        bbox = cv2.selectROI(frame, False)

        # Инициализируем трекер с помощью первого кадра и ограничительной рамки
        ok = tracker.init(frame, bbox)

        while True:
            # Читаем новый фрейм
            ok, frame = video.read()
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
            cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

            # HUD fps
            cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
            # Вывод
            cv2.imshow("Tracking", frame)

            # Выход по клавише esc
            k = cv2.waitKey(1) & 0xff
            if k == 27: break

    pass
