import sys

from frames.main import Ui_FrameDefault

from logic.error import FrameError
from logic.header import FrameHeader, get_header

from PyQt5.QtWidgets import *


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.path = ""
        self.filename = ""

        self.ui = Ui_FrameDefault()
        self.FrameDefault = self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(self.exit)

        self.ui.actionHeader.triggered.connect(self.get_header)

        # self.ui.actionAbout.triggered.connect(self.about)

        self.show()

    @staticmethod
    def exit():
        sys.exit()

    def open_file(self):
        options = QFileDialog.Options()
        # TODO: default directory?
        directory = "D:/Github/frequency-analysis/tests/"
        # directory = ""
        self.path, _ = QFileDialog.getOpenFileName(self, "Выберите аудиофайл", directory,
                                                   "All Files (*);;VLC media file (*.wav *.mp3 *.ogg *.flac *.aiff)",
                                                   options=options)
        if self.path:
            self.filename = self.path[(self.path.rfind('/') + 1):self.path.rfind('.')]

            self.wav_info, self.message = get_header(self.path, self.filename)

            if not self.wav_info:
                self.error = FrameError(self.message)

                self.ui.renameWindowTitle(self.FrameDefault)

                self.ui.actionHeader.setEnabled(False)
                self.ui.actionSpectre.setEnabled(False)
                self.ui.actionAnalysis.setEnabled(False)
            else:
                self.ui.renameWindowTitle(self.FrameDefault, self.path)

                self.ui.actionHeader.setEnabled(True)
                self.ui.actionSpectre.setEnabled(True)
                self.ui.actionAnalysis.setEnabled(True)

    def get_header(self):
        self.info = FrameHeader(self.wav_info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()

    sys.exit(app.exec_())

# return FrameDefault
#
# def renameWindowTitle(self, FrameDefault, path=""):
#     if not path:
#         title = "Частотный анализатор"
#     else:
#         title = "Частотный анализатор ({})".format(path)
#
#     _translate = QtCore.QCoreApplication.translate
#     FrameDefault.setWindowTitle(_translate("FrameDefault", title))
