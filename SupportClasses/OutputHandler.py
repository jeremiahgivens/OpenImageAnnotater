import os
import glob
import shutil


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
            unlabeledPath = os.path.join(tempPath, 'unlabeled')
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
            for form in imgFormats:
                files.append(glob.glob(os.path.join(pathToImageFolder, form)))

            # Need this as one string array. There is probably a more optimal way so,
            # TODO Find the Pythonic way of doing this.

            combinedFiles = files[0]
            for f in range(1, len(files)):
                combinedFiles += files[f]

            for f in combinedFiles:
                shutil.copy(f, unlabeledPath)


    def buildOutputFolder(self):
        pass

    def setOutputFormat(self, format):
        pass
