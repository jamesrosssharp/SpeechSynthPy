import functions
import numpy as np

from scipy.io import wavfile
samplerate, data = wavfile.read('../samples/rr.wav')

decim = 8

data = np.array([d / 32768.0 for d in data])

LPC = functions.LPCEncode(data, decim)

functions.LPCDecode(LPC, len(data) // decim, len(data)*100, 37, 0.1, "../out/rr.wav", samplerate // decim)    
