# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GoogleDrive\Courseworks\4_coursework\Practice\Frequency_analysis\UiFiles\FrequencyForm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1042, 740)
        MainForm.setMinimumSize(QtCore.QSize(1042, 740))
        MainForm.setMaximumSize(QtCore.QSize(1042, 740))
        self.open_btn = QtWidgets.QPushButton(MainForm)
        self.open_btn.setGeometry(QtCore.QRect(20, 700, 111, 31))
        self.open_btn.setObjectName("open_btn")
        self.exit_btn = QtWidgets.QPushButton(MainForm)
        self.exit_btn.setGeometry(QtCore.QRect(910, 700, 111, 31))
        self.exit_btn.setObjectName("exit_btn")
        self.analysis_btn = QtWidgets.QPushButton(MainForm)
        self.analysis_btn.setGeometry(QtCore.QRect(680, 700, 211, 31))
        self.analysis_btn.setObjectName("analysis_btn")
        self.path_line = QtWidgets.QLineEdit(MainForm)
        self.path_line.setGeometry(QtCore.QRect(140, 700, 521, 31))
        self.path_line.setObjectName("path_line")
        self.tabWidget = QtWidgets.QTabWidget(MainForm)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1042, 691))
        self.tabWidget.setMinimumSize(QtCore.QSize(1042, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(1042, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.parameters_tab = QtWidgets.QWidget()
        self.parameters_tab.setAccessibleName("")
        self.parameters_tab.setObjectName("parameters_tab")
        self.parameters_text = QtWidgets.QTextEdit(self.parameters_tab)
        self.parameters_text.setGeometry(QtCore.QRect(-1, -1, 1042, 664))
        self.parameters_text.setMinimumSize(QtCore.QSize(1042, 0))
        self.parameters_text.setMaximumSize(QtCore.QSize(1042, 16777215))
        self.parameters_text.setObjectName("parameters_text")
        self.tabWidget.addTab(self.parameters_tab, "")
        self.wave_tab = QtWidgets.QWidget()
        self.wave_tab.setObjectName("wave_tab")
        self.wave_image = QtWidgets.QLabel(self.wave_tab)
        self.wave_image.setGeometry(QtCore.QRect(0, 0, 1042, 664))
        self.wave_image.setMinimumSize(QtCore.QSize(1042, 0))
        self.wave_image.setMaximumSize(QtCore.QSize(1042, 16777215))
        self.wave_image.setText("")
        self.wave_image.setObjectName("wave_image")
        self.tabWidget.addTab(self.wave_tab, "")
        self.fft_tab = QtWidgets.QWidget()
        self.fft_tab.setObjectName("fft_tab")
        self.fft_image = QtWidgets.QLabel(self.fft_tab)
        self.fft_image.setGeometry(QtCore.QRect(0, 0, 1042, 664))
        self.fft_image.setMinimumSize(QtCore.QSize(1042, 0))
        self.fft_image.setMaximumSize(QtCore.QSize(1042, 16777215))
        self.fft_image.setText("")
        self.fft_image.setObjectName("fft_image")
        self.tabWidget.addTab(self.fft_tab, "")
        self.analysis_tab = QtWidgets.QWidget()
        self.analysis_tab.setObjectName("analysis_tab")
        self.gssnr_image = QtWidgets.QLabel(self.analysis_tab)
        self.gssnr_image.setGeometry(QtCore.QRect(0, 0, 1042, 664))
        self.gssnr_image.setMinimumSize(QtCore.QSize(1042, 0))
        self.gssnr_image.setMaximumSize(QtCore.QSize(1042, 16777215))
        self.gssnr_image.setText("")
        self.gssnr_image.setObjectName("gssnr_image")
        self.tabWidget.addTab(self.analysis_tab, "")

        self.retranslateUi(MainForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Частотный анализатор"))
        self.open_btn.setText(_translate("MainForm", "Выбрать файл"))
        self.exit_btn.setText(_translate("MainForm", "Выход"))
        self.analysis_btn.setText(_translate("MainForm", "Начать анализ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parameters_tab), _translate("MainForm", "Информация об аудиофайле"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wave_tab), _translate("MainForm", "Wav-волна аудиофайла"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fft_tab), _translate("MainForm", "Спектральный анализ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysis_tab), _translate("MainForm", "Коэффициент GSSNR"))

