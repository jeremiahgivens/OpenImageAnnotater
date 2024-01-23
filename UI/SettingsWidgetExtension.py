
from AutoGenerated.SettingsWidget import *
from PyQt6.QtWidgets import QFileDialog


class SettingsWidgetExtension(Ui_SettingsWidget):
    def __init__(self, outputHandler, modelHandler, videoDicer):
        self.outputHandler = outputHandler
        self.modelHandler = modelHandler
        self.videoDicer = videoDicer
        self.connectInputs()

    def connectInputs(self):
        self.browseOutputPath.clicked.connect(self.browseForOutputPath)
        self.browseModelPath.clicked.connect(self.browseForDetectionModelPath)
        self.importImageFolder.clicked.connect(self.browseForFolderOfImages)
        self.importVideo.clicked.connect(self.browseForVideo)
        self.importExisting.clicked.connect(self.browseForExistingAnnotatedSet)

    def browseForOutputPath(self):
        fname = QFileDialog.getExistingDirectory(None, 'Select your outpur folder', '../')
        self.outputPath.setText(fname)

    def browseForDetectionModelPath(self):
        fname = QFileDialog.getOpenFileName(None, 'Select your object detection model', '../')
        self.modelPath.setText(fname[0])

    def browseForFolderOfImages(self):
        fname = QFileDialog.getExistingDirectory(None, 'Select folder of images to import', '../')
        # Add methods for importing folder here.

    def browseForVideo(self):
        fname = QFileDialog.getOpenFileName(None, 'Select video to import', '../')
        # Add methods for importing folder here.

    def browseForExistingAnnotatedSet(self):
        fname = QFileDialog.getExistingDirectory(None, 'Select existing annotation set', '../')
        # Add code for importing existing labeled data.