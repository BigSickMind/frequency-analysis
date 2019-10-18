import sys

from PyQt5.QtWidgets import *

from frames.error import Ui_FrameError


class FrameError(QWidget):
    def __init__(self, message):
        super(FrameError, self).__init__()

        self.ui = Ui_FrameError()
        self.ui.setupUi(self)

        self.ui.buttonOk.clicked.connect(self.ok)
        self.ui.labelError.setText(message)

        self.show()

    def ok(self):
        self.close()


# Test
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FrameError('1')

    sys.exit(app.exec_())
