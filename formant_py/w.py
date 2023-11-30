import functions
import numpy as np

from scipy.io import wavfile
samplerate, data = wavfile.read('../samples/w.wav')

decim = 8

data = np.array([d / 32768.0 for d in data])

for i in range(0, 10):

    LPC = functions.LPCEncode(data[i*100:(i+1)*100], decim)

    functions.LPCDecode(LPC, 100 // decim, 100 // decim, 37, 0.1, "../out/w.wav", samplerate // decim)    
