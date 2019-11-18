import numpy

from scipy.fftpack import fft

from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import *

from src.frames.spectrum import Ui_FrameSpectrum


class FrameSpectrum(QWidget):
    def __init__(self, channel, sample_rate):
        super(FrameSpectrum, self).__init__()

        self.ui = Ui_FrameSpectrum()
        self.ui.setupUi(self)

        self.plot_spectrum(channel, sample_rate)

        self.show()

    def add_spectrum(self, figure):
        self.canvas = FigureCanvas(figure)
        self.ui.imageLayout.addWidget(self.canvas)
        self.canvas.draw()

        self.toolbar = NavigationToolbar(self.canvas, self.ui.imageWidget, coordinates=True)
        self.ui.imageLayout.addWidget(self.toolbar)

    def plot_spectrum(self, channel, sample_rate):
        # TODO: refactor this shit
        
        fft_data = abs(fft(channel))
        n = len(channel)
        fft_data = fft_data[0:(n // 2)]
        fft_data = fft_data / float(n)
        freqArray = numpy.arange(0, (n // 2), 1.0) * (sample_rate * 1.0 / n)
        db = 10 * numpy.log10(fft_data)

        figure = pyplot.figure(figsize=(20, 20))
        axes = figure.add_subplot(111)
        axes.set_xlabel('Частота (Гц)')
        axes.set_ylabel('Мощность (дБ)')
        axes.plot(freqArray, db)

        self.add_spectrum(figure)
