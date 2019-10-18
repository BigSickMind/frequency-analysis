from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameSpectrogram(object):
    def setupUi(self, FrameSpectrogram):
        FrameSpectrogram.setObjectName("FrameSpectrogram")
        FrameSpectrogram.setWindowModality(QtCore.Qt.ApplicationModal)
        FrameSpectrogram.resize(800, 600)
        FrameSpectrogram.setMinimumSize(QtCore.QSize(600, 600))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/spectrogram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameSpectrogram.setWindowIcon(icon)

        self.imageLayout = QtWidgets.QVBoxLayout(FrameSpectrogram)
        self.imageLayout.setObjectName("imageLayout")
        self.imageWidget = QtWidgets.QWidget(FrameSpectrogram)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageWidget.sizePolicy().hasHeightForWidth())
        self.imageWidget.setSizePolicy(sizePolicy)
        self.imageWidget.setObjectName("imageWidget")
        self.imageLayout.addWidget(self.imageWidget)

        self.retranslateUi(FrameSpectrogram)
        QtCore.QMetaObject.connectSlotsByName(FrameSpectrogram)

    def retranslateUi(self, FrameSpectrogram):
        _translate = QtCore.QCoreApplication.translate
        FrameSpectrogram.setWindowTitle(_translate("FrameSpectrogram", "Спектрограмма"))
