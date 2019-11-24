from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameWaiting(object):
    def setupUi(self, FrameWaiting):
        FrameWaiting.setObjectName("FrameWaiting")
        FrameWaiting.setWindowModality(QtCore.Qt.ApplicationModal)
        FrameWaiting.resize(311, 147)
        FrameWaiting.setMinimumSize(QtCore.QSize(311, 147))
        FrameWaiting.setMaximumSize(QtCore.QSize(311, 147))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/icons/waiting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameWaiting.setWindowIcon(icon)

        FrameWaiting.setAutoFillBackground(False)
        self.labelWaiting = QtWidgets.QLabel(FrameWaiting)
        self.labelWaiting.setGeometry(QtCore.QRect(60, 30, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelWaiting.setFont(font)
        self.labelWaiting.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWaiting.setObjectName("labelWaiting")

        self.retranslateUi(FrameWaiting)
        QtCore.QMetaObject.connectSlotsByName(FrameWaiting)

    def retranslateUi(self, FrameWaiting):
        _translate = QtCore.QCoreApplication.translate
        FrameWaiting.setWindowTitle(_translate("FrameWaiting", "Пожалуйста, подождите..."))
        self.labelWaiting.setText(_translate("FrameWaiting", "Пожалуйста, подождите..."))
