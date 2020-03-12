import json

# f = open("known_face_save_tracker.txt", "r+")

# json_array = json.loads(f.read())
# f.truncate(0)
# f.seek(0)
# f.write("zxc")


# json_array["Nikhil_suwalka"] = "asdfghjkl"
# print(json_array)
# aa = json.dumps(json_array)
# print(aa)
# f.close()
#
# f = open("known_face_save_tracker.txt", "w+")
# f.write("a")
# f.write(json.dumps(json_array))
# f.close()
import os

files_count = len(next(os.walk("knownimages"))[2])
print(files_count)
