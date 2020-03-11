
import os
import pickle
import shutil
import time
from datetime import datetime
import cv2
import face_recognition
import imutils
from PIL import Image
from imutils.video import VideoStream
import time

args = {'encodings': 'encodings.pickle', 'output': None, 'display': 1, 'detection_method': 'cnn'}

print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

found = False
unknownFaces = 0
knownFaces = 0
counter = 0

while True:
    frame = vs.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750)
    r = frame.shape[1] / float(rgb.shape[1])
    print(time.perf_counter())
    boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
    print(time.perf_counter())
    break
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    print("Face detected: ", len(encodings))

    found = False
    for encoding in encodings:
        found = True
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            print(counts[max(counts, key=counts.get)])
            threshold = round(data["names"].count(name) * 0.60)
            if (counts[max(counts, key=counts.get)] >= threshold):
                name = max(counts, key=counts.get)
            else:
                name = "Unknown"
            if (name == "Unknown"):
                unknownFaces += 1
            else:
                knownFaces += 1
                counter = 0
            now = datetime.now()
            if (now.second % 3 == 0):
                date_time = "temp\\" + now.strftime("%d-%m-%Y_%H-%M-%S") + ".png"
                cv2.imwrite(date_time, rgb)
                image = Image.open(date_time).rotate(270, expand=True)
                image.thumbnail((600, 468), Image.ANTIALIAS)
                image.save(date_time, quality=40, optimize=True)

        names.append(name)

    if (not found):
        counter += 1
        if (counter > 10):
            if (unknownFaces + knownFaces > 0 and (unknownFaces / (unknownFaces + knownFaces)) * 100 > 80):
                print("Detected unknown person!")
            unknownFaces = 0
            knownFaces = 0
            shutil.rmtree("temp")
            os.mkdir("temp")

    print(unknownFaces, knownFaces)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
