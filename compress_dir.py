import argparse

from imutils import paths
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=False, help="argument to specify dir name")
args = vars(ap.parse_args())
print("Argument: ",args)
imagePaths = list(paths.list_images(args["dir"]))
for imgPath in imagePaths:
    image = Image.open(imgPath)
    image.thumbnail((600, 468), Image.ANTIALIAS)
    print(imgPath)
    image.save(imgPath, quality=70, optimize=True)
print("Done")