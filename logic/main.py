import sys

import numpy

import scipy.io.wavfile as wavfile

from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from frames.main import Ui_FrameDefault

from logic.error import FrameError
from logic.header import FrameHeader, get_header
from logic.spectrogram import FrameSpectrogram
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
        #  spectrum plot - frequency/db, spectrogram - time/frequency?
        self.ui.actionSpectrogram.triggered.connect(self.plot_spectrogram)
        self.ui.actionSpectrum.triggered.connect(self.plot_spectrum)
        self.ui.actionAnalysis.triggered.connect(self.frequency_analysis)

        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionAbout.triggered.connect(self.about)

        self.show()

    @staticmethod
    def exit():
        sys.exit()

    def build_waveform(self):
        # TODO: refactor this shit
        #  Set picture size like window

        # TODO: on little screens
        figure = pyplot.figure(figsize=(20, 20))

        self.sample_rate, self.wave_data = wavfile.read(self.path)

        channel1 = self.wave_data[:, 0]
        channel2 = self.wave_data[:, 1]

        # TODO: normalize amplitude values or not?
        channel1 = numpy.divide(channel1, max(channel1))
        channel2 = numpy.divide(channel2, max(channel2))

        time = numpy.arange(0, float(self.wave_data.shape[0] / self.sample_rate), 1 / self.sample_rate)

        # TODO: think about mono channel

        # TODO: scrollable image?
        axes_left = figure.add_subplot(411)
        axes_left.set_title('Левый канал')
        axes_left.set_xlabel('Время (сек)')
        axes_left.set_ylabel('Амлитуда (метры)')
        axes_left.plot(time, channel1)

        axes_right = figure.add_subplot(413)
        axes_right.set_title('Правый канал')
        axes_right.set_xlabel('Время (сек)')
        axes_right.set_ylabel('Амлитуда (метры)')
        axes_right.plot(time, channel2)

        self.canvas = FigureCanvas(figure)
        self.ui.imageLayout.addWidget(self.canvas)
        self.canvas.draw()

        # self.scroll = QScrollBar(Qt.Horizontal)
        # self.ui.imageLayout.addWidget(self.scroll)

        self.toolbar = NavigationToolbar(self.canvas, self.ui.imageWidget, coordinates=True)
        self.ui.imageLayout.addWidget(self.toolbar)

    def set_main_window(self):
        if not self.wav_info:
            self.error = FrameError(self.message)

            self.ui.renameWindowTitle(self.FrameDefault)

            if self.ui.actionHeader.isEnabled():
                self.ui.actionHeader.setDisabled(True)
                self.ui.actionSpectrogram.setDisabled(True)
                self.ui.actionSpectrum.setDisabled(True)
                self.ui.actionAnalysis.setDisabled(True)
        else:
            self.ui.renameWindowTitle(self.FrameDefault, self.path)

            if not self.ui.actionHeader.isEnabled():
                self.ui.actionHeader.setEnabled(True)
                self.ui.actionSpectrogram.setEnabled(True)
                self.ui.actionSpectrum.setEnabled(True)
                self.ui.actionAnalysis.setEnabled(True)

            self.build_waveform()

    # TODO: test normal files 2-3 min
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

    def plot_spectrogram(self):
        self.spectrogram = FrameSpectrogram(self.sample_rate, self.wave_data)

    def plot_spectrum(self):
        self.spectrum = FrameSpectrum(self.wave_data[:, 0], self.sample_rate)

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
