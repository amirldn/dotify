import os

def makefolder(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)
