from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameError(object):
    def setupUi(self, FrameError):
        FrameError.setObjectName("FrameError")
        FrameError.setWindowModality(QtCore.Qt.ApplicationModal)
        FrameError.resize(500, 90)
        FrameError.setMinimumSize(QtCore.QSize(500, 90))
        FrameError.setMaximumSize(QtCore.QSize(500, 90))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/icons/error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameError.setWindowIcon(icon)

        self.buttonOk = QtWidgets.QPushButton(FrameError)
        self.buttonOk.setGeometry(QtCore.QRect(210, 50, 81, 31))
        self.buttonOk.setObjectName("buttonOk")
        self.labelError = QtWidgets.QLabel(FrameError)
        self.labelError.setGeometry(QtCore.QRect(50, 20, 400, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelError.setFont(font)
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.setObjectName("labelError")

        self.retranslateUi(FrameError)
        QtCore.QMetaObject.connectSlotsByName(FrameError)

    def retranslateUi(self, FrameError):
        _translate = QtCore.QCoreApplication.translate
        FrameError.setWindowTitle(_translate("FrameError", "Ошибка"))
        self.buttonOk.setText(_translate("FrameError", "ОК"))
        self.labelError.setText(_translate("FrameError", "TextLabel"))
