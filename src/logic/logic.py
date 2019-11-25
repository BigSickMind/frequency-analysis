import sys

import numpy

# TODO: some wav files are opened with errors of unreadable bytes
import scipy.io.wavfile as wavfile

# TODO: main library
import wavio

# TODO: useless
import wave

# TODO: good library for another formats (except MP3)
# import soundfile

import matplotlib
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from frames.main import Ui_FrameMain

from logic import collect

from logic.error import FrameError
from logic.header import FrameHeader, get_header
from logic.spectrogram import FrameSpectrogram
from logic.spectrum import FrameSpectrum
from logic.analysis import FrameAnalysis
from logic.about import FrameAbout


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_FrameMain()
        self.FrameMain = self.ui.setupUi(self)

        self.last_path = ''

    def start(self):
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(self.exit)

        self.ui.actionHeader.triggered.connect(self.get_header)
        self.ui.actionSpectrogram.triggered.connect(self.plot_spectrogram)
        self.ui.actionSpectrum.triggered.connect(self.plot_spectrum)
        self.ui.actionAnalysis.triggered.connect(self.frequency_analysis)

        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionAbout.triggered.connect(self.about)

        self.show()

    def exit(self):
        self.close()

    def print_error(self, message):
        self.error = FrameError(message, parent=self)

        self.ui.renameWindowTitle(self.FrameMain)

        if self.ui.actionHeader.isEnabled():
            self.ui.actionHeader.setDisabled(True)
            self.ui.actionSpectrogram.setDisabled(True)
            self.ui.actionSpectrum.setDisabled(True)
            self.ui.actionAnalysis.setDisabled(True)

    def build_mono(self, figure, time):
        # channel = self.wave_data

        channel = self.wave.data

        # self.wave.readframes(self.wave.getnframes())

        # channel = self.data

        # TODO: normalize amplitude values or not?
        channel = numpy.divide(channel, max(channel))

        axes = figure.add_subplot(111)
        axes.set_title('Канал')
        axes.set_xlabel('Время (сек)')
        axes.set_ylabel('Амлитуда (метры)')
        axes.plot(time, channel)

        return figure

    def build_stereo(self, figure, time):
        # channel1 = self.wave_data[:, 0]
        # channel2 = self.wave_data[:, 1]

        channel1 = self.wave.data[:, 0]
        channel2 = self.wave.data[:, 1]

        # self.wave.readframes(self.wave.getnframes())

        # channel1 = self.data[:, 0]
        # channel2 = self.data[:, 1]

        # TODO: normalize amplitude values or not?
        channel1 = numpy.divide(channel1, max(channel1))
        channel2 = numpy.divide(channel2, max(channel2))

        # TODO: scrollable image?
        axes_left = figure.add_subplot(311)
        axes_left.set_title('Левый канал')
        axes_left.set_xlabel('Время (сек)')
        axes_left.set_ylabel('Амлитуда (метры)')
        axes_left.plot(time, channel1)

        axes_right = figure.add_subplot(313)
        axes_right.set_title('Правый канал')
        axes_right.set_xlabel('Время (сек)')
        axes_right.set_ylabel('Амлитуда (метры)')
        axes_right.plot(time, channel2)

        return figure

    def build_waveform(self, path, message, NumChannels):
        # TODO: refactor this shit
        #  Set picture size like window

        figure = pyplot.figure(figsize=(20, 20))

        # TODO: fix problems?
        matplotlib.rcParams['agg.path.chunksize'] = 10000

        # self.sample_rate, self.wave_data = wavfile.read(self.path)
        self.wave = wavio.read(path)
        # self.wave = wave.open(path, 'r')
        # self.data, self.rate = soundfile.read(path)

        # print(1)
        # exit()

        # time = numpy.arange(0, float(self.wave_data.shape[0] / self.sample_rate), 1 / self.sample_rate)
        time = numpy.arange(0, float(self.wave.data.shape[0] / self.wave.rate), 1 / self.wave.rate)
        # time = numpy.arange(0, float(self.wave.getnframes() / self.wave.getframerate()), 1 / self.wave.getframerate())
        # time = numpy.arange(0, float(self.data.shape[0] / self.rate), 1 / self.rate)

        if NumChannels > 2:
            self.print_error(message)
        else:
            if NumChannels == 1:
                self.build_mono(figure, time)
            elif NumChannels == 2:
                self.build_stereo(figure, time)

            canvas = FigureCanvas(figure)
            self.ui.imageLayout.addWidget(canvas)
            canvas.draw()

            # self.scroll = QScrollBar(Qt.Horizontal)
            # self.ui.imageLayout.addWidget(self.scroll)

            toolbar = NavigationToolbar(canvas, self.ui.imageWidget, coordinates=True)
            self.ui.imageLayout.addWidget(toolbar)

            pyplot.close(figure)
            collect()

    def set_main_window(self, path, message, NumChannels):
        if not self.wav_info:
            self.last_path = ''

            self.print_error(message)
        else:
            self.last_path = path

            self.ui.renameWindowTitle(self.FrameMain, path)

            if not self.ui.actionHeader.isEnabled():
                self.ui.actionHeader.setEnabled(True)
                self.ui.actionSpectrogram.setEnabled(True)
                self.ui.actionSpectrum.setEnabled(True)
                self.ui.actionAnalysis.setEnabled(True)

            self.build_waveform(path, message, NumChannels)

    # TODO: test normal files 2-3 min
    def open_file(self):

        options = QFileDialog.Options()

        # self.path, _ = QFileDialog.getOpenFileName(self, "Выберите аудиофайл", directory,
        path, _ = QFileDialog.getOpenFileName(self, "Выберите аудиофайл", '',
                                              "VLC media file (*.wav *.mp3 *.ogg *.flac *.aiff);;All Files (*)",
                                              options=options)
        if path and self.last_path != path:
            for i in reversed(range(self.ui.imageLayout.count())):
                self.ui.imageLayout.itemAt(i).widget().setParent(None)

            filename = path[(path.rfind('/') + 1):path.rfind('.')]

            self.wav_info, message, NumChannels = get_header(path, filename)

            self.set_main_window(path, message, NumChannels)

    def get_header(self):
        self.header = FrameHeader(self.wav_info, parent=self)

    def plot_spectrogram(self):
        # self.spectrogram = FrameSpectrogram(self.wave_data, self.sample_rate)
        self.spectrogram = FrameSpectrogram(self.wave.data, self.wave.rate, parent=self)
        # self.spectrogram = FrameSpectrogram(self.data, self.rate)

    def plot_spectrum(self):
        # self.spectrum = FrameSpectrum(self.wave_data[:, 0], self.sample_rate)
        self.spectrum = FrameSpectrum(self.wave.data[:, 0], self.wave.rate, parent=self)
        # self.spectrum = FrameSpectrum(self.data[:, 0], self.rate)

    def frequency_analysis(self):
        # self.analysis = FrameAnalysis(self.wave_data[:, 0], self.sample_rate)
        self.analysis = FrameAnalysis(self.wave.data[:, 0], self.wave.rate, parent=self)
        # self.analysis = FrameAnalysis(self.data[:, 0], self.rate)

    def help(self):
        pass

    def about(self):
        self.about = FrameAbout(parent=self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()

    sys.exit(app.exec_())

# return FrameMain
#
# def renameWindowTitle(self, FrameMain, path=""):
#     if not path:
#         title = "Частотный анализатор"
#     else:
#         title = "Частотный анализатор ({})".format(path)
#
#     _translate = QtCore.QCoreApplication.translate
#     FrameMain.setWindowTitle(_translate("FrameMain", title))
