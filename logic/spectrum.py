import numpy
import scipy.io.wavfile

from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import *

from frames.spectrum import Ui_FrameSpectrum


class FrameSpectrum(QWidget):
    def __init__(self, path):
        super(FrameSpectrum, self).__init__()

        self.ui = Ui_FrameSpectrum()
        self.ui.setupUi(self)

        self.plot_spectrum(path)

        self.show()

    def add_spectrum(self, figure):
        self.canvas = FigureCanvas(figure)
        self.ui.imageLayout.addWidget(self.canvas)
        self.canvas.draw()

        self.toolbar = NavigationToolbar(self.canvas, self.ui.imageWidget, coordinates=True)
        self.ui.imageLayout.addWidget(self.toolbar)

    def plot_spectrum(self, path):
        # TODO: refactor this shit
        window_size = 2048
        window_step = 512

        sample_rate, wave_data = scipy.io.wavfile.read(path)
        if isinstance(wave_data[0], numpy.ndarray):
            wave_data = wave_data.mean(1)

        # plot = pyplot.figure()
        # axes = plot.add_axes((0.1, 0.1, 0.8, 0.8))
        # axes.specgram(wave_data, NFFT=window_size, noverlap=window_size - window_step, Fs=sample_rate)
        # pyplot.show()

        figure = pyplot.figure()
        axes = figure.add_subplot(111)
        # axes = figure.add_axes((0.1, 0.1, 0.8, 0.8))
        axes.specgram(wave_data, NFFT=window_size, noverlap=window_size - window_step, Fs=sample_rate)

        self.add_spectrum(figure)

        # axes = self.figure.add_subplot(111)
        # axes.clear()
        #
        # axes = self.figure.add_axes((0.1, 0.1, 0.8, 0.8))
        # axes.specgram(wave_data, NFFT=window_size, noverlap=window_size - window_step, Fs=sample_rate)
        #
        # self.canvas.draw()
