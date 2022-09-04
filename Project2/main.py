from scipy.io import wavfile
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
def plot_main_signal():      #a
    T,wave=scipy.io.wavfile.read("tone.wav")
    # T,wave=scipy.io.wavfile.read("sample.wav")
    wave=wave[:25000]
    t=np.arange(0,25000/T,1/T)
    plt.plot(t,wave)
    plt.show()




def fourier():     #b
    T, t = scipy.io.wavfile.read("tone.wav")
    # # T, wave = scipy.io.wavfile.read("sample.wav")

    x = np.fft.fft(np.sin(t))
    x = x*(2/len(x))
    sampleRate=1/T
    freq = np.fft.fftfreq(len(t),d=sampleRate)
    freq2, x2 = [], []
    freq3, x3 = [], []
    for i in range (len(x)):
        if x.real[i]>0:
            freq2.append(freq[i])
            x2.append(x.real[i])

    for i in range (len(x2)):
        if freq2[i]>0 and freq2[i]< 2000:
            freq3.append(freq2[i])
            x3.append(x2[i])

    plt.plot(freq3,x3)
    plt.show()


def imshow(sample):
    # T, t = scipy.io.wavfile.read("tone.wav")
    rate, data = scipy.io.wavfile.read("sample.wav")

    signal_array = []
    line = int(data.size/2048)+1
    for i in range(sample-1):
        arr = []
        for j in range(line):
            arr.append(data[(line)*i + j])
        signal_array.append(arr)

    arr = []
    for i in range (line * (sample-1), data.size):
            arr.append(data[i])
    signal_array.append(arr)

    fourie_x = []
    fourie_freq = []

    for i in range(len(signal_array)):
        x = np.fft.fft(np.sin(signal_array[i]))
        fourie_x.append(x)
        sampleRate = 1 / rate
        freq = np.fft.fftfreq(len(signal_array[i]), d=sampleRate)
        fourie_freq.append(freq)

    plt.imshow(fourie_x)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    plot_main_signal()
    fourier()
    # imshow(2048)
    # imshow(1024)
    # imshow(4096)
