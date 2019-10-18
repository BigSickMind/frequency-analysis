from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameDefault(object):
    def setupUi(self, FrameDefault):
        FrameDefault.setObjectName("FrameDefault")
        FrameDefault.setWindowModality(QtCore.Qt.NonModal)
        FrameDefault.resize(900, 600)
        FrameDefault.setMinimumSize(QtCore.QSize(900, 600))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameDefault.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(FrameDefault)
        self.centralwidget.setObjectName("centralwidget")
        self.imageLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.imageLayout.setObjectName("imageLayout")
        self.imageWidget = QtWidgets.QWidget(self.centralwidget)
        self.imageWidget.setObjectName("imageWidget")
        self.imageLayout.addWidget(self.imageWidget)
        FrameDefault.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrameDefault)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_analysis = QtWidgets.QMenu(self.menubar)
        self.menu_analysis.setObjectName("menu_analysis")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        FrameDefault.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrameDefault)
        self.statusbar.setObjectName("statusbar")
        FrameDefault.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(FrameDefault)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(FrameDefault)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(FrameDefault)
        self.actionExit.setObjectName("actionExit")
        self.actionHeader = QtWidgets.QAction(FrameDefault)
        self.actionHeader.setCheckable(False)
        self.actionHeader.setChecked(False)
        self.actionHeader.setEnabled(False)
        self.actionHeader.setObjectName("actionHeader")
        self.actionSpectrum = QtWidgets.QAction(FrameDefault)
        self.actionSpectrum.setEnabled(False)
        self.actionSpectrum.setObjectName("actionSpectrum")
        self.actionAnalysis = QtWidgets.QAction(FrameDefault)
        self.actionAnalysis.setEnabled(False)
        self.actionAnalysis.setObjectName("actionAnalysis")
        self.actionHelp = QtWidgets.QAction(FrameDefault)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSpectrogram = QtWidgets.QAction(FrameDefault)
        self.actionSpectrogram.setEnabled(False)
        self.actionSpectrogram.setObjectName("actionSpectrogram")
        self.menu_file.addAction(self.actionOpen)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionExit)
        self.menu_analysis.addAction(self.actionHeader)
        self.menu_analysis.addAction(self.actionSpectrogram)
        self.menu_analysis.addAction(self.actionSpectrum)
        self.menu_analysis.addSeparator()
        self.menu_analysis.addAction(self.actionAnalysis)
        self.menu_help.addAction(self.actionHelp)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_analysis.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(FrameDefault)
        QtCore.QMetaObject.connectSlotsByName(FrameDefault)

        return FrameDefault

    def retranslateUi(self, FrameDefault):
        _translate = QtCore.QCoreApplication.translate
        FrameDefault.setWindowTitle(_translate("FrameDefault", "Частотный анализатор"))
        self.menu_file.setTitle(_translate("FrameDefault", "Файл"))
        self.menu_analysis.setTitle(_translate("FrameDefault", "Анализ"))
        self.menu_help.setTitle(_translate("FrameDefault", "Справка"))
        self.actionAbout.setText(_translate("FrameDefault", "О программе..."))
        self.actionAbout.setStatusTip(_translate("FrameDefault", "О программе"))
        self.actionOpen.setText(_translate("FrameDefault", "Открыть файл"))
        self.actionOpen.setStatusTip(_translate("FrameDefault", "Открыть файл"))
        self.actionOpen.setShortcut(_translate("FrameDefault", "Ctrl+O"))
        self.actionExit.setText(_translate("FrameDefault", "Выход"))
        self.actionExit.setStatusTip(_translate("FrameDefault", "Выход из программы"))
        self.actionExit.setShortcut(_translate("FrameDefault", "Ctrl+Q"))
        self.actionHeader.setText(_translate("FrameDefault", "Данные из заголовка"))
        self.actionHeader.setStatusTip(_translate("FrameDefault", "Данные из заголовка"))
        self.actionSpectrum.setText(_translate("FrameDefault", "График спектра"))
        self.actionSpectrum.setStatusTip(_translate("FrameDefault", "График спектра"))
        self.actionAnalysis.setText(_translate("FrameDefault", "Начать анализ"))
        self.actionAnalysis.setStatusTip(_translate("FrameDefault", "Анализ на наличие внесённых изменений"))
        self.actionHelp.setText(_translate("FrameDefault", "Справка"))
        self.actionHelp.setShortcut(_translate("FrameDefault", "F1"))
        self.actionSpectrogram.setText(_translate("FrameDefault", "Спектрограмма"))
        self.actionSpectrogram.setStatusTip(_translate("FrameDefault", "Спектрограмма"))

    def renameWindowTitle(self, FrameDefault, path=""):
        if not path:
            title = "Частотный анализатор"
        else:
            title = "Частотный анализатор ({})".format(path)

        _translate = QtCore.QCoreApplication.translate
        FrameDefault.setWindowTitle(_translate("FrameDefault", title))
