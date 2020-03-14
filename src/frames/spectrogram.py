from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameSpectrogram(object):
    def setupUi(self, FrameSpectrogram):
        FrameSpectrogram.setObjectName("FrameSpectrogram")
        FrameSpectrogram.resize(800, 600)
        FrameSpectrogram.setMinimumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/icons/spectrogram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameSpectrogram.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FrameSpectrogram)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageLayout = QtWidgets.QVBoxLayout()
        self.imageLayout.setObjectName("imageLayout")
        self.imageWidget = QtWidgets.QWidget(self.centralwidget)
        self.imageWidget.setObjectName("imageWidget")
        self.imageLayout.addWidget(self.imageWidget)
        self.verticalLayout.addLayout(self.imageLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonOk = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOk.setObjectName("buttonOk")
        self.horizontalLayout.addWidget(self.buttonOk)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 12)
        self.verticalLayout.setStretch(1, 1)
        FrameSpectrogram.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrameSpectrogram)
        QtCore.QMetaObject.connectSlotsByName(FrameSpectrogram)

    def retranslateUi(self, FrameSpectrogram):
        _translate = QtCore.QCoreApplication.translate
        FrameSpectrogram.setWindowTitle(_translate("FrameSpectrogram", "Спектрограмма"))
        self.buttonOk.setText(_translate("FrameSpectrogram", "OK"))
