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
        self.imageLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.imageLayout.setObjectName("imageLayout")
        self.imageWidget = QtWidgets.QWidget(self.centralwidget)
        self.imageWidget.setObjectName("imageWidget")
        self.imageLayout.addWidget(self.imageWidget)
        FrameSpectrogram.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrameSpectrogram)
        QtCore.QMetaObject.connectSlotsByName(FrameSpectrogram)

    def retranslateUi(self, FrameSpectrogram):
        _translate = QtCore.QCoreApplication.translate
        FrameSpectrogram.setWindowTitle(_translate("FrameSpectrogram", "Спектрограмма"))
