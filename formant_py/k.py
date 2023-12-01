import functions
import numpy as np

from scipy.io import wavfile
samplerate, data = wavfile.read('../samples/k.wav')

decim = 8

data = np.array([d / 32768.0 for d in data])

DSIZE = decim * 50

for i in range(0, len(data) // DSIZE):

    LPC = functions.LPCEncode(data[i*DSIZE:(i+1)*DSIZE], decim)

    functions.LPCDecodeNoise(LPC, DSIZE // decim, DSIZE // decim, 37, 0.1, "../out/k.wav", samplerate // decim)    
