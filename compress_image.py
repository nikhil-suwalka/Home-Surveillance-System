import argparse

from imutils import paths
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--img", required=False, help="argument to specify img path")
args = vars(ap.parse_args())
print("Argument: ",args)
imgPath = args["img"]
image = Image.open(imgPath)
image.thumbnail((600, 468), Image.ANTIALIAS)
print(imgPath)
image.save(imgPath, quality=70, optimize=True)
print("Done")