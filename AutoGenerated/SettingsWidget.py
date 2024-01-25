# Form implementation generated from reading ui file './UIDesignerFiles/settingsWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        SettingsWidget.setObjectName("SettingsWidget")
        SettingsWidget.resize(500, 402)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(SettingsWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.browseOutputPath = QtWidgets.QPushButton(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseOutputPath.sizePolicy().hasHeightForWidth())
        self.browseOutputPath.setSizePolicy(sizePolicy)
        self.browseOutputPath.setObjectName("browseOutputPath")
        self.verticalLayout_2.addWidget(self.browseOutputPath)
        self.browseModelPath = QtWidgets.QPushButton(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseModelPath.sizePolicy().hasHeightForWidth())
        self.browseModelPath.setSizePolicy(sizePolicy)
        self.browseModelPath.setObjectName("browseModelPath")
        self.verticalLayout_2.addWidget(self.browseModelPath)
        self.outputFormat = QtWidgets.QComboBox(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputFormat.sizePolicy().hasHeightForWidth())
        self.outputFormat.setSizePolicy(sizePolicy)
        self.outputFormat.setObjectName("outputFormat")
        self.outputFormat.addItem("")
        self.outputFormat.addItem("")
        self.verticalLayout_2.addWidget(self.outputFormat)
        self.importImageFolder = QtWidgets.QPushButton(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importImageFolder.sizePolicy().hasHeightForWidth())
        self.importImageFolder.setSizePolicy(sizePolicy)
        self.importImageFolder.setMinimumSize(QtCore.QSize(0, 32))
        self.importImageFolder.setBaseSize(QtCore.QSize(0, 0))
        self.importImageFolder.setObjectName("importImageFolder")
        self.verticalLayout_2.addWidget(self.importImageFolder)
        self.importVideo = QtWidgets.QPushButton(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importVideo.sizePolicy().hasHeightForWidth())
        self.importVideo.setSizePolicy(sizePolicy)
        self.importVideo.setMinimumSize(QtCore.QSize(0, 32))
        self.importVideo.setObjectName("importVideo")
        self.verticalLayout_2.addWidget(self.importVideo)
        self.importExisting = QtWidgets.QPushButton(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importExisting.sizePolicy().hasHeightForWidth())
        self.importExisting.setSizePolicy(sizePolicy)
        self.importExisting.setMinimumSize(QtCore.QSize(0, 32))
        self.importExisting.setObjectName("importExisting")
        self.verticalLayout_2.addWidget(self.importExisting)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.outputPath = QtWidgets.QLineEdit(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputPath.sizePolicy().hasHeightForWidth())
        self.outputPath.setSizePolicy(sizePolicy)
        self.outputPath.setObjectName("outputPath")
        self.verticalLayout_4.addWidget(self.outputPath)
        self.modelPath = QtWidgets.QLineEdit(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelPath.sizePolicy().hasHeightForWidth())
        self.modelPath.setSizePolicy(sizePolicy)
        self.modelPath.setObjectName("modelPath")
        self.verticalLayout_4.addWidget(self.modelPath)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=SettingsWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 20)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 20)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.classList = QtWidgets.QListWidget(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.classList.sizePolicy().hasHeightForWidth())
        self.classList.setSizePolicy(sizePolicy)
        self.classList.setObjectName("classList")
        self.verticalLayout_3.addWidget(self.classList)
        self.lineEdit = QtWidgets.QLineEdit(parent=SettingsWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addClass = QtWidgets.QPushButton(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addClass.sizePolicy().hasHeightForWidth())
        self.addClass.setSizePolicy(sizePolicy)
        self.addClass.setObjectName("addClass")
        self.horizontalLayout_3.addWidget(self.addClass)
        self.deleteClass = QtWidgets.QPushButton(parent=SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteClass.sizePolicy().hasHeightForWidth())
        self.deleteClass.setSizePolicy(sizePolicy)
        self.deleteClass.setObjectName("deleteClass")
        self.horizontalLayout_3.addWidget(self.deleteClass)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 30)
        self.verticalLayout_3.setStretch(3, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.horizontalSlider = QtWidgets.QSlider(parent=SettingsWidget)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(80)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        self.label_4 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.horizontalSlider_2 = QtWidgets.QSlider(parent=SettingsWidget)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setSliderPosition(20)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_6.addWidget(self.horizontalSlider_2)
        self.label_11 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.horizontalSlider_3 = QtWidgets.QSlider(parent=SettingsWidget)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalLayout_7.addWidget(self.horizontalSlider_3)
        self.label_13 = QtWidgets.QLabel(parent=SettingsWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.confirmSettings = QtWidgets.QPushButton(parent=SettingsWidget)
        self.confirmSettings.setObjectName("confirmSettings")
        self.verticalLayout_5.addWidget(self.confirmSettings)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 20)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(SettingsWidget)

    def retranslateUi(self, SettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        SettingsWidget.setWindowTitle(_translate("SettingsWidget", "Setup"))
        self.browseOutputPath.setText(_translate("SettingsWidget", "Output Path"))
        self.browseModelPath.setText(_translate("SettingsWidget", "Detection Model"))
        self.outputFormat.setItemText(0, _translate("SettingsWidget", "YOLOv8"))
        self.outputFormat.setItemText(1, _translate("SettingsWidget", "YOLOv5"))
        self.importImageFolder.setText(_translate("SettingsWidget", "Import Image Folder"))
        self.importVideo.setText(_translate("SettingsWidget", "Import Video"))
        self.importExisting.setText(_translate("SettingsWidget", "Combine WIth Another Project"))
        self.label.setText(_translate("SettingsWidget", "Number of images:"))
        self.label_3.setText(_translate("SettingsWidget", "Number of labeled images:"))
        self.label_6.setText(_translate("SettingsWidget", "Number of unlabeled images:"))
        self.label_7.setText(_translate("SettingsWidget", "0"))
        self.label_8.setText(_translate("SettingsWidget", "0"))
        self.label_9.setText(_translate("SettingsWidget", "0"))
        self.label_2.setText(_translate("SettingsWidget", "Class Labels"))
        self.addClass.setText(_translate("SettingsWidget", "Add"))
        self.deleteClass.setText(_translate("SettingsWidget", "Delete"))
        self.label_5.setText(_translate("SettingsWidget", "train"))
        self.label_4.setText(_translate("SettingsWidget", "80% "))
        self.label_10.setText(_translate("SettingsWidget", "valid"))
        self.label_11.setText(_translate("SettingsWidget", "20% "))
        self.label_12.setText(_translate("SettingsWidget", "test"))
        self.label_13.setText(_translate("SettingsWidget", "0%  "))
        self.confirmSettings.setText(_translate("SettingsWidget", "Confirm Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWidget = QtWidgets.QWidget()
    ui = Ui_SettingsWidget()
    ui.setupUi(SettingsWidget)
    SettingsWidget.show()
    sys.exit(app.exec())
