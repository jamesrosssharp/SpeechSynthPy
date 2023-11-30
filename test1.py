import numpy as np
from scipy.signal import lfilter
from scipy.io import wavfile
samplerate, data = wavfile.read('samples/ae2.wav')

from matplotlib import pyplot as plt

decim = 8

data = np.array([d / 32768.0 for d in data])

#plt.plot(data)
#plt.show()

from scipy.linalg import solve_toeplitz, toeplitz
import numpy as np

from scipy.signal import decimate

data = decimate(data, decim)

def Autocor(signal, k):

    if k == 0:
        return np.sum(signal**2)
    else:
        return np.sum(signal[k:]*signal[:-k])

def Levinson(w_sig, p):
    r_list = [Autocor(w_sig, i) for i in range(p)]
    b_list = [Autocor(w_sig, i) for i in range(1, p + 1)]
    LPC = solve_toeplitz((r_list, r_list), b_list)
    return LPC

#for n in range(3,12):
n = 10
LPC = Levinson(data, n)
LPC = np.insert(-LPC, 0, 1)
print(LPC)

# Synthesize

syn = np.zeros(len(data)*10)
syn[::38] = 1.0

#syn = np.random.normal(loc = 0.0, scale = 1.0, size = len(data)*10)

dsyn = lfilter([1], LPC, syn) / 4

plt.plot(data)
plt.plot(dsyn, 'k')
plt.show()

wavfile.write("test.wav", samplerate // decim, dsyn / 5.0)
