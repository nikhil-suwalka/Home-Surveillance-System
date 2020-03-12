# USAGE
# python recognize_faces_video.py --encodings encodings.pickle
# python recognize_faces_video.py --encodings encodings.pickle --output output/jurassic_park_trailer_output.avi --display 0

# import the necessary packages
import concurrent.futures
import os
import shutil
import json
import threading
from PIL import Image
from imutils.video import VideoStream
import face_recognition
import pickle
from datetime import datetime
import cv2
import shutil


# def imageSavefromFrame(rgb, date_time):
def imageSavefromFrame(arr):
    # print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    cv2.imwrite(arr[1], arr[0])
    image = Image.open(arr[1])
    # .rotate(270, expand=True)
    image.thumbnail((600, 468), Image.ANTIALIAS)
    image.save(arr[1], quality=40, optimize=True)
    print(arr[1])
    return arr[1]


args = {'encodings': 'encodings.pickle', 'output': None, 'display': 1, 'detection_method': 'cnn'}

# load the known faces and embeddings
print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

# initialize the video stream and pointer to output video file, then
# allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()

found = False
unknownFaces = 0
knownFaces = 0
counter = 0
p = None
detectedKnownFace = 0
# loop over frames from the video file stream

images_to_save = []
while True:
    # grab the frame from the threaded video stream
    frame = vs.read()

    # convert the input frame from BGR to RGB then resize it to have
    # a width of 750px (to speedup processing)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    rgb = cv2.resize(frame, (0, 0), fx=0.7, fy=0.7)
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
        now = datetime.now()

        if (now.second % 5 == 0):
            print("Take pic")
            date_time = "temp\\" + now.strftime("%d-%m-%Y_%H-%M-%S.%f") + ".png"
            images_to_save.append([rgb, date_time])
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
            threshold = round(data["names"].count(name) * 0.70)
            if (counts[max(counts, key=counts.get)] >= threshold):
                name = max(counts, key=counts.get)
                if (len(encodings) == 1 and counts[max(counts, key=counts.get)] >= round(data["names"].count(name))):
                    print("known")
                    detectedKnownFace += 1
                    if (detectedKnownFace >= 5):
                        f = open("known_face_save_tracker.txt", "r+")
                        json_string = f.read()

                        detectedKnownFace = 0
                        if (len(json_string) > 0):
                            json_array = json.loads(json_string)
                        else:
                            json_array = json.loads("{}")
                        if (name in json_array.keys()):
                            if (json_array[name] != now.strftime("%d-%m-%Y")):
                                json_array[name] = now.strftime("%d-%m-%Y")
                                arg = [rgb, "dataset\\" + name + "\\" + now.strftime("%d-%m-%Y_%H-%M-%S.%f") + ".png"]
                                threading.Thread(target=imageSavefromFrame, args=[arg]).start()

                        else:
                            json_array[name] = now.strftime("%d-%m-%Y")

                        print("Json-array: ", json_array)
                        f.truncate()
                        f.seek(0)
                        f.write(json.dumps(json_array))
                        f.close()

            else:
                name = "Unknown"
                detectedKnownFace = 0
            if (name == "Unknown"):
                unknownFaces += 1
            else:
                knownFaces += 1
                counter = 0

            # # TODO solve critical section problem

        names.append(name)

    if (not found):
        counter += 1
        if (counter > 30):
            if (unknownFaces + knownFaces > 0 and (unknownFaces / (unknownFaces + knownFaces)) * 100 > 80):
                print("Detected unknown person!")
            if __name__ == '__main__':
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    results = executor.map(imageSavefromFrame, images_to_save)
            unknownFaces = 0
            knownFaces = 0
            shutil.rmtree("temp")
            os.mkdir("temp")
            images_to_save.clear()
            counter = 0

    print(unknownFaces, knownFaces)

    # loop over the recognized faces
    for ((top, right, bottom, left), name) in zip(boxes, names):
        # rescale the face coordinates
        top = int(top * r)
        right = int(right * r)
        bottom = int(bottom * r)
        left = int(left * r)

        # draw the predicted face name on the image
        cv2.rectangle(frame, (left, top), (right, bottom),
                      (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
