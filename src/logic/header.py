import struct
from datetime import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from frames.header import Ui_FrameHeader

from logic import collect

from formats.wav_formats import get_AudioFormat

INVALID_FORMAT = "Некорректный формат файла."
CORRUPT = "Не удаётся прочитать данные файла."

FORMAT = {
    0: "бит",
    1: "байт",
    2: "Кбайт",
    3: "Мбайт",
    4: "Гбайт"
}

DELETIONS = (8, 1024, 1024, 1024, 1024,)


class FrameHeader(QMainWindow):
    def __init__(self, wav_info, parent=None):
        super(FrameHeader, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_FrameHeader()
        self.ui.setupUi(self)

        self.ui.buttonOk.clicked.connect(self.ok)

        self.fill_table(wav_info)

        self.show()

    def ok(self):
        collect()
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

        collect()


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
        return wav_info, INVALID_FORMAT, -3, '', ''
    file = open(path, "rb")

    ChunkID = str(file.read(4), encoding="utf-8")
    if ChunkID != 'RIFF':
        return wav_info, CORRUPT, -1, ['ChunkID', 'RIFF', ChunkID]

    ChunkSize = struct.unpack('I', file.read(4))[0]

    Format = str(file.read(4), encoding="utf-8")
    if Format != 'WAVE':
        return wav_info, CORRUPT, -1, ['Format', 'WAVE', Format]

    Subchunk1ID = str(file.read(4), encoding="utf-8")
    if Subchunk1ID != 'fmt ':
        return wav_info, CORRUPT, -1, ['Subchunk1ID', 'fmt ', Subchunk1ID]

    Subchunk1Size = struct.unpack("I", file.read(4))[0]
    AudioFormat = struct.unpack("H", file.read(2))[0]
    NumChannels = struct.unpack("H", file.read(2))[0]
    SampleRate = struct.unpack("I", file.read(4))[0]
    ByteRate = struct.unpack("I", file.read(4))[0]
    BlockAlign = struct.unpack("H", file.read(2))[0]
    BitsPerSample = struct.unpack("H", file.read(2))[0]

    Subchunk2ID = str(file.read(4), encoding="utf-8")
    if Subchunk2ID != 'data':
        return wav_info, CORRUPT, -1, ['Subchunk2ID', 'data', Subchunk2ID]

    Subchunk2Size = struct.unpack("I", file.read(4))[0]

    if ByteRate != SampleRate * NumChannels * BitsPerSample // 8:
        return wav_info, CORRUPT, -2, ['Байтрейт', 'Частота дискретизации * Количество каналов * Бит в сэмпле / 8']

    if BlockAlign != NumChannels * BitsPerSample // 8:
        return wav_info, CORRUPT, -2, ['Байт на сэмпл', 'Количество каналов * Бит в сэмпле / 8']

    DurationSeconds = Subchunk2Size / (BitsPerSample / 8) / NumChannels / SampleRate
    DurationMinutes = int(DurationSeconds / 60)
    DurationHours = int(DurationSeconds / 3600)
    DurationSeconds = int(DurationSeconds - (DurationMinutes * 60) - (DurationHours * 3600))

    duration = time(DurationHours, DurationMinutes, DurationSeconds)

    wav_info = [filename, duration, ChunkID, format_determine(ChunkSize), Format, Subchunk1ID,
                "{} бит".format(Subchunk1Size),
                get_AudioFormat(AudioFormat), NumChannels, "{} Гц".format(SampleRate), "{} байт/сек".format(ByteRate),
                "{} байт".format(BlockAlign), "{} бит".format(BitsPerSample), Subchunk2ID,
                format_determine(Subchunk2Size)]

    return wav_info, "", NumChannels, []
