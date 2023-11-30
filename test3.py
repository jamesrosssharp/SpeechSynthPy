
from scipy.io import wavfile
import numpy as np

e = [ 1.,         -1.39633296,  0.46841189, -0.69600425,  1.17562901, -0.40912892,
  0.37339634, -1.02903467,  0.53459021,  0.011124,    0.03056732]
ll = [ 1.,         -2.31290523,  1.49606326, -0.15547028,  0.56006575, -0.79852425,
  0.16184324, -0.10320262,  0.2785704,  -0.10148356, -0.00666854]
oo = [ 1.,         -2.01650881,  1.00826265,  0.23934394,  0.07632905, -0.32807819,
  0.05059092, -0.16244381,  0.18058969,  0.02267418, -0.03044778]
u = [ 1.,         -2.55766909,  2.83532354, -2.20451397,  1.90039137, -2.00072789,
  2.11747837, -1.541302,    0.78850204, -0.47432413,  0.2108129 ]
a = [ 1.,         -1.75077479,  1.29385398, -0.91167159,  0.99413484, -1.2149513,
  1.24028589, -1.24257103,  1.02673807, -0.77943757,  0.43060488]

hello = [(a, 2000, 500), (u, 500, 500), (a, 100, 100)]

count = 0

dsyn = []

delay = np.zeros(10)

taps = np.zeros(11)

for (phoneme, length, interp) in hello:

    taps_lerp = (np.array(phoneme) - taps) / interp
#    taps = phoneme

    for i in range(0, length + interp):

        if (i < interp):
            taps += taps_lerp
        
        pulse = 0

        if count == 37:
            pulse = 1.0
            count = 0
        
        count += 1

        accu = pulse
        for i, coeff in enumerate(taps[1:]):
            print("i: %d coeff: %f delay[i]: %f" % (i, coeff, delay[i]))
            accu -= coeff * delay[i]
        
        dsyn.append(accu)

        delay[1:] = delay[:-1]
        delay[0] = accu
        print (taps)
        print (delay)

dsyn = np.array(dsyn)
dsyn *= 32768 * 0.1

wavfile.write("hello?.wav", 6000, dsyn.astype(np.int16))
