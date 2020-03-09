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
    print("asdfg", arr)
    # print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    cv2.imwrite(arr[1], arr[0])
    image = Image.open(arr[1]).rotate(270, expand=True)
    image.thumbnail((600, 468), Image.ANTIALIAS)
    image.save(arr[1], quality=40, optimize=True)
    print(arr[1])
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

# load the known faces and embeddings
print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

# initialize the video stream and pointer to output video file, then
# allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
writer = None

found = False
unknownFaces = 0
knownFaces = 0
counter = 0
p = None
# loop over frames from the video file stream

temp1 = []
while True:
    # grab the frame from the threaded video stream
    frame = vs.read()

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
            print(counts[max(counts, key=counts.get)])
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
                temp1.append([rgb, date_time])
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

        print("Size: ", len(temp1))
        print(temp1)
        names.append(name)

    if (not found):
        counter += 1
        if (counter > 10):
            if (unknownFaces + knownFaces > 0 and (unknownFaces / (unknownFaces + knownFaces)) * 100 > 80):
                print("Detected unknown person!")

            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = executor.map(imageSavefromFrame, temp1)
            unknownFaces = 0
            knownFaces = 0
            # shutil.rmtree("temp")
            # os.mkdir("temp")
            temp1.clear()

    print(unknownFaces, knownFaces)

    # # loop over the recognized faces
    # for ((top, right, bottom, left), name) in zip(boxes, names):
    #     # rescale the face coordinates
    #     top = int(top * r)
    #     right = int(right * r)
    #     bottom = int(bottom * r)
    #     left = int(left * r)
    #
    #     # draw the predicted face name on the image
    #     cv2.rectangle(frame, (left, top), (right, bottom),
    #                   (0, 255, 0), 2)
    #     y = top - 15 if top - 15 > 15 else top + 15
    #     cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
    #                 0.75, (0, 255, 0), 2)

    # if the video writer is None *AND* we are supposed to write
    # the output video to disk initialize the writer
    if writer is None and args["output"] is not None:
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter(args["output"], fourcc, 20,
                                 (frame.shape[1], frame.shape[0]), True)

    # if the writer is not None, write the frame with recognized
    # faces t odisk
    if writer is not None:
        writer.write(frame)

    # check to see if we are supposed to display the output frame to
    # the screen
    if args["display"] > 0:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

# check to see if the video writer point needs to be released
if writer is not None:
    writer.release()
