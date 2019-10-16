from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameDefault(object):
    def setupUi(self, FrameDefault):
        FrameDefault.setObjectName("FrameDefault")
        FrameDefault.setWindowModality(QtCore.Qt.NonModal)
        FrameDefault.resize(900, 600)
        FrameDefault.setMinimumSize(QtCore.QSize(600, 400))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameDefault.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(FrameDefault)
        self.centralwidget.setObjectName("centralwidget")
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
        self.actionRecent = QtWidgets.QAction(FrameDefault)
        self.actionRecent.setObjectName("actionRecent")
        self.actionExit = QtWidgets.QAction(FrameDefault)
        self.actionExit.setObjectName("actionExit")
        self.actionHeader = QtWidgets.QAction(FrameDefault)
        self.actionHeader.setCheckable(False)
        self.actionHeader.setChecked(False)
        self.actionHeader.setEnabled(False)
        self.actionHeader.setObjectName("actionHeader")
        self.actionSpectre = QtWidgets.QAction(FrameDefault)
        self.actionSpectre.setEnabled(False)
        self.actionSpectre.setObjectName("actionSpectre")
        self.actionAnalysis = QtWidgets.QAction(FrameDefault)
        self.actionAnalysis.setEnabled(False)
        self.actionAnalysis.setObjectName("actionAnalysis")
        self.actionHelp = QtWidgets.QAction(FrameDefault)
        self.actionHelp.setObjectName("actionHelp")
        self.menu_file.addAction(self.actionOpen)
        self.menu_file.addAction(self.actionRecent)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionExit)
        self.menu_analysis.addAction(self.actionHeader)
        self.menu_analysis.addAction(self.actionSpectre)
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
        self.actionRecent.setText(_translate("FrameDefault", "Недавние"))
        self.actionExit.setText(_translate("FrameDefault", "Выход"))
        self.actionExit.setStatusTip(_translate("FrameDefault", "Выход из программы"))
        self.actionExit.setShortcut(_translate("FrameDefault", "Ctrl+Q"))
        self.actionHeader.setText(_translate("FrameDefault", "Данные из заголовка"))
        self.actionHeader.setStatusTip(_translate("FrameDefault", "Данные из заголовка"))
        self.actionSpectre.setText(_translate("FrameDefault", "График спектра"))
        self.actionSpectre.setStatusTip(_translate("FrameDefault", "График спектра"))
        self.actionAnalysis.setText(_translate("FrameDefault", "Начать анализ"))
        self.actionAnalysis.setStatusTip(_translate("FrameDefault", "Анализ на наличие внесённых изменений"))
        self.actionHelp.setText(_translate("FrameDefault", "Справка"))
        self.actionHelp.setShortcut(_translate("FrameDefault", "F1"))

    def renameWindowTitle(self, FrameDefault, path=""):
        if not path:
            title = "Частотный анализатор"
        else:
            title = "Частотный анализатор ({})".format(path)

        _translate = QtCore.QCoreApplication.translate
        FrameDefault.setWindowTitle(_translate("FrameDefault", title))