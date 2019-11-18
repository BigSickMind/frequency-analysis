# TODO: think about this shit

import sys

sys.path = sys.path + ['src']

from PyQt5.QtWidgets import QMainWindow, QApplication

import logic.logic as logic


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.setupUi(self)
        logic.Main.__init__(self)

        logic.Main.start(self)

        # self.setWindowTitle("Частотный анализатор")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())
