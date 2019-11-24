import struct
from datetime import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from frames.header import Ui_FrameHeader

from formats.wav_formats import get_AudioFormat

INVALID_FORMAT = "Некорректный формат файла."
CORRUPT = "Не удаётся открыть файл. Возможно он повреждён."

FORMAT = {
    0: "бит",
    1: "байт",
    2: "Кбайт",
    3: "Мбайт",
    4: "Гбайт"
}

DELETIONS = (8, 1024, 1024, 1024, 1024,)


class FrameHeader(QWidget):
    def __init__(self, wav_info):
        super(FrameHeader, self).__init__()

        self.ui = Ui_FrameHeader()
        self.ui.setupUi(self)

        self.ui.buttonOk.clicked.connect(self.ok)

        self.fill_table(wav_info)

        self.show()

    def ok(self):
        self.close()

    def fill_table(self, wav_info):
        self.ui.tableInfo.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.tableInfo.verticalHeader().setDefaultSectionSize(30)

        rows = self.ui.tableInfo.rowCount()
        columns = self.ui.tableInfo.columnCount()
        for i in range(rows):
            for j in range(columns):
                item = QTableWidgetItem(str(wav_info[i + j]))
                item.setFlags(Qt.ItemIsEnabled)
                self.ui.tableInfo.setItem(i, j, item)


def format_determine(value):
    deletions = 0

    while deletions < 4:
        val = value / DELETIONS[deletions]

        if val <= 1:
            return "{} {}".format(round(value, 1), FORMAT[deletions])

        value = val
        deletions += 1

    return "{} {}".format(round(value, 1), FORMAT[deletions])


def get_header(path, filename):
    wav_info = []

    file_format = path[(path.rfind('.') + 1):]
    if file_format != 'wav':
        return wav_info, INVALID_FORMAT, 0
    file = open(path, "rb")

    ChunkID = str(file.read(4), encoding="utf-8")
    if ChunkID != 'RIFF':
        return wav_info, CORRUPT, 0

    ChunkSize = struct.unpack('I', file.read(4))[0]

    Format = str(file.read(4), encoding="utf-8")
    if Format != 'WAVE':
        return wav_info, CORRUPT, 0

    Subchunk1ID = ''
    while True:
        try:
            fmt = str(file.read(2), encoding="utf-8")
            if fmt == 'fm':
                fmt = str(file.read(2), encoding="utf-8")
                if fmt == 't ':
                    Subchunk1ID = 'fmt '
                break
        except:
            continue

    if Subchunk1ID != 'fmt ':
        return wav_info, CORRUPT, 0

    # Subchunk1ID = str(file.read(4), encoding="utf-8")
    # if Subchunk1ID != 'fmt ':
    #     return wav_info, CORRUPT, 0

    Subchunk1Size = struct.unpack("I", file.read(4))[0]
    AudioFormat = struct.unpack("H", file.read(2))[0]
    NumChannels = struct.unpack("H", file.read(2))[0]
    SampleRate = struct.unpack("I", file.read(4))[0]
    ByteRate = struct.unpack("I", file.read(4))[0]
    BlockAlign = struct.unpack("H", file.read(2))[0]
    BitsPerSample = struct.unpack("H", file.read(2))[0]

    # TODO: correct read of Subchunk2ID?

    Subchunk2ID = ''
    while True:
        try:
            data = str(file.read(2), encoding="utf-8")
            if data == 'da':
                data = str(file.read(2), encoding="utf-8")
                if data == 'ta':
                    Subchunk2ID = 'data'
                break
        except:
            continue

    if Subchunk2ID != 'data':
        return wav_info, CORRUPT, 0

    # Subchunk2ID = str(file.read(4), encoding="utf-8")
    # if Subchunk1ID != 'data':
    #     return wav_info, CORRUPT, 0

    Subchunk2Size = struct.unpack("I", file.read(4))[0]

    if ByteRate != SampleRate * NumChannels * BitsPerSample // 8:
        return wav_info, CORRUPT, 0

    if BlockAlign != NumChannels * BitsPerSample // 8:
        return wav_info, CORRUPT, 0

    DurationSeconds = Subchunk2Size / (BitsPerSample / 8) / NumChannels / SampleRate
    DurationMinutes = int(DurationSeconds / 60)
    DurationHours = int(DurationSeconds / 3600)
    DurationSeconds = int(DurationSeconds - (DurationMinutes * 60) - (DurationHours * 3600))

    duration = time(DurationHours, DurationMinutes, DurationSeconds)

    # TODO: add formats: Gz, Mb, etc.
    #  Convert to b, Kb, Mb or Gb
    #  Add translation for Format: PCM = 1, etc. Find another Formats
    #  Convert ints to str

    wav_info = [filename, duration, ChunkID, format_determine(ChunkSize), Format, Subchunk1ID, "{} бит".format(Subchunk1Size),
                get_AudioFormat(AudioFormat), NumChannels, "{} Гц".format(SampleRate), "{} байт/сек".format(ByteRate),
                "{} байт".format(BlockAlign), "{} бит".format(BitsPerSample), Subchunk2ID,
                format_determine(Subchunk2Size)]

    return wav_info, "", NumChannels

    # if flag:
    #     self.ui.parameters_text.append('Параметры аудиофайла {}:\n'.format(self.filename))
    #     self.ui.parameters_text.append("ChunkID = {}\n".format(ChunkID))
    #     self.ui.parameters_text.append("Формат = {}\n".format(Format))
    #     self.ui.parameters_text.append("Subchunk1ID = {}\n".format(Subchunk1ID))
    #     self.ui.parameters_text.append("Размер SubChunk1 = {} байт\n".format(str(Subchunk1Size[0])))
    #     self.ui.parameters_text.append("AudioFormat = {}\n".format(str(AudioFormat[0])))
    #     self.ui.parameters_text.append("Количество каналов = {}\n".format(str(NumChannels[0])))
    #     self.ui.parameters_text.append("Частота дискретизации = {} Гц\n".format(str(SampleRate[0])))
    #     self.ui.parameters_text.append("Байтрейт = {} байт/сек\n".format(str(ByteRate[0])))
    #     self.ui.parameters_textappend("BlockAlign = {}\n".format(str(BlockAlign[0])))
    #     self.ui.parameters_text.append("Бит на семпл = {} бит\n".format(str(BitsPerSample[0])))
    #     self.ui.parameters_text.append("Subchunk2ID = {}\n".format(Subchunk2ID))
    #     self.ui.parameters_text.append("Размер SubChunk2 = {} Мб\n".format(str(Subchunk2Size[0] / (1024 * 1024))))
    #     self.ui.parameters_text.append("Исходный размер = {} Мб\n".format(str(TotalSize / (1024 * 1024))))
    #
    #     self.ui.parameters_text.append('Наличие изменений в аудиофайле {}:\n'.format(self.filename))
    #
    #     self.frequency_analysing()
    #
    #     self.ui.parameters_text.append("Анализ файла {} закончен".format(self.filename))
    # else:
    #     self.ui.parameters_text.append("Ваш wav-файл повреждён, программа завершена")
