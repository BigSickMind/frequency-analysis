import numpy

from scipy.fftpack import fft

from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from frames.spectrum import Ui_FrameSpectrum

from logic import collect


class FrameSpectrum(QMainWindow):
    def __init__(self, wave_data, sample_rate, parent=None):
        super(FrameSpectrum, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_FrameSpectrum()
        self.ui.setupUi(self)

        self.init(wave_data, sample_rate)

        self.ui.buttonOk.clicked.connect(self.ok)
        self.ui.comboBoxScale.activated.connect(self.plot_spectrum)

        self.show()

    def init(self, wave_data, sample_rate):
        self.wave_data = wave_data
        self.sample_rate = sample_rate

        fft_data = abs(fft(self.wave_data))
        n = len(self.wave_data)
        fft_data = fft_data[0:(n // 2)]
        self.fft_data = fft_data / float(n)
        self.freqArray = numpy.arange(0, (n // 2), 1.0) * (self.sample_rate * 1.0 / n)

        self.db = 10 * numpy.log10(self.fft_data)

        figure = pyplot.figure(figsize=(20, 20))
        axes = figure.add_subplot(111)

        axes.plot(self.freqArray, self.db)

        axes.set_xlabel('Частота (Гц)')
        axes.set_ylabel('Мощность (дБ)')

        self.add_spectrum(figure)

        pyplot.close(figure)
        collect()

    def ok(self):
        collect()
        self.close()

    def add_spectrum(self, figure):
        canvas = FigureCanvas(figure)
        self.ui.imageLayout.addWidget(canvas)
        canvas.draw()

        toolbar = NavigationToolbar(canvas, self.ui.imageWidget, coordinates=True)
        self.ui.imageLayout.addWidget(toolbar)

        collect()

    def plot_spectrum(self):
        for i in reversed(range(self.ui.imageLayout.count())):
            self.ui.imageLayout.removeWidget(self.ui.imageLayout.itemAt(i).widget())

        text = self.ui.comboBoxScale.currentText()

        figure = pyplot.figure(figsize=(20, 20))
        axes = figure.add_subplot(111)

        if text == 'Логарифмический':
            axes.plot(self.freqArray, self.db)

            axes.set_xlabel('Частота (Гц)')
            axes.set_ylabel('Мощность (дБ)')
        else:
            axes.magnitude_spectrum(self.wave_data, Fs=self.sample_rate)

            axes.set_xlabel('Частота (Гц)')
            axes.set_ylabel('Мощность')

        self.add_spectrum(figure)

        pyplot.close(figure)
        collect()
