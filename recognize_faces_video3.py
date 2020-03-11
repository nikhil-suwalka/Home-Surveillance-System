# USAGE
# python recognize_faces_video.py --encodings encodings.pickle
# python recognize_faces_video.py --encodings encodings.pickle --output output/jurassic_park_trailer_output.avi --display 0

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


# def imageSavefromFrame(rgb, date_time):
def imageSavefromFrame(arr):
    # print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    cv2.imwrite(arr[1], arr[0])
    image = Image.open(arr[1]).rotate(270, expand=True)
    image.thumbnail((600, 468), Image.ANTIALIAS)
    image.save(arr[1], quality=40, optimize=True)
    return arr[1]


# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-e", "--encodings", required=True,
# 	help="path to serialized db of facial encodings")
# ap.add_argument("-o", "--output", type=str,
# 	help="path to output video")
# ap.add_argument("-y", "--display", type=int, default=1,
# 	help="whether or not to display output frame to screen")
# ap.add_argument("-d", "--detection-method", type=str, default="cnn",
# 	help="face detection model to use: either `hog` or `cnn`")
# args = vars(ap.parse_args())

args = {'encodings': 'encodings.pickle', 'output': None, 'display': 1, 'detection_method': 'cnn'}

found = False
unknownFaces = 0
knownFaces = 0
counter = 0
p = None
# loop over frames from the video file stream

images_to_save = []


def get_frame(frame, data):
    global unknownFaces, knownFaces, counter, p, found, args

    # convert the input frame from BGR to RGB then resize it to have
    # a width of 750px (to speedup processing)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750)
    r = frame.shape[1] / float(rgb.shape[1])

    # detect the (x, y)-coordinates of the bounding boxes
    # corresponding to each face in the input frame, then compute
    # the facial embeddings for each face
    boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    # loop over the facial embeddings
    print("Face detected: ", len(encodings))

    found = False
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        found = True
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        # check to see if we have found a match
        if True in matches:
            # find the indexes of all matched faces then initialize a
            # dictionary to count the total number of times each face
            # was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            # print(counts[max(counts, key=counts.get)])
            # determine the recognized face with the largest number
            # of votes (note: in the event of an unlikely tie Python
            # will select first entry in the dictionary)
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
                imageSavefromFrame([rgb, date_time])
                # p = threading.Thread(target=imageSavefromFrame, args=(rgb, date_time))

                # p = multiprocessing.Process(target=imageSavefromFrame, args=(rgb, date_time))
                # p.start()

                # update the list of names

        # if (len(temp1) > 4):
        #     with concurrent.futures.ThreadPoolExecutor() as executor:
        #         results = executor.map(imageSavefromFrame, temp1)
        #         for result in results:
        #             print(result)
        # temp1.clear()
        # print("Here")

        names.append(name)

    if (not found):
        counter += 1
        if (counter > 10):
            if (unknownFaces + knownFaces > 0 and (unknownFaces / (unknownFaces + knownFaces)) * 100 > 80):
                print("Detected unknown person!")
            # if __name__ == '__main__':
            #     with concurrent.futures.ProcessPoolExecutor() as executor:
            #         results = executor.map(imageSavefromFrame, images_to_save)
            unknownFaces = 0
            knownFaces = 0
            # shutil.rmtree("temp")
            # os.mkdir("temp")
            images_to_save.clear()

    print(unknownFaces, knownFaces)
    return 123

if __name__ == '__main__':
    processes = []
    # load the known faces and embeddings
    print("[INFO] loading encodings...")
    data = pickle.loads(open(args["encodings"], "rb").read())

    # initialize the video stream and pointer to output video file, then
    # allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    while True:

        # if (len(processes) == 0):
        #     print("Hello")
        while (len(processes) < 10):
            frame = vs.read()
            # p = multiprocessing.Process(target=get_frame, args=[frame, data])
            # processes.append(p)
            processes.append([frame,data])
            #
            # if (len(processes) > 10):
            #     print("In here")

            # for process in processes:
            #     process.start()
        print(len(processes))
        print(len(processes[0]))
        t = []
        for p in processes:
            pp = threading.Thread(target=get_frame, args=p)
            pp.start()
            t.append(pp)
        for p in t:
            p.join()
        # with concurrent.futures.ThreadPoolExecutor() as executor:

            # results = executor.map(get_frame, processes)
            # for result in results:
            #     print(result)
            # processes.clear()
        # else:
        #     print("Hello2")
        #
        #     i = 0
        #     while (len(processes) > 0):
        #         if (not processes[i].is_alive()):
        #             del processes[i]
        #             i-=1
        #         i += 1
        # if (i >= len(processes)):
        #     break

        # cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanupqq
    cv2.destroyAllWindows()
    vs.stop()
