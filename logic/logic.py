import sys

from frames.main import Ui_FrameDefault

from PyQt5.QtWidgets import *


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.path = ""
        self.filename = ""

        self.ui = Ui_FrameDefault()
        self.FrameDefault = self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open_file)
        # self.ui.actionClose.triggered.connect(self.close_file)
        self.ui.actionExit.triggered.connect(self.exit)

        # self.ui.actionAbout.triggered.connect(self.about)

        self.show()

    @staticmethod
    def exit():
        sys.exit()

    def open_file(self):
        options = QFileDialog.Options()
        self.path, _ = QFileDialog.getOpenFileName(self, "Выберите аудиофайл", "",
                                                   "All Files (*);;VLC media file (*.wav *.mp3 *.ogg *.flac *.aiff)",
                                                   options=options)
        self.filename = self.path[(self.path.rfind('/') + 1):self.path.rfind('.')]

        self.ui.renameWindowTitle(self.FrameDefault, self.path)

        # if correct file

        self.ui.actionInfo.setEnabled(True)
        self.ui.actionSpectre.setEnabled(True)
        self.ui.actionAnalysis.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()

    sys.exit(app.exec_())

# return FrameDefault
#
# def renameWindowTitle(self, FrameDefault, path):
#     _translate = QtCore.QCoreApplication.translate
#     FrameDefault.setWindowTitle(_translate("FrameDefault", "Частотный анализатор ({})".format(path)))
