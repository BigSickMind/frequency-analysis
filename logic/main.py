import sys

import numpy as np
import scipy.io.wavfile as wavfile
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import *

from frames.main import Ui_FrameDefault

from logic.error import FrameError
from logic.header import FrameHeader, get_header
from logic.spectrum import FrameSpectrum


# TODO: check message.wav. Seems that it's normal, but program crashes
class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.ui = Ui_FrameDefault()
        self.FrameDefault = self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(self.exit)

        self.ui.actionHeader.triggered.connect(self.get_header)

        # TODO: spectrogram and spectrum plot - different things?
        #  spectrum plot - fft, spectrogram - ?
        self.ui.actionSpectrum.triggered.connect(self.plot_spectrum)
        self.ui.actionFFT.triggered.connect(self.plot_fft)
        self.ui.actionAnalysis.triggered.connect(self.frequency_analysis)

        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionAbout.triggered.connect(self.about)

        self.show()

    @staticmethod
    def exit():
        sys.exit()

    def add_wave(self):
        # TODO: refactor this shit
        #  Set picture size like window
        figure = pyplot.figure()

        sample_rate, wave_data = wavfile.read(self.path)
        channel1 = wave_data[:, 0]
        channel2 = wave_data[:, 1]
        time = np.arange(0, float(wave_data.shape[0] / sample_rate), 1 / sample_rate)

        # TODO: check correct y values
        ax = figure.add_subplot(411)
        ax.set_title('Левый канал')
        ax.plot(time, channel1)
        ax.set_xlabel('Время (сек)')
        ax.set_ylabel('Амлитуда (метры)')

        ax2 = figure.add_subplot(413)
        ax2.set_title('Правый канал')
        ax2.plot(time, channel2)
        ax2.set_xlabel('Время (сек)')
        ax2.set_ylabel('Амлитуда (метры)')

        self.canvas = FigureCanvas(figure)
        self.ui.imageLayout.addWidget(self.canvas)
        self.canvas.draw()

        self.toolbar = NavigationToolbar(self.canvas, self.ui.imageWidget, coordinates=True)
        self.ui.imageLayout.addWidget(self.toolbar)

    def set_main_window(self):
        if not self.wav_info:
            self.error = FrameError(self.message)

            self.ui.renameWindowTitle(self.FrameDefault)

            if self.ui.actionHeader.isEnabled():
                self.ui.actionHeader.setDisabled(True)
                self.ui.actionSpectrum.setDisabled(True)
                self.ui.actionFFT.setDisabled(True)
                self.ui.actionAnalysis.setDisabled(True)
        else:
            self.ui.renameWindowTitle(self.FrameDefault, self.path)

            if not self.ui.actionHeader.isEnabled():
                self.ui.actionHeader.setEnabled(True)
                self.ui.actionSpectrum.setEnabled(True)
                self.ui.actionFFT.setEnabled(True)
                self.ui.actionAnalysis.setEnabled(True)

            self.add_wave()

    def open_file(self):
        options = QFileDialog.Options()
        # TODO: default directory?
        directory = "D:/Github/frequency-analysis/tests/test/"
        # directory = ""
        self.path, _ = QFileDialog.getOpenFileName(self, "Выберите аудиофайл", directory,
                                                   "All Files (*);;VLC media file (*.wav *.mp3 *.ogg *.flac *.aiff)",
                                                   options=options)
        if self.path:
            self.filename = self.path[(self.path.rfind('/') + 1):self.path.rfind('.')]

            self.wav_info, self.message = get_header(self.path, self.filename)

            self.set_main_window()

    def get_header(self):
        self.info = FrameHeader(self.wav_info)

    def plot_spectrum(self):
        self.spectrum = FrameSpectrum(self.path)

    def plot_fft(self):
        pass

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
