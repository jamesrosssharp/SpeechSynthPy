import functions
import numpy as np

from scipy.io import wavfile
samplerate, data = wavfile.read('../samples/s.wav')

decim = 8

data = np.array([d / 32768.0 for d in data])

LPC = functions.LPCEncode(data, decim)

functions.LPCDecodeNoise(LPC, len(data) // decim, len(data)*100, 37, 0.2, "../out/s.wav", samplerate // decim)    
