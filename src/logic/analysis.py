import numpy

from scipy.fftpack import fft

from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from statistics import mean
from math import sqrt

from time import time

from PyQt5.QtWidgets import *

from src.frames.analysis import Ui_FrameAnalysis


class FrameAnalysis(QWidget):
    def __init__(self, wave_data, sample_rate):
        super(FrameAnalysis, self).__init__()

        self.ui = Ui_FrameAnalysis()
        self.ui.setupUi(self)

        self.analysis(wave_data, sample_rate)

        self.show()

    def add_analysis(self, figure):
        self.canvas = FigureCanvas(figure)
        self.ui.imageLayout.addWidget(self.canvas)
        self.canvas.draw()

        self.toolbar = NavigationToolbar(self.canvas, self.ui.imageWidget, coordinates=True)
        self.ui.imageLayout.addWidget(self.toolbar)

    def plot_analysis(self, freqArray, GSSNR, freqs, GSSNR_blocks):
        figure = pyplot.figure(figsize=(20, 20))
        self.axes = figure.add_subplot(111)
        self.axes.set_xlabel('Частота (Гц)')
        self.axes.set_ylabel('GSSNR')

        for i in range(6, len(freqs)):
            if i == 6:
                self.axes.plot(freqs[i], GSSNR_blocks[i], 'go', label='значения GSSNR')
            else:
                self.axes.plot(freqs[i], GSSNR_blocks[i], 'go')
        self.axes.plot(freqs, GSSNR_blocks, '--b', label='GSSNR интервалов')
        self.axes.plot(freqArray, [GSSNR] * len(freqArray), 'r', label='GSSNR аудиофайла')

        self.axes.legend(loc='upper right')
        self.add_analysis(figure)

    def analysis(self, wave_data, sample_rate):
        fft_data = abs(fft(wave_data))
        n = len(wave_data)
        fft_data = fft_data[0:(n // 2)]
        fft_data = fft_data / float(n)
        freqArray = numpy.arange(0, (n // 2), 1.0) * (sample_rate * 1.0 / n)
        db = 10 * numpy.log10(fft_data)

        # TODO: why is working so long? where is a problem?
        GSSNR = self.get_parameters(freqArray, db)

        # TODO: Here. Twice cycle with raising values
        freqs, GSSNR_blocks = self.get_interval_parameters(freqArray, db)

        self.plot_analysis(freqArray, GSSNR, freqs, GSSNR_blocks)

    @staticmethod
    def get_parameters(freqArray, db):
        # TODO: TEST
        start_time = time()

        start = 0

        numerator = 0
        denominator = 0

        for i in range(len(freqArray)):
            if freqArray[i] - freqArray[start] <= 100.0:
                continue
            else:
                # TODO: TEST
                print(i)

                finish = i
                numerator, denominator = calculate_GSSNR_block(db[start:finish], numerator, denominator)
                start = finish

        if start < len(db) - 1:
            numerator, denominator = calculate_GSSNR_block(db[start:], numerator, denominator)

        GSSNR = numerator / denominator

        print('GSSNR GSSNR GSSNR: ', time() - start_time)

        return GSSNR

    # TODO: Patent, algorithm
    @staticmethod
    def get_interval_parameters(freqArray, db):
        # TODO: TEST
        start_time = time()

        finish = 0
        k = 1

        freqs = []
        GSSNR_blocks = []

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

                numerator = 0
                denominator = 0

                while idx < finish:
                    db_cut = db[idx:min(idx + n, finish)]
                    idx += n

                    if idx < finish <= idx + n and finish - idx < n // 2:
                        db_cut = db[(idx - n):finish]
                        idx = finish

                    numerator, denominator = calculate_GSSNR_block(db_cut, numerator, denominator)

                GSSNR_block = numerator / denominator
                GSSNR_blocks.append(GSSNR_block)
                freqs.append(freqArray[i])
                k += 1

        if finish < len(freqArray) - 1:
            n = finish // (10 * k)
            idx = 0

            numerator = 0
            denominator = 0

            while idx < finish:
                db_cut = db[idx:min(idx + n, finish)]
                idx += n

                if idx < finish <= idx + n and finish - idx < n // 2:
                    db_cut = db[(idx - n):finish]
                    idx = finish

                numerator, denominator = calculate_GSSNR_block(db_cut, numerator, denominator)

            GSSNR_block = numerator / denominator
            GSSNR_blocks.append(GSSNR_block)
            freqs.append(freqArray[len(freqArray) - 1])

        print('GSSNR INTERVAL GSSNR INTERVAL: ', time() - start_time)

        return freqs, GSSNR_blocks


def calculate_GSSNR_block(db, numerator, denominator):
    sum1 = 0
    sum2 = 0
    for j in range(len(db)):
        sum1 += db[j] ** 2
        sum2 += db[j]

    mean_db_hundred = mean(db)
    sigma_b = sqrt(sum1 / len(db) - (sum2 / len(db)) ** 2)

    numerator += sigma_b ** 2
    denominator += (sigma_b - mean_db_hundred) ** 2

    return numerator, denominator

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
