from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameWaiting(object):
    def setupUi(self, FrameWaiting):
        FrameWaiting.setObjectName("FrameWaiting")
        FrameWaiting.setWindowModality(QtCore.Qt.ApplicationModal)
        FrameWaiting.resize(294, 143)
        FrameWaiting.setMinimumSize(QtCore.QSize(294, 143))
        FrameWaiting.setMaximumSize(QtCore.QSize(294, 143))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/waiting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameWaiting.setWindowIcon(icon)

        self.progressBar = QtWidgets.QProgressBar(FrameWaiting)
        self.progressBar.setGeometry(QtCore.QRect(50, 70, 211, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.labelWaiting = QtWidgets.QLabel(FrameWaiting)
        self.labelWaiting.setGeometry(QtCore.QRect(90, 40, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelWaiting.setFont(font)
        self.labelWaiting.setObjectName("labelWaiting")

        self.retranslateUi(FrameWaiting)
        QtCore.QMetaObject.connectSlotsByName(FrameWaiting)

    def retranslateUi(self, FrameWaiting):
        _translate = QtCore.QCoreApplication.translate
        FrameWaiting.setWindowTitle(_translate("FrameWaiting", "Подождите..."))
        self.labelWaiting.setText(_translate("FrameWaiting", "Подождите..."))
