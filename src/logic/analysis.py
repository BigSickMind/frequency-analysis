import numpy

from scipy.fftpack import fft

from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from statistics import mean
from math import sqrt
from math import log10 as lg

from time import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from frames.analysis import Ui_FrameAnalysis

from logic import collect


class FrameAnalysis(QMainWindow):
    def __init__(self, filename, NumChannels, values, wave_data, sample_rate, parent=None):
        super(FrameAnalysis, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_FrameAnalysis()
        self.ui.setupUi(self)

        self.ui.buttonOk.clicked.connect(self.ok)
        self.analysis(filename, NumChannels, values, wave_data, sample_rate)

        self.show()

    def ok(self):
        collect()
        self.close()

    def add_analysis_GSSNR(self, figure_GSSNR):
        canvas = FigureCanvas(figure_GSSNR)
        self.ui.GSSNRLayout.addWidget(canvas)
        canvas.draw()

        toolbar = NavigationToolbar(canvas, self.ui.GSSNRWidget, coordinates=True)
        self.ui.GSSNRLayout.addWidget(toolbar)

        collect()

    def add_analysis_SSNR(self, figure_SSNR):
        canvas = FigureCanvas(figure_SSNR)
        self.ui.SSNRLayout.addWidget(canvas)
        canvas.draw()

        toolbar = NavigationToolbar(canvas, self.ui.SSNRWidget, coordinates=True)
        self.ui.SSNRLayout.addWidget(toolbar)

        collect()

    def add_results(self, filename, NumChannels, values, result_GSSNR, result_SSNR):
        if NumChannels < 0:
            self.ui.textResults.append('В аудиофайл {}.wav вносились изменения\n'.format(filename))

            if NumChannels == -1:
                self.ui.textResults.append(
                    'В заголовке в {} вместо значения "{}" записано значение "{}"'.format(*values))
            else:
                self.ui.textResults.append(
                    'В заголовке значения не удовлетворяют формуле {} = {}'.format(*values))
        else:
            if result_GSSNR and result_SSNR:
                self.ui.textResults.append('В аудиофайл {}.wav не вносились изменения'.format(filename))
            else:
                self.ui.textResults.append('В аудиофайл {}.wav вносились изменения в области данных\n'.format(filename))

    def analysis(self, filename, NumChannels, values, wave_data, sample_rate):
        result_GSSNR, result_SSNR = False, False

        if NumChannels > 0:
            fft_data = abs(fft(wave_data))
            n = len(wave_data)
            fft_data = fft_data[0:(n // 2)]
            fft_data = fft_data / float(n)
            freqArray = numpy.arange(0, (n // 2), 1.0) * (sample_rate * 1.0 / n)
            db = 10 * numpy.log10(fft_data)

            GSSNR, SSNR = get_parameters(freqArray, db)

            freqs, GSSNR_blocks, SSNR_blocks, result_GSSNR, result_SSNR = get_interval_parameters(freqArray, db)

            figure_GSSNR = plot_analysis(freqArray, GSSNR, freqs, GSSNR_blocks, 'GSSNR')
            figure_SSNR = plot_analysis(freqArray, SSNR, freqs, SSNR_blocks, 'SSNR')

            self.add_analysis_GSSNR(figure_GSSNR)
            self.add_analysis_SSNR(figure_SSNR)

        self.add_results(filename, NumChannels, values, result_GSSNR, result_SSNR)

        if NumChannels > 0:
            pyplot.close(figure_GSSNR)
            pyplot.close(figure_SSNR)

        collect()


def plot_analysis(freqArray, SSNR, freqs, SSNR_blocks, SSNR_type):
    figure = pyplot.figure(figsize=(20, 20))
    axes = figure.add_subplot(111)
    axes.set_xlabel('Частота (Гц)')
    axes.set_ylabel(SSNR_type)

    for i in range(len(freqs)):
        if i == 0:
            axes.plot(freqs[i], SSNR_blocks[i], 'go', label='значения {} интервалов'.format(SSNR_type))
        else:
            axes.plot(freqs[i], SSNR_blocks[i], 'go')

    axes.plot(freqs, SSNR_blocks, '--b', label='{} интервалов'.format(SSNR_type))
    axes.plot(freqArray, [SSNR] * len(freqArray), 'r', label='{} аудиофайла'.format(SSNR_type))

    if SSNR_type == 'GSSNR':
        axes.legend(loc='upper right')
    else:
        axes.legend(loc='lower left')

    return figure


def calculate_block(db, GSSNR_numerator, GSSNR_denominator, SSNR, n):
    sum1 = 0
    sum2 = 0
    for j in range(len(db)):
        sum1 += db[j] ** 2
        sum2 += db[j]

    mean_db = mean(db)
    sigma_b = sqrt(sum1 / len(db) - (sum2 / len(db)) ** 2)

    GSSNR_numerator += sigma_b ** 2
    GSSNR_denominator += (sigma_b - mean_db) ** 2

    SSNR += 10 * lg(sigma_b ** 2 / ((sigma_b - mean_db) ** 2))
    n.append(len(db))

    return GSSNR_numerator, GSSNR_denominator, SSNR, n


def get_parameters(freqArray, db):
    start = 0
    limit_freq = 250.0

    GSSNR_numerator = 0
    GSSNR_denominator = 0

    SSNR = 0
    n = []

    for i in range(len(freqArray)):
        if freqArray[i] - freqArray[start] <= limit_freq:
            continue
        else:
            finish = i
            GSSNR_numerator, GSSNR_denominator, SSNR, n = calculate_block(db[start:finish], GSSNR_numerator,
                                                                          GSSNR_denominator, SSNR, n)
            start = finish

    if start < len(db) - 1:
        GSSNR_numerator, GSSNR_denominator, SSNR, n = calculate_block(db[start:], GSSNR_numerator, GSSNR_denominator,
                                                                      SSNR, n)

    GSSNR = GSSNR_numerator / GSSNR_denominator
    SSNR = SSNR / mean(n)

    return GSSNR, SSNR


def get_interval_parameters(freqArray, db):
    finish = 0
    limit_freq = 250.0
    k = 10

    freqs = []
    GSSNR_blocks = []
    SSNR_blocks = []

    for i in range(len(freqArray)):
        if freqArray[i] - freqArray[0] <= limit_freq:
            continue
        else:
            finish = i
            n = finish // k
            idx = 0

            GSSNR_numerator = 0
            GSSNR_denominator = 0

            SSNR = 0
            mean_n = []

            while idx < finish:
                db_cut = db[idx:min(idx + n, finish)]
                idx += n

                if idx < finish <= idx + n and finish - idx < n // 2:
                    db_cut = db[(idx - n):finish]
                    idx = finish

                GSSNR_numerator, GSSNR_denominator, SSNR, mean_n = calculate_block(db_cut, GSSNR_numerator,
                                                                                   GSSNR_denominator, SSNR, mean_n)
            freqs.append(freqArray[i])

            GSSNR_block = GSSNR_numerator / GSSNR_denominator
            GSSNR_blocks.append(GSSNR_block)

            SSNR_block = SSNR / mean(mean_n)
            SSNR_blocks.append(SSNR_block)

            limit_freq += 250
            k += 10

    if finish < len(freqArray) - 1:
        n = finish // k
        idx = 0

        GSSNR_numerator = 0
        GSSNR_denominator = 0

        SSNR = 0
        mean_n = []

        while idx < finish:
            db_cut = db[idx:min(idx + n, finish)]
            idx += n

            if idx < finish <= idx + n and finish - idx < n // 2:
                db_cut = db[(idx - n):finish]
                idx = finish

            GSSNR_numerator, GSSNR_denominator, SSNR, mean_n = calculate_block(db_cut, GSSNR_numerator,
                                                                               GSSNR_denominator, SSNR, mean_n)

        freqs.append(freqArray[len(freqArray) - 1])

        GSSNR_block = GSSNR_numerator / GSSNR_denominator
        GSSNR_blocks.append(GSSNR_block)

        SSNR_block = SSNR / mean(mean_n)
        SSNR_blocks.append(SSNR_block)

    result_GSSNR = gssnr_analysis(GSSNR_blocks)
    result_SSNR = ssnr_analysis(SSNR_blocks)

    return freqs, GSSNR_blocks, SSNR_blocks, result_GSSNR, result_SSNR


def gssnr_analysis(GSSNR_blocks):
    GSSNR_blocks = GSSNR_blocks[6:]
    flag = True
    model = []
    for i in range(1, len(GSSNR_blocks)):
        if not flag:
            if GSSNR_blocks[i] - GSSNR_blocks[i - 1] <= 0:
                continue
            elif GSSNR_blocks[i] - GSSNR_blocks[i - 1] > 0:
                model.append('min')
                flag = True
        else:
            if GSSNR_blocks[i] - GSSNR_blocks[i - 1] >= 0:
                continue
            elif GSSNR_blocks[i] - GSSNR_blocks[i - 1] < 0:
                model.append('max')
                flag = False
    if len(model) >= 3 and model[0] == 'max' and model[1] == 'min' and model[len(model) - 1] == 'max':
        return True
    else:
        return False


def ssnr_analysis(SSNR_blocks):
    SSNR_blocks = SSNR_blocks[6:]
    flag = True
    model = []
    for i in range(1, len(SSNR_blocks)):
        if flag:
            if SSNR_blocks[i] - SSNR_blocks[i - 1] >= 0:
                continue
            elif SSNR_blocks[i] - SSNR_blocks[i - 1] < 0:
                model.append('max')
                flag = False
        else:
            if SSNR_blocks[i] - SSNR_blocks[i - 1] <= 0:
                continue
            else:
                model.append('max')
    if len(model) == 1:
        return True
    else:
        return False
