from scipy.io import wavfile
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
def plot_main_signal():
    T,wave=scipy.io.wavfile.read("sound.wav")
    wave=wave[:1000]
    t=np.arange(0,1000/T,1/T)
    plt.plot(t,wave)
    plt.show()

def fourier():
    T, wave = scipy.io.wavfile.read("sound.wav")
    k, t=150, 61
    omega=np.pi*2/t
    ak=[]
    for i in range(k+1):
        bk, ck= 0, 0
        for s in range (t-1):
            bk+=wave[s]*np.cos(s*i*omega)
            ck+=wave[s]*np.sin(s*i*omega)
        bk*=1/t
        ck*=1/t
        ak.append(complex(bk,-ck))
    for z in range(len(ak)):
        ak[z]=abs(ak[z])
    time=np.linspace(0,T,k+1)
    plt.stem(time,ak+bk)
    plt.show()


def frequency():
    counter=0
    T, wave = scipy.io.wavfile.read("sound.wav")
    for i in range(0, T-1):
        if wave[i] < 0 and wave[i + 1] > 0 :
            counter+=1
    print('Frequency:', counter*T/wave[0])

if __name__ == '__main__':
    plot_main_signal()
    fourier()
    frequency()
