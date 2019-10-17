import numpy

import scipy.io.wavfile

from matplotlib import pyplot

from frames.spectrum import Ui_FrameSpectrum

from PyQt5.QtWidgets import *


class FrameSpectrum(QWidget):
    def __init__(self, path):
        super(FrameSpectrum, self).__init__()

        self.ui = Ui_FrameSpectrum()
        self.ui.setupUi(self)

        # self.plot_spectrum(path)

        self.show()

    def plot_spectrum(self, path):
        window_size = 2048
        window_step = 512

        sample_rate, wave_data = scipy.io.wavfile.read(path)
        if isinstance(wave_data[0], numpy.ndarray):
            wave_data = wave_data.mean(1)

        plot = pyplot.figure()
        axes = plot.add_axes((0.1, 0.1, 0.8, 0.8))
        axes.specgram(wave_data, NFFT=window_size, noverlap=window_size - window_step, Fs=sample_rate)
        pyplot.show()
