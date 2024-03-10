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
        self.image_qt = None
        self.pic = None

    def resizeImage(self):
        if self.image_qt is not None and self.pic is not None:
            pixMap = QPixmap.fromImage(self.image_qt)
            gvSize = self.graphicsView.size()
            pixMap = pixMap.scaled(gvSize.width(), gvSize.height(), Qt.AspectRatioMode.KeepAspectRatio)
            self.pic.setPixmap(pixMap)
            print("Resizing")

    def load(self):
        path = self.outputHandler.getPathToFirstImage()
        if os.path.exists(path):
            self.image_qt = QImage(path)
            self.pic = QGraphicsPixmapItem()
            pixMap = QPixmap.fromImage(self.image_qt)
            gvSize = self.graphicsView.size()
            pixMap = pixMap.scaled(gvSize.width(), gvSize.height(), Qt.AspectRatioMode.KeepAspectRatio)
            self.pic.setPixmap(pixMap)
            self.scene.addItem(self.pic)
        else:
            print("Issue loading image in graphics view. See ImageAnnotator load method.")