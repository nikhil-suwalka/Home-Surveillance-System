from imutils import paths
from PIL import Image
path = input("Enter the dir path: ")
imagePaths = list(paths.list_images(path))
for imgPath in imagePaths:
    image = Image.open(imgPath).rotate(270,expand=True)
    image.thumbnail((600,468), Image.ANTIALIAS)
    print(imgPath)
    image.save(imgPath,quality=70,optimize=True)
