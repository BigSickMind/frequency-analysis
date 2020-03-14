import numpy

from logic import collect

from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from frames.spectrogram import Ui_FrameSpectrogram


class FrameSpectrogram(QMainWindow):
    def __init__(self, wave_data, sample_rate, parent=None):
        super(FrameSpectrogram, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_FrameSpectrogram()
        self.ui.setupUi(self)

        self.ui.buttonOk.clicked.connect(self.ok)

        self.plot_spectrogram(wave_data, sample_rate)

        self.show()

    def ok(self):
        collect()
        self.close()

    def add_spectrogram(self, figure):
        canvas = FigureCanvas(figure)
        self.ui.imageLayout.addWidget(canvas)
        canvas.draw()

        toolbar = NavigationToolbar(canvas, self.ui.imageWidget, coordinates=True)
        self.ui.imageLayout.addWidget(toolbar)

        collect()

    def plot_spectrogram(self, wave_data, sample_rate):
        window_size = 2048
        window_step = 512

        if isinstance(wave_data[0], numpy.ndarray):
            wave_data = wave_data.mean(1)

        figure = pyplot.figure(figsize=(20, 20))
        axes = figure.add_subplot(111)
        axes.set_xlabel('Время (сек)')
        axes.set_ylabel('Частота (Гц)')
        _, _, _, im = axes.specgram(wave_data, NFFT=window_size, noverlap=window_size - window_step, Fs=sample_rate)
        figure.colorbar(im).set_label('Мощность (дБ)')

        self.add_spectrogram(figure)

        pyplot.close(figure)
        collect()
