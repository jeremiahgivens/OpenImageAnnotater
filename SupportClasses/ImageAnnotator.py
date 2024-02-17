from PyQt6.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsScene
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt
import os

class ImageAnnotator():
    def __init__(self, outputHandler, graphicsView):
        self.outputHandler = outputHandler
        self.graphicsView = graphicsView
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

    def load(self):
        path = self.outputHandler.getPathToFirstImage()
        if os.path.exists(path):
            self.image_qt = QImage(path)
            pic = QGraphicsPixmapItem()
            pixMap = QPixmap.fromImage(self.image_qt)
            gvSize = self.graphicsView.size()
            pixMap = pixMap.scaled(gvSize.width(), gvSize.height(), Qt.AspectRatioMode.KeepAspectRatio)
            pic.setPixmap(pixMap)
            self.scene.addItem(pic)
            print("Image added to graphics view.")
        else:
            print("Issue loading image in graphics view. See ImageAnnotator load method.")