import numpy as np
from scipy.signal import lfilter
from scipy.io import wavfile

from matplotlib import pyplot as plt

#plt.plot(data)
#plt.show()

from scipy.linalg import solve_toeplitz, toeplitz
import numpy as np

from scipy.signal import decimate

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

def LPCEncode(data, decim, n = 10):

    data = decimate(data, decim)

    #for n in range(3,12):
    #n = 10
    LPC = Levinson(data, n)
    LPC = np.insert(-LPC, 0, 1)
    print(LPC)

    plt.plot(data)
    return LPC

def LPCDecode(LPC, orig_length, length, period, gain, wav, samplerate):

    # Synthesize

    syn = np.zeros(length)
    syn[::period] = 1.0


    dsyn = lfilter([1], LPC, syn) * gain

    plt.plot(dsyn[:orig_length], 'k')
    plt.show()

    dsyn *= 32768.0

    wavfile.write(wav, samplerate, dsyn.astype(np.int16))
