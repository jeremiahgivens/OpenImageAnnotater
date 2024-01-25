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
            rootPath = os.path.join(self.path, 'data')
            if ~os.path.exists(rootPath):
                os.makedirs(rootPath)


    def addImageToFolder(self, path):
        pass

    def buildOutputFolder(self):
        pass

    def setOutputFormat(self, format):
        pass
