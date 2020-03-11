# import the necessary packages
import concurrent.futures
import os
import shutil
from PIL import Image
import time
from imutils.video import VideoStream
import face_recognition
import argparse
import imutils
import pickle
from datetime import datetime
import cv2
import threading
import multiprocessing


found = False
unknownFaces = 0
knownFaces = 0
counter = 0
p = None
# def imageSavefromFrame(rgb, date_time):
def imageSavefromFrame(arr):
    print("asdfg", arr)
    # print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    cv2.imwrite(arr[1], arr[0])
    image = Image.open(arr[1]).rotate(270, expand=True)
    image.thumbnail((600, 468), Image.ANTIALIAS)
    image.save(arr[1], quality=40, optimize=True)
    print(arr[1])
    return arr[1]


def encodings_fun(encoding):
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
        # # TODO solve critical section problem

        if (now.second % 5 == 0):
            # if (p is not None):
            #     p.join()
            date_time = "temp\\" + now.strftime("%d-%m-%Y_%H-%M-%S.%f") + ".png"
            temp1.append([rgb, date_time])

    print("Size: ", len(temp1))
    print(temp1)
    names.append(name)




args = {'encodings': 'encodings.pickle', 'output': None, 'display': 1, 'detection_method': 'cnn'}

print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()


temp1 = []
while True:

    frame = vs.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750)
    r = frame.shape[1] / float(rgb.shape[1])

    boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    print("Face detected: ", len(encodings))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(encodings_fun, encodings)

    if args["display"] > 0:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

cv2.destroyAllWindows()
vs.stop()

