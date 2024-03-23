from PyQt6.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsScene, QWidget
from PyQt6.QtGui import QImage, QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt
import os


class PixMapItem(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        print("Mouse press event, x: " + str(event.pos().x()) + ", y: " + str(event.pos().y()))

    def mouseMoveEvent(self, event):
        print("Mouse move event, x: " + str(event.pos().x()) + ", y: " + str(event.pos().y()))


class ImageAnnotator():
    def __init__(self, outputHandler, graphicsView):
        self.outputHandler = outputHandler
        self.graphicsView = graphicsView
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.image_qt = None
        self.pic = None
        self.paths = []
        self.currentIndex = None

    def resizeImage(self):
        if self.image_qt is not None and self.pic is not None:
            pixMap = QPixmap.fromImage(self.image_qt)
            gvSize = self.graphicsView.size()
            pixMap = pixMap.scaled(gvSize.width(), gvSize.height(), Qt.AspectRatioMode.KeepAspectRatio)
            painter = QPainter(pixMap)
            painter.setPen(QColor(255, 34, 255, 255))
            painter.drawRect(10, 10, 10, 10)
            self.pic.setPixmap(pixMap)
            print("Resizing")

    def showNextImage(self):
        if self.currentIndex is None:
            self.currentIndex = 0
            self.showRandomImage()
        elif self.currentIndex == len(self.paths) - 1:
            self.currentIndex += 1
            self.showRandomImage()
        else:
            self.currentIndex += 1
            self.showImage(self.paths[self.currentIndex])

    def showPreviousImage(self):
        if self.currentIndex is None or self.currentIndex == 0:
            self.currentIndex = 0
            self.showRandomImage(isNext=False)
        else:
            self.currentIndex -= 1
            self.showImage(self.paths[self.currentIndex])

    def showRandomImage(self, isNext=True):
        path = self.outputHandler.getPathToRandomImage()
        if isNext:
            self.paths.append(path)
        else:
            self.paths.insert(0, path)

        self.showImage(path)

    def showImage(self, path):
        if os.path.exists(path):
            self.image_qt = QImage(path)
            self.pic = PixMapItem()
            pixMap = QPixmap.fromImage(self.image_qt)
            gvSize = self.graphicsView.size()
            pixMap = pixMap.scaled(gvSize.width(), gvSize.height(), Qt.AspectRatioMode.KeepAspectRatio)
            painter = QPainter(pixMap)
            painter.setPen(QColor(255, 34, 255, 255))
            painter.drawRect(10, 10, 10, 10)
            self.pic.setPixmap(pixMap)
            self.scene.addItem(self.pic)
        else:
            print("Issue loading image in graphics view. See ImageAnnotator load method.")