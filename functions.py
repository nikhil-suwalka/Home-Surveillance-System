import os


def getAllAuthorizedNames():
    return os.listdir("dataset")


def getPicsByDirName(dirname):
    return os.listdir("dataset/" + dirname)



def addNewAuthorized(name):
    os.mkdir("dataset/" + name)
