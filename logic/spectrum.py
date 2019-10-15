import numpy
from matplotlib import pyplot
import scipy.io.wavfile

window_size = 2048
window_step = 512
file = input()
sample_rate, wave_data = scipy.io.wavfile.read(file)
if isinstance(wave_data[0], numpy.ndarray):
    wave_data = wave_data.mean(1)

plot = pyplot.figure()
axes = plot.add_axes((0.1, 0.1, 0.8, 0.8))
axes.specgram(wave_data,  NFFT=window_size, noverlap=window_size - window_step, Fs=sample_rate)
pyplot.show()