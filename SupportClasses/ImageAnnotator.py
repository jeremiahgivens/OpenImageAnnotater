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

    def load(self):
        path = self.outputHandler.getPathToFirstImage()
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