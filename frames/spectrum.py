from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameSpectrum(object):
    def setupUi(self, FrameSpectrum):
        FrameSpectrum.setObjectName("FrameSpectrum")
        FrameSpectrum.setWindowModality(QtCore.Qt.ApplicationModal)
        FrameSpectrum.resize(693, 470)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/spectrum.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameSpectrum.setWindowIcon(icon)

        self.retranslateUi(FrameSpectrum)
        QtCore.QMetaObject.connectSlotsByName(FrameSpectrum)

    def retranslateUi(self, FrameSpectrum):
        _translate = QtCore.QCoreApplication.translate
        FrameSpectrum.setWindowTitle(_translate("FrameSpectrum", "График спектра"))
