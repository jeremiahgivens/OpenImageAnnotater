import os


class OutputHandler():
    def __init__(self):
        self.path = ''

    def setOutputFolderPath(self, path) -> bool:
        pathIsValid = os.path.exists(path)
        if pathIsValid:
            self.path = path
        return pathIsValid

    def setUpFolder(self):
        if os.path.exists(self.path):
            testPath = os.path.join(self.path, 'test')
            self.makeImagesAndLabelsFolder(self.path, 'test')
            self.makeImagesAndLabelsFolder(self.path, 'valid')
            self.makeImagesAndLabelsFolder(self.path, 'train')

            tempPath = os.path.join(self.path, 'temp')
            self.makeDirIfNonExistent(tempPath)

    def makeDirIfNonExistent(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def makeImagesAndLabelsFolder(self, root, name):
        path = testPath = os.path.join(root, name)
        self.makeDirIfNonExistent(path)
        imagesPath = os.path.join(path, 'images')
        labelsPath = os.path.join(path, 'labels')
        self.makeDirIfNonExistent(imagesPath)
        self.makeDirIfNonExistent(labelsPath)


    def addImageToFolder(self, path):
        pass

    def buildOutputFolder(self):
        pass

    def setOutputFormat(self, format):
        pass
