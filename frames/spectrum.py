from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameSpectrum(object):
    def setupUi(self, FrameSpectrum):
        FrameSpectrum.setObjectName("FrameSpectrum")
        FrameSpectrum.setWindowModality(QtCore.Qt.ApplicationModal)
        FrameSpectrum.resize(800, 600)
        FrameSpectrum.setMinimumSize(QtCore.QSize(600, 600))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/spectrum.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameSpectrum.setWindowIcon(icon)

        self.imageLayout = QtWidgets.QVBoxLayout(FrameSpectrum)
        self.imageLayout.setObjectName("imageLayout")
        self.imageWidget = QtWidgets.QWidget(FrameSpectrum)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageWidget.sizePolicy().hasHeightForWidth())
        self.imageWidget.setSizePolicy(sizePolicy)
        self.imageWidget.setObjectName("imageWidget")
        self.imageLayout.addWidget(self.imageWidget)

        self.retranslateUi(FrameSpectrum)
        QtCore.QMetaObject.connectSlotsByName(FrameSpectrum)

    def retranslateUi(self, FrameSpectrum):
        _translate = QtCore.QCoreApplication.translate
        FrameSpectrum.setWindowTitle(_translate("FrameSpectrum", "График спектра"))
