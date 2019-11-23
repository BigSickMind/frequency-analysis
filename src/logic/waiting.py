import sys

from PyQt5.QtWidgets import *

from src.frames.waiting import Ui_FrameWaiting


class FrameWaiting(QWidget):
    def __init__(self):
        super(FrameWaiting, self).__init__()

        self.ui = Ui_FrameWaiting()
        self.ui.setupUi(self)

        self.show()

    def setValue(self, value):
        self.ui.progressBar.setValue(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FrameWaiting()

    sys.exit(app.exec_())
