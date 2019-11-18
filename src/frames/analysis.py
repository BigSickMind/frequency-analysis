from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameAnalysis(object):
    def setupUi(self, FrameAnalysis):
        FrameAnalysis.setObjectName("FrameAnalysis")
        FrameAnalysis.setWindowModality(QtCore.Qt.ApplicationModal)
        FrameAnalysis.resize(800, 600)
        FrameAnalysis.setMinimumSize(QtCore.QSize(600, 600))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/analysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameAnalysis.setWindowIcon(icon)

        self.imageLayout = QtWidgets.QVBoxLayout(FrameAnalysis)
        self.imageLayout.setObjectName("imageLayout")
        self.imageWidget = QtWidgets.QWidget(FrameAnalysis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageWidget.sizePolicy().hasHeightForWidth())
        self.imageWidget.setSizePolicy(sizePolicy)
        self.imageWidget.setObjectName("imageWidget")
        self.imageLayout.addWidget(self.imageWidget)

        self.retranslateUi(FrameAnalysis)
        QtCore.QMetaObject.connectSlotsByName(FrameAnalysis)

    def retranslateUi(self, FrameAnalysis):
        _translate = QtCore.QCoreApplication.translate
        FrameAnalysis.setWindowTitle(_translate("FrameAnalysis", "Анализ"))
