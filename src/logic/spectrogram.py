import numpy

from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from src.frames.spectrogram import Ui_FrameSpectrogram


class FrameSpectrogram(QWidget):
    def __init__(self, wave_data, sample_rate):
        super(FrameSpectrogram, self).__init__()
        # self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_FrameSpectrogram()
        self.ui.setupUi(self)

        self.plot_spectrogram(wave_data, sample_rate)

        self.show()

    def add_spectrogram(self, figure):
        self.canvas = FigureCanvas(figure)
        self.ui.imageLayout.addWidget(self.canvas)
        self.canvas.draw()

        self.toolbar = NavigationToolbar(self.canvas, self.ui.imageWidget, coordinates=True)
        self.ui.imageLayout.addWidget(self.toolbar)

    def plot_spectrogram(self,  wave_data, sample_rate):
        # TODO: refactor this shit
        #  Spectrogram for 2 channels or what?
        window_size = 2048
        window_step = 512

        if isinstance(wave_data[0], numpy.ndarray):
            wave_data = wave_data.mean(1)

        # TODO: on little screens
        figure = pyplot.figure(figsize=(20, 20))
        axes = figure.add_subplot(111)
        axes.set_xlabel('Время (сек)')
        axes.set_ylabel('Частота (Гц)')
        axes.specgram(wave_data, NFFT=window_size, noverlap=window_size - window_step, Fs=sample_rate)

        self.add_spectrogram(figure)

        # axes = self.figure.add_axes((0.1, 0.1, 0.8, 0.8))