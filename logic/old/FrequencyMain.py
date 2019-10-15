import sys
import struct

import numpy as np

import scipy.io.wavfile as wavfile
from scipy.fftpack import fft

from matplotlib import pyplot as plt

from frames.FrequencyForm import Ui_MainForm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        self.path = ""
        self.filename = ""

        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        self.ui.open_btn.clicked.connect(self.btn_open_clicked)
        self.ui.analysis_btn.clicked.connect(self.btn_analysis_clicked)
        self.ui.exit_btn.clicked.connect(self.btn_exit_clicked)

        self.show()

    @staticmethod
    def signal_noise(freqArray, db):
        from statistics import mean

        start = 0
        new_db = []
        all_sigma = []
        all_mean = []
        for i in range(len(freqArray)):
            if freqArray[i] - freqArray[start] <= 100.0:
                new_db.append(db[i])
            else:
                mean_new_db = mean(new_db)
                sum1 = 0
                sum2 = 0
                for j in range(len(new_db)):
                    sum1 += new_db[j] ** 2
                    sum2 += new_db[j]
                from math import sqrt
                sigma_b = sqrt(sum1 / len(new_db) - (sum2 / len(new_db)) ** 2)
                all_sigma.append(sigma_b)
                all_mean.append(mean_new_db)
                start = i
                new_db = [db[start]]

        if len(new_db):
            mean_new_db = mean(new_db)
            sum1 = 0
            sum2 = 0
            for j in range(len(new_db)):
                sum1 += new_db[j] ** 2
                sum2 += new_db[j]
            from math import sqrt
            sigma_b = sqrt(sum1 / len(new_db) - (sum2 / len(new_db)) ** 2)
            all_sigma.append(sigma_b)
            all_mean.append(mean_new_db)

        sum1 = 0
        sum2 = 0
        for j in range(len(all_sigma)):
            sum1 += all_sigma[j] ** 2
            sum2 += (all_sigma[j] - all_mean[j]) ** 2
        GSSNR = sum1 / sum2
        return GSSNR

    @staticmethod
    def gssnr_analysis(gssnr_blocks):
        gssnr_blocks = gssnr_blocks[6:]
        flag = True
        model = []
        for i in range(1, len(gssnr_blocks)):
            if not flag:
                if gssnr_blocks[i] - gssnr_blocks[i - 1] <= 0:
                    continue
                elif gssnr_blocks[i] - gssnr_blocks[i - 1] > 0:
                    model.append('min')
                    flag = True
            else:
                if gssnr_blocks[i] - gssnr_blocks[i - 1] >= 0:
                    continue
                elif gssnr_blocks[i] - gssnr_blocks[i - 1] < 0:
                    model.append('max')
                    flag = False
        if len(model) >= 3 and model[0] == 'max' and model[1] == 'min' and model[len(model) - 1] == 'max':
            return True
        else:
            return False

    def build_plots(self):
        sample_rate, wave_data = wavfile.read(self.path)

        channel1 = wave_data[:, 0]
        channel2 = wave_data[:, 1]
        time = np.arange(0, float(wave_data.shape[0] / sample_rate), 1 / sample_rate)

        plt.figure(figsize=(8, 7))
        plt.subplot(211).set_title('Левый канал')
        plt.plot(time, channel1)
        plt.ylabel('Амлитуда (метры)')
        plt.subplot(212).set_title('Правый канал')
        plt.plot(time, channel2)
        plt.xlabel('Время (сек)')
        plt.ylabel('Амлитуда (метры)')
        plt.savefig('wave.png')
        pixmap_wave = QPixmap('wave.png')

        self.ui.wave_image.setPixmap(pixmap_wave)
        self.resize(pixmap_wave.width(), pixmap_wave.height())

        fft_data = abs(fft(channel1))
        n = len(channel1)
        fft_data = fft_data[0:(n // 2)]
        fft_data = fft_data / float(n)
        freqArray = np.arange(0, (n // 2), 1.0) * (sample_rate * 1.0 / n)
        db = 10 * np.log10(fft_data)

        plt.figure(figsize=(8, 7))
        plt.plot(freqArray, db)
        plt.xlabel('Частота (Гц)')
        plt.ylabel('Мощность (дБ)')
        plt.savefig('fft.png')
        pixmap_fft = QPixmap('fft.png')

        self.ui.fft_image.setPixmap(pixmap_fft)
        self.resize(pixmap_fft.width(), pixmap_fft.height())
        return freqArray, db

    def signal_noise_not_equal(self, freqArray, db, GSSNR1):
        from statistics import mean

        start = 0
        k = 1
        new_db = []
        all_sigma = []
        all_mean_sigma = []
        x = []
        all_GSSNR_blocks = []
        for i in range(len(freqArray)):
            if freqArray[i] - freqArray[start] <= 100.0 * k:
                new_db.append(db[i])
            else:
                n = len(new_db) // (10 * k)
                st = 0
                while st < len(new_db):
                    new_new_db = new_db[st:min(st + n, len(new_db))]
                    st += n
                    if st + n >= len(new_db):
                        while st < len(new_db):
                            new_new_db.append(new_db[st])
                            st += 1
                    mean_new_new_db = mean(new_new_db)
                    sum1 = 0
                    sum2 = 0
                    for j in range(len(new_new_db)):
                        sum1 += new_new_db[j] ** 2
                        sum2 += new_new_db[j]
                    from math import sqrt
                    sigma_b = sqrt(sum1 / len(new_new_db) - (sum2 / len(new_new_db)) ** 2)
                    all_sigma.append(sigma_b)
                    all_mean_sigma.append(mean_new_new_db)

                sum1 = 0
                sum2 = 0
                for j in range(len(all_sigma)):
                    sum1 += all_sigma[j] ** 2
                    sum2 += (all_sigma[j] - all_mean_sigma[j]) ** 2
                GSSNR_blocks = sum1 / sum2
                all_GSSNR_blocks.append(GSSNR_blocks)
                x.append(freqArray[i])
                k += 1

        if len(new_db):
            n = len(new_db) // (10 * k)
            st = 0
            while st < len(new_db):
                new_new_db = new_db[st:min(st + n, len(new_db))]
                st += n
                if st + n >= len(new_db):
                    while st < len(new_db):
                        new_new_db.append(new_db[st])
                        st += 1
                mean_new_new_db = mean(new_new_db)
                sum1 = 0
                sum2 = 0
                for j in range(len(new_new_db)):
                    sum1 += new_new_db[j] ** 2
                    sum2 += new_new_db[j]
                from math import sqrt
                sigma_b = sqrt(sum1 / len(new_new_db) - (sum2 / len(new_new_db)) ** 2)
                all_sigma.append(sigma_b)
                all_mean_sigma.append(mean_new_new_db)
                st += n

            sum1 = 0
            sum2 = 0
            for j in range(len(all_sigma)):
                sum1 += all_sigma[j] ** 2
                sum2 += (all_sigma[j] - all_mean_sigma[j]) ** 2
            GSSNR_blocks = sum1 / sum2
            all_GSSNR_blocks.append(GSSNR_blocks)

            x.append(freqArray[len(freqArray) - 1])

        plt.figure(figsize=(8, 7))
        for i in range(6, len(x)):
            if i == 6:
                plt.plot(x[i], all_GSSNR_blocks[i], 'go', label='значения GSSNR')
            else:
                plt.plot(x[i], all_GSSNR_blocks[i], 'go')
        plt.plot(x, all_GSSNR_blocks, '--b', label='GSSNR интервалов')
        plt.plot(freqArray, [GSSNR1] * len(freqArray), 'r', label='GSSNR аудиофайла')
        plt.legend(loc='upper right')
        plt.xlabel('Частота (Гц)')
        plt.ylabel('GSSNR')
        plt.savefig('gssnr.png')
        pixmap_gssnr = QPixmap('gssnr.png')

        self.ui.gssnr_image.setPixmap(pixmap_gssnr)
        self.resize(pixmap_gssnr.width(), pixmap_gssnr.height())
        return all_GSSNR_blocks

    def frequency_analysing(self):
        freqArray, db = self.build_plots()
        GSSNR = self.signal_noise(freqArray, db)
        gssnr_blocks = self.signal_noise_not_equal(freqArray, db, GSSNR)

        if self.gssnr_analysis(gssnr_blocks):
            self.ui.parameters_text.append(
                'Требуется проведение дальнейшего анализа, в файл {} возможно вносились изменения\n'.format(
                    self.filename))
        else:
            self.ui.parameters_text.append(
                'В файл {} вносились изменения\n'.format(self.filename))

    def btn_open_clicked(self):
        options = QFileDialog.Options()
        self.path, _ = QFileDialog.getOpenFileName(self, "Выберите аудиофайл", "",
                                                   "All Files (*);;VLC media file (*.wav *.mp3 *.ogg *.flac *.aiff)",
                                                   options=options)
        self.ui.path_line.setText(self.path)
        self.filename = self.path[self.path.rfind('/') + 1::]

    def btn_analysis_clicked(self):
        self.ui.parameters_text.clear()
        self.ui.wave_image.clear()
        self.ui.fft_image.clear()
        self.ui.gssnr_image.clear()

        file_format = self.filename[self.filename.rfind('.') + 1:len(self.filename)]
        if file_format != 'wav':
            self.ui.parameters_text.append(
                "Вы выбрали неправильный формат аудиофайла, ожидался wav, приняли {}".format(file_format))
            return
        file = open(self.path, "rb")
        self.ui.parameters_text.append("Начинается анализ wav-файла: {}\n".format(self.filename))
        flag = True
        ChunkID = str(file.read(4), encoding="utf-8")
        if ChunkID != 'RIFF':
            flag = False
        ChunkSizeString = file.read(4)
        ChunkSize = struct.unpack('I', ChunkSizeString)
        TotalSize = ChunkSize[0] + 8
        Format = str(file.read(4), encoding="utf-8")

        if Format != 'WAVE':
            flag = False

        SubChunk1ID = str(file.read(4), encoding="utf-8")

        if SubChunk1ID != 'fmt ':
            flag = False

        SubChunk1SizeString = file.read(4)
        SubChunk1Size = struct.unpack("I", SubChunk1SizeString)

        AudioFormatString = file.read(2)
        AudioFormat = struct.unpack("H", AudioFormatString)

        NumChannelsString = file.read(2)
        NumChannels = struct.unpack("H", NumChannelsString)

        SampleRateString = file.read(4)
        SampleRate = struct.unpack("I", SampleRateString)

        ByteRateString = file.read(4)
        ByteRate = struct.unpack("I", ByteRateString)

        BlockAlignString = file.read(2)
        BlockAlign = struct.unpack("H", BlockAlignString)

        BitsPerSampleString = file.read(2)
        BitsPerSample = struct.unpack("H", BitsPerSampleString)

        SubChunk2ID = str(file.read(4), encoding="utf-8")

        if SubChunk2ID != 'data':
            flag = False

        SubChunk2SizeString = file.read(4)
        SubChunk2Size = struct.unpack("I", SubChunk2SizeString)

        if flag:
            self.ui.parameters_text.append('Параметры аудиофайла {}:\n'.format(self.filename))
            self.ui.parameters_text.append("ChunkID = {}\n".format(ChunkID))
            self.ui.parameters_text.append("Формат = {}\n".format(Format))
            self.ui.parameters_text.append("SubChunk1ID = {}\n".format(SubChunk1ID))
            self.ui.parameters_text.append("Размер SubChunk1 = {} байт\n".format(str(SubChunk1Size[0])))
            self.ui.parameters_text.append("AudioFormat = {}\n".format(str(AudioFormat[0])))
            self.ui.parameters_text.append("Количество каналов = {}\n".format(str(NumChannels[0])))
            self.ui.parameters_text.append("Частота дискретизации = {} Гц\n".format(str(SampleRate[0])))
            self.ui.parameters_text.append("Байтрейт = {} байт/сек\n".format(str(ByteRate[0])))
            self.ui.parameters_text.append("BlockAlign = {}\n".format(str(BlockAlign[0])))
            self.ui.parameters_text.append("Бит на семпл = {} бит\n".format(str(BitsPerSample[0])))
            self.ui.parameters_text.append("SubChunk2ID = {}\n".format(SubChunk2ID))
            self.ui.parameters_text.append("Размер SubChunk2 = {} Мб\n".format(str(SubChunk2Size[0] / (1024 * 1024))))
            self.ui.parameters_text.append("Исходный размер = {} Мб\n".format(str(TotalSize / (1024 * 1024))))

            self.ui.parameters_text.append('Наличие изменений в аудиофайле {}:\n'.format(self.filename))

            self.frequency_analysing()

            self.ui.parameters_text.append("Анализ файла {} закончен".format(self.filename))
        else:
            self.ui.parameters_text.append("Ваш wav-файл повреждён, программа завершена")

    def btn_exit_clicked(self):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
