import sys

import numpy

import wavio
import soundfile

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

        self.ui.actionAboutProgram.triggered.connect(self.about)

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
        channel = self.wave.data

        channel = numpy.divide(channel, max(channel))

        axes = figure.add_subplot(111)
        axes.set_title('Канал')
        axes.set_xlabel('Время (сек)')
        axes.set_ylabel('Амлитуда (метры)')
        axes.plot(time, channel)

        return figure

    def build_stereo(self, figure, time):
        channel1 = self.wave.data[:, 0]
        channel2 = self.wave.data[:, 1]

        channel1 = numpy.divide(channel1, max(channel1))
        channel2 = numpy.divide(channel2, max(channel2))

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

    def build_waveform(self, path, message):
        figure = pyplot.figure(figsize=(20, 20))

        matplotlib.rcParams['agg.path.chunksize'] = 10000

        self.wave = wavio.read(path)

        time = numpy.arange(0, float(self.wave.data.shape[0] / self.wave.rate), 1 / self.wave.rate)

        if self.NumChannels > 2:
            self.print_error(message)
        else:
            if self.NumChannels == 1:
                self.build_mono(figure, time)
            elif self.NumChannels == 2:
                self.build_stereo(figure, time)

            canvas = FigureCanvas(figure)
            self.ui.imageLayout.addWidget(canvas)
            canvas.draw()

            toolbar = NavigationToolbar(canvas, self.ui.imageWidget, coordinates=True)
            self.ui.imageLayout.addWidget(toolbar)

            pyplot.close(figure)
            collect()

    def set_main_window(self, path, message):
        if self.NumChannels == -3:
            self.last_path = ''

            self.print_error(message)
        elif self.NumChannels < 0:
            self.print_error(message)

            self.last_path = path

            self.ui.renameWindowTitle(self.FrameMain, path)

            self.ui.actionAnalysis.setEnabled(True)
        else:
            self.last_path = path

            self.ui.renameWindowTitle(self.FrameMain, path)

            if not self.ui.actionHeader.isEnabled():
                self.ui.actionHeader.setEnabled(True)
                self.ui.actionSpectrogram.setEnabled(True)
                self.ui.actionSpectrum.setEnabled(True)
                self.ui.actionAnalysis.setEnabled(True)

            self.build_waveform(path, message)

    def open_file(self):

        options = QFileDialog.Options()

        path, _ = QFileDialog.getOpenFileName(self, "Выберите аудиофайл", '',
                                              "VLC media file (*.wav *.mp3 *.ogg *.flac *.aiff);;All Files (*)",
                                              options=options)
        if path and self.last_path != path:
            for i in reversed(range(self.ui.imageLayout.count())):
                self.ui.imageLayout.itemAt(i).widget().setParent(None)

            self.filename = path[(path.rfind('/') + 1):path.rfind('.')]

            self.wav_info, message, self.NumChannels, self.values = get_header(path, self.filename)

            self.set_main_window(path, message)

    def get_header(self):
        self.header = FrameHeader(self.wav_info, parent=self)

    def plot_spectrogram(self):
        self.spectrogram = FrameSpectrogram(self.wave.data, self.wave.rate, parent=self)

    def plot_spectrum(self):
        self.spectrum = FrameSpectrum(self.wave.data[:, 0], self.wave.rate, parent=self)

    def frequency_analysis(self):
        if self.NumChannels < 0:
            self.analysis = FrameAnalysis(self.filename, self.NumChannels, self.values,
                                          None, None, parent=self)
        else:
            self.analysis = FrameAnalysis(self.filename, self.NumChannels, self.values,
                                          self.wave.data[:, 0], self.wave.rate, parent=self)

    def about(self):
        self.about = FrameAbout(parent=self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()

    sys.exit(app.exec_())