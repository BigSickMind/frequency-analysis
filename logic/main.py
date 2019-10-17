import sys

from frames.main import Ui_FrameDefault

from logic.error import FrameError
from logic.header import FrameHeader, get_header
from logic.spectrum import FrameSpectrum

from PyQt5.QtWidgets import *
from PyQt5 import QtCore

MAX_ACTIONS = 8


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.ui = Ui_FrameDefault()
        self.FrameDefault = self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionClear.triggered.connect(self.clear_recent)
        self.ui.actionExit.triggered.connect(self.exit)

        self.ui.actionHeader.triggered.connect(self.get_header)
        self.ui.actionSpectrum.triggered.connect(self.plot_spectrum)
        self.ui.actionAnalysis.triggered.connect(self.frequency_analysis)

        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionAbout.triggered.connect(self.about)

        self.show()

    @staticmethod
    def exit():
        sys.exit()

    # TODO: Maybe need this shited shit
    def setActionName(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.actionRecent1.setText(self.path)

    def add_action(self):
        # TODO: create actions in ui, setVisible False and assign new files to these actions
        # TODO: insert recent files to the top, think about how save them

        # TODO: Don't need this shit, just a test
        actions = self.ui.menu_recent.actions()

        if len(actions) == 1:
            self.ui.menu_recent.addSeparator()

        # TODO: test add action
        self.ui.actionRecent1 = QAction(self.FrameDefault)
        self.ui.actionRecent1.setObjectName("actionRecent1")
        self.ui.menu_recent.addAction(self.ui.actionRecent1)
        self.setActionName()

        self.ui.actionRecent1.triggered.connect(self.get_action1)

        if not self.ui.actionClear.isEnabled():
            self.ui.actionClear.setEnabled(True)

        # print(self.ui.menu_recent.actions())

        # for action in actions:
        #     if action.isSeparator():
        #         print(1)
        #     else:
        #         print(2)

        # for action in self.ui.menu_recent.actions():
        #     print(action)

    # TODO: Don't need this shit, just a test
    def get_action1(self):
        print(1)

    def set_main_window(self):
        if not self.wav_info:
            self.error = FrameError(self.message)

            self.ui.renameWindowTitle(self.FrameDefault)

            if self.ui.actionHeader.isEnabled():
                self.ui.actionHeader.setDisabled(True)
                self.ui.actionSpectrum.setDisabled(True)
                self.ui.actionAnalysis.setDisabled(True)
        else:
            self.ui.renameWindowTitle(self.FrameDefault, self.path)

            if not self.ui.actionHeader.isEnabled():
                self.ui.actionHeader.setEnabled(True)
                self.ui.actionSpectrum.setEnabled(True)
                self.ui.actionAnalysis.setEnabled(True)

            self.add_action()

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

            self.set_main_window()

    # TODO: how clear right? 80% right
    def clear_recent(self):
        actions = self.ui.menu_recent.actions()

        for i, action in enumerate(actions):
            if i != 0:
                self.ui.menu_recent.removeAction(action)

        self.ui.actionClear.setDisabled(True)

    def get_header(self):
        self.info = FrameHeader(self.wav_info)

    def plot_spectrum(self):
        self.spectrum = FrameSpectrum(self.path)

    def frequency_analysis(self):
        pass

    def help(self):
        pass

    def about(self):
        pass


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
