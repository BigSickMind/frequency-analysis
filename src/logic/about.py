import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from frames.about import Ui_FrameAbout


class FrameAbout(QMainWindow):
    def __init__(self, parent=None):
        super(FrameAbout, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_FrameAbout()
        self.ui.setupUi(self)

        self.ui.textAbout.setReadOnly(True)

        self.show()


# Test
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FrameAbout()

    sys.exit(app.exec_())
