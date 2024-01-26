import os
import glob
import shutil
import numpy as np


class OutputHandler():
    def __init__(self):
        self.root = ''

    def setOutputFolderPath(self, path) -> bool:
        pathIsValid = os.path.exists(path)
        if pathIsValid:
            self.root = path
        return pathIsValid

    def setUpFolder(self):
        if os.path.exists(self.root):
            testPath = os.path.join(self.root, 'test')
            self.makeImagesAndLabelsFolder(self.root, 'test')
            self.makeImagesAndLabelsFolder(self.root, 'valid')
            self.makeImagesAndLabelsFolder(self.root, 'train')

            tempPath = os.path.join(self.root, 'temp')
            unlabeledPath = os.path.join(self.root, 'unlabeled')
            self.makeDirIfNonExistent(tempPath)
            self.makeDirIfNonExistent(unlabeledPath)

    def makeDirIfNonExistent(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def makeImagesAndLabelsFolder(self, root, name):
        path = os.path.join(root, name)
        self.makeDirIfNonExistent(path)
        imagesPath = os.path.join(path, 'images')
        labelsPath = os.path.join(path, 'labels')
        self.makeDirIfNonExistent(imagesPath)
        self.makeDirIfNonExistent(labelsPath)

    def importImageFolder(self, pathToImageFolder):
        if os.path.exists(self.root) and os.path.exists(pathToImageFolder):
            unlabeledPath = os.path.join(self.root, 'temp', 'unlabeled')

            print(unlabeledPath)
            
            files = []
            imgFormats = ['*.bmp', '*.dng', '*.jpeg', '*.jpg', '*.mpo', '*.png', '*.tif', '*.tiff', '*.webp', '*.pfm']
            for format in imgFormats:
                files.append(glob.glob(os.path.join(pathToImageFolder, format)))

            files = np.array(files)
            files = files.ravel()
            for f in files:
                shutil.copy(f, unlabeledPath)


    def buildOutputFolder(self):
        pass

    def setOutputFormat(self, format):
        pass
