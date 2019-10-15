import struct

from frames.info import Ui_FrameInfo

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

INVALID_FORMAT = "Некорректный формат файла."
CORRUPT = "Не удаётся открыть файл. Возможно он повреждён."


class FrameInfo(QWidget):
    def __init__(self, wav_info):
        super(FrameInfo, self).__init__()

        self.ui = Ui_FrameInfo()
        self.ui.setupUi(self)

        self.ui.buttonOk.clicked.connect(self.ok)
        self.fill_table(wav_info)

        self.show()

    def ok(self):
        self.close()

    def fill_table(self, wav_info):
        rows = self.ui.tableInfo.rowCount()
        columns = self.ui.tableInfo.columnCount()
        for i in range(rows):
            for j in range(columns):
                item = QTableWidgetItem(str(wav_info[i + j]))
                item.setFlags(Qt.ItemIsEnabled)
                # TODO: remove scroll, remove resizing rows
                self.ui.tableInfo.setItem(i, j, item)


def get_info(path, filename):
    wav_info = []

    file_format = path[(path.rfind('.') + 1):]
    if file_format != 'wav':
        return wav_info, INVALID_FORMAT
    file = open(path, "rb")

    ChunkID = str(file.read(4), encoding="utf-8")
    if ChunkID != 'RIFF':
        return wav_info, CORRUPT

    ChunkSize = struct.unpack('I', file.read(4))[0]
    # TODO: NEED?
    TotalSize = ChunkSize + 8

    Format = str(file.read(4), encoding="utf-8")
    if Format != 'WAVE':
        return wav_info, CORRUPT

    Subchunk1ID = str(file.read(4), encoding="utf-8")
    if Subchunk1ID != 'fmt ':
        return wav_info, CORRUPT

    Subchunk1Size = struct.unpack("I", file.read(4))[0]
    AudioFormat = struct.unpack("H", file.read(2))[0]
    NumChannels = struct.unpack("H", file.read(2))[0]
    SampleRate = struct.unpack("I", file.read(4))[0]
    ByteRate = struct.unpack("I", file.read(4))[0]
    BlockAlign = struct.unpack("H", file.read(2))[0]
    BitsPerSample = struct.unpack("H", file.read(2))[0]

    Subchunk2ID = str(file.read(4), encoding="utf-8")
    if Subchunk2ID != 'data':
        return wav_info, CORRUPT

    Subchunk2Size = struct.unpack("I", file.read(4))[0]

    if ByteRate != SampleRate * NumChannels * BitsPerSample // 8:
        return wav_info, CORRUPT

    if BlockAlign != NumChannels * BitsPerSample // 8:
        return wav_info, CORRUPT

    # TODO: add formats: Gz, Mb, etc. Convert to b, Kb, Mb or Gb
    #  Add translation for Format: PCM = 1, etc. Find another Formats
    #  Convert ints to str

    wav_info = [filename, TotalSize, ChunkID, ChunkSize, Format, Subchunk1ID, Subchunk1Size, AudioFormat, NumChannels,
                SampleRate, ByteRate, BlockAlign, BitsPerSample, Subchunk2ID, Subchunk2Size]

    return wav_info, ""

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
    #     self.ui.parameters_text.append("BlockAlign = {}\n".format(str(BlockAlign[0])))
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
