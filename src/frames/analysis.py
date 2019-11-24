from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameAnalysis(object):
    def setupUi(self, FrameAnalysis):
        FrameAnalysis.setObjectName("FrameAnalysis")
        FrameAnalysis.setWindowModality(QtCore.Qt.ApplicationModal)
        FrameAnalysis.resize(800, 600)
        FrameAnalysis.setMinimumSize(QtCore.QSize(600, 600))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/icons/analysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameAnalysis.setWindowIcon(icon)

        self.imageLayout = QtWidgets.QVBoxLayout(FrameAnalysis)
        self.imageLayout.setObjectName("imageLayout")
        self.tabAnalysis = QtWidgets.QTabWidget(FrameAnalysis)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabAnalysis.setFont(font)
        self.tabAnalysis.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabAnalysis.setObjectName("tabAnalysis")
        self.tabGSSNR = QtWidgets.QWidget()
        self.tabGSSNR.setObjectName("tabGSSNR")
        self.GSSNRLayout = QtWidgets.QVBoxLayout(self.tabGSSNR)
        self.GSSNRLayout.setObjectName("GSSNRLayout")
        self.GSSNRWidget = QtWidgets.QWidget(self.tabGSSNR)
        self.GSSNRWidget.setObjectName("GSSNRWidget")
        self.GSSNRLayout.addWidget(self.GSSNRWidget)
        self.tabAnalysis.addTab(self.tabGSSNR, "")
        self.tabSSNR = QtWidgets.QWidget()
        self.tabSSNR.setObjectName("tabSSNR")
        self.SSNRLayout = QtWidgets.QVBoxLayout(self.tabSSNR)
        self.SSNRLayout.setObjectName("SSNRLayout")
        self.SSNRWidget = QtWidgets.QWidget(self.tabSSNR)
        self.SSNRWidget.setObjectName("SSNRWidget")
        self.SSNRLayout.addWidget(self.SSNRWidget)
        self.tabAnalysis.addTab(self.tabSSNR, "коэффициент SSNR")
        self.imageLayout.addWidget(self.tabAnalysis)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonOk = QtWidgets.QPushButton(FrameAnalysis)
        self.buttonOk.setObjectName("buttonOk")
        self.horizontalLayout.addWidget(self.buttonOk)
        self.imageLayout.addLayout(self.horizontalLayout)
        self.imageLayout.setStretch(0, 12)
        self.imageLayout.setStretch(1, 1)

        self.retranslateUi(FrameAnalysis)
        self.tabAnalysis.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FrameAnalysis)

    def retranslateUi(self, FrameAnalysis):
        _translate = QtCore.QCoreApplication.translate
        FrameAnalysis.setWindowTitle(_translate("FrameAnalysis", "Анализ"))
        self.tabAnalysis.setTabText(self.tabAnalysis.indexOf(self.tabGSSNR),
                                    _translate("FrameAnalysis", "коэффициент GSSNR"))
        self.buttonOk.setText(_translate("FrameAnalysis", "OK"))
