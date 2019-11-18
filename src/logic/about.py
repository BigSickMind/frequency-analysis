import sys

from PyQt5.QtWidgets import *

from src.frames.about import Ui_FrameAbout


class FrameAbout(QWidget):
    def __init__(self):
        super(FrameAbout, self).__init__()

        self.ui = Ui_FrameAbout()
        self.ui.setupUi(self)

        self.ui.textAbout.setReadOnly(True)

        self.show()


# Test
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FrameAbout()

    sys.exit(app.exec_())
