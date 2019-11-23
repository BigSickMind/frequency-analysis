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

from src.frames.analysis import Ui_FrameAnalysis

from src.logic.waiting import FrameWaiting


class FrameAnalysis(QWidget):
    def __init__(self, wave_data, sample_rate):
        super(FrameAnalysis, self).__init__()

        self.ui = Ui_FrameAnalysis()
        self.ui.setupUi(self)

        self.ui.buttonOk.clicked.connect(self.ok)
        self.analysis(wave_data, sample_rate)

        self.show()

    def ok(self):
        self.close()

    def add_analysis_GSSNR(self, figure_GSSNR):
        canvas = FigureCanvas(figure_GSSNR)
        self.ui.GSSNRLayout.addWidget(canvas)
        canvas.draw()

        toolbar = NavigationToolbar(canvas, self.ui.GSSNRWidget, coordinates=True)
        self.ui.GSSNRLayout.addWidget(toolbar)

    def add_analysis_SSNR(self, figure_SSNR):
        canvas = FigureCanvas(figure_SSNR)
        self.ui.SSNRLayout.addWidget(canvas)
        canvas.draw()

        toolbar = NavigationToolbar(canvas, self.ui.SSNRWidget, coordinates=True)
        self.ui.SSNRLayout.addWidget(toolbar)

    def analysis(self, wave_data, sample_rate):
        fft_data = abs(fft(wave_data))
        n = len(wave_data)
        fft_data = fft_data[0:(n // 2)]
        fft_data = fft_data / float(n)
        freqArray = numpy.arange(0, (n // 2), 1.0) * (sample_rate * 1.0 / n)
        db = 10 * numpy.log10(fft_data)

        # TODO: why is working so long? where is a problem?
        GSSNR, SSNR = get_parameters(freqArray, db)

        # TODO: Here. Twice cycle with raising values
        freqs, GSSNR_blocks, SSNR_blocks = self.get_interval_parameters(freqArray, db)

        figure_GSSNR = plot_analysis(freqArray, GSSNR, freqs, GSSNR_blocks, 'GSSNR')
        figure_SSNR = plot_analysis(freqArray, SSNR, freqs, SSNR_blocks, 'SSNR')

        self.add_analysis_GSSNR(figure_GSSNR)
        self.add_analysis_SSNR(figure_SSNR)

        self.waiting.close()


def plot_analysis(freqArray, SSNR, freqs, SSNR_blocks, SSNR_type):
    figure = pyplot.figure(figsize=(20, 20))
    axes = figure.add_subplot(111)
    axes.set_xlabel('Частота (Гц)')
    axes.set_ylabel(SSNR_type)

    for i in range(6, len(freqs)):
        if i == 6:
            axes.plot(freqs[i], SSNR_blocks[i], 'go', label='значения {} интервалов'.format(SSNR_type))
        else:
            axes.plot(freqs[i], SSNR_blocks[i], 'go')

    axes.plot(freqs, SSNR_blocks, '--b', label='{} интервалов'.format(SSNR_type))
    axes.plot(freqArray, [SSNR] * len(freqArray), 'r', label='{} аудиофайла'.format(SSNR_type))

    axes.legend(loc='upper right')

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
    # TODO: TEST
    start_time = time()

    start = 0

    GSSNR_numerator = 0
    GSSNR_denominator = 0

    SSNR = 0
    n = []

    for i in range(len(freqArray)):
        if freqArray[i] - freqArray[start] <= 100.0:
            continue
        else:
            # TODO: TEST
            print(i)

            finish = i
            GSSNR_numerator, GSSNR_denominator, SSNR, n = calculate_block(db[start:finish], GSSNR_numerator,
                                                                          GSSNR_denominator, SSNR, n)
            start = finish

    if start < len(db) - 1:
        GSSNR_numerator, GSSNR_denominator, SSNR, n = calculate_block(db[start:], GSSNR_numerator, GSSNR_denominator,
                                                                      SSNR, n)

    GSSNR = GSSNR_numerator / GSSNR_denominator
    SSNR = SSNR / mean(n)

    print('GSSNR SSNR GSSNR SSNR: ', time() - start_time)

    return GSSNR, SSNR


# TODO: Patent, algorithm
def get_interval_parameters(freqArray, db):
    # TODO: TEST
    start_time = time()

    finish = 0
    k = 1

    freqs = []
    GSSNR_blocks = []
    SSNR_blocks = []

    for i in range(len(freqArray)):
        # TODO: 100 Hz, too slow
        if freqArray[i] - freqArray[0] <= 200.0 * k:
            continue
        else:
            # TODO: TEST
            print(i)

            finish = i
            n = finish // (10 * k)
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

            k += 1

    if finish < len(freqArray) - 1:
        n = finish // (10 * k)
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

    print('GSSNR INTERVAL SSNR INTERVAL: ', time() - start_time)

    return freqs, GSSNR_blocks, SSNR_blocks

# TODO: shitted shit of shit
# def gssnr_analysis(gssnr_blocks):
#     gssnr_blocks = gssnr_blocks[6:]
#     flag = True
#     model = []
#     for i in range(1, len(gssnr_blocks)):
#         if not flag:
#             if gssnr_blocks[i] - gssnr_blocks[i - 1] <= 0:
#                 continue
#             elif gssnr_blocks[i] - gssnr_blocks[i - 1] > 0:
#                 model.append('min')
#                 flag = True
#         else:
#             if gssnr_blocks[i] - gssnr_blocks[i - 1] >= 0:
#                 continue
#             elif gssnr_blocks[i] - gssnr_blocks[i - 1] < 0:
#                 model.append('max')
#                 flag = False
#     if len(model) >= 3 and model[0] == 'max' and model[1] == 'min' and model[len(model) - 1] == 'max':
#         return True
#     else:
#         return False

# def frequency_analysing(self):
#     GSSNR = get_parameters(freqArray, db)
#     gssnr_blocks = self.get_interval_parameters(freqArray, db, GSSNR)
# 
#     if self.gssnr_analysis(gssnr_blocks):
#         self.ui.parameters_text.append(
#             'Требуется проведение дальнейшего анализа, в файл {} возможно вносились изменения\n'.format(
#                 self.filename))
#     else:
#         self.ui.parameters_text.append(
#             'В файл {} вносились изменения\n'.format(self.filename))
