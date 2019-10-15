import struct


def get_info(filename, path):
    file_format = filename[(filename.rfind('.') + 1)::]
    if file_format != 'wav':
        # Show Window with error
        return
    file = open(path, "rb")
    # self.ui.parameters_text.append("Начинается анализ wav-файла: {}\n".format(self.filename))
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