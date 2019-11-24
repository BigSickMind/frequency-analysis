from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameAbout(object):
    def setupUi(self, FrameAbout):
        FrameAbout.setObjectName("FrameAbout")
        FrameAbout.setWindowModality(QtCore.Qt.ApplicationModal)
        FrameAbout.resize(490, 260)
        FrameAbout.setMinimumSize(QtCore.QSize(490, 260))
        FrameAbout.setMaximumSize(QtCore.QSize(490, 260))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameAbout.setWindowIcon(icon)
        self.textAbout = QtWidgets.QTextEdit(FrameAbout)
        self.textAbout.setGeometry(QtCore.QRect(0, 0, 491, 261))
        self.textAbout.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textAbout.setObjectName("textAbout")

        self.retranslateUi(FrameAbout)
        QtCore.QMetaObject.connectSlotsByName(FrameAbout)

    def retranslateUi(self, FrameAbout):
        _translate = QtCore.QCoreApplication.translate
        FrameAbout.setWindowTitle(_translate("FrameAbout", "О программе"))
        self.textAbout.setHtml(_translate("FrameAbout",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Частотный анализатор 2.0</span></p>\n"
                                          "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                          "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Частотный анализатор - программное обеспечение для спектрального анализа и анализа аудиофайлов расширения wav на предмет внесённых изменений.</span></p>\n"
                                          "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                          "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                          "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                          "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Авторы:</span></p>\n"
                                          "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                          "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Егор Смирнов, разработчик и тестер</span></p>\n"
                                          "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Алексей Гераськин, сооснователь и проектировщик</span></p>\n"
                                          "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                          "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                          "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Copyright © 2018-2020 Dream Analytics.</span></p></body></html>"))
