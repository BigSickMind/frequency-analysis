import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from frames.error import Ui_FrameError

from logic import collect


class FrameError(QMainWindow):
    def __init__(self, message, parent=None):
        super(FrameError, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_FrameError()
        self.ui.setupUi(self)

        self.ui.buttonOk.clicked.connect(self.ok)
        self.ui.labelError.setText(message)

        self.show()

    def ok(self):
        collect()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FrameError('1')

    sys.exit(app.exec_())
