
from scipy.io import wavfile
import numpy as np

e = [ 1.,         -1.39633296,  0.46841189, -0.69600425,  1.17562901, -0.40912892,
  0.37339634, -1.02903467,  0.53459021,  0.011124,    0.03056732]
#ll = [ 1.,         -2.31290523,  1.49606326, -0.15547028,  0.56006575, -0.79852425,
#  0.16184324, -0.10320262,  0.2785704,  -0.10148356, -0.00666854]
#ll = [1.000000, -2.077153, 1.121301, 0.104632, 0.017396, -0.105020, -0.112899, 0.063954, 0.112775, -0.216031, 0.115757]
ll = [1.000000, -1.955699, 1.335746, -0.553353, 0.730732, -1.270587, 1.534098, -1.089953, 0.664223, -0.691521, 0.348346]

oo = [ 1.,         -2.01650881,  1.00826265,  0.23934394,  0.07632905, -0.32807819,
  0.05059092, -0.16244381,  0.18058969,  0.02267418, -0.03044778]
u = [ 1.,         -2.55766909,  2.83532354, -2.20451397,  1.90039137, -2.00072789,
  2.11747837, -1.541302,    0.78850204, -0.47432413,  0.2108129 ]
rr = [ 1.,         -3.01250585,  4.18476758, -3.93516425,  3.25794138, -2.92736639,
  2.86889721, -2.50135287,  1.82227749, -1.0700554,   0.3402342 ]
null = np.zeros(11)

er = [1.000000, -1.647412, 0.757628, -0.528415, 0.690910, -0.188210, 0.506061, -0.875655, 0.207391, 0.041742, 0.086520]

w1 = [1.000000, -1.070782, 0.118038, -0.125481, 0.026854, 0.112460, -0.085232, -0.075794, 0.117928, 0.093062, -0.075123]
w2 = [1.000000, -1.080115, 0.155698, -0.135259, 0.232103, 0.040086, -0.213449, 0.058073, 0.031447, 0.048606, -0.051928]
w3 = [1.000000, -1.575516, 0.475914, 0.232985, -0.043798, -0.153551, 0.116322, -0.069693, 0.041678, 0.000064, 0.021572]
w4 = [1.000000, -1.419174, 0.179733, 0.168772, 0.204685, 0.102483, -0.235251, -0.084305, 0.110172, 0.103416, -0.049310]
w5 = [1.000000, -1.313828, 0.204704, 0.121689, 0.133914, -0.011800, -0.049396, -0.011630, -0.018828, -0.027333, 0.073420]
w6 = [1.000000, -1.414232, 0.321199, 0.130871, 0.077759, -0.007974, -0.086803, -0.019539, 0.086778, 0.004879, -0.020285]
w7 = [1.000000, -1.500472, 0.368633, 0.244047, 0.048297, -0.057437, -0.089109, 0.022730, -0.026078, 0.114067, -0.051491]
w8 = [1.000000, -1.284910, 0.251496, 0.037871, 0.051694, 0.038931, 0.075938, -0.048721, -0.079061, 0.011004, 0.048463]
WLEN = 40

d1 = [1.000000, -0.557151, 0.132137, -0.656529, 0.005821, 0.133759, -0.025523, 0.009056, -0.011924, -0.027860, 0.048778]
d2 = [1.000000, -0.420020, -0.270654, -0.276628, -0.065789, 0.344115, 0.105167, -0.422662, -0.142296, 0.101721, 0.129642]
d3 = [1.000000, -0.423891, -0.247666, -0.107214, -0.305814, 0.234865, 0.152175, -0.115070, 0.083101, -0.215564, 0.068232]
d4 = [1.000000, -1.103021, 0.532646, -0.554723, 0.035810, 0.122497, 0.004955, -0.157844, 0.250351, -0.049327, -0.015627]
d5 = [1.000000, -1.079388, 0.171395, -0.608815, 0.289950, 0.345926, 0.489272, -0.486574, -0.102937, -0.169062, 0.228480]
d6 = [1.000000, -1.271303, 0.361462, -0.329435, 0.117882, 0.519108, -0.031825, -0.204961, -0.084625, -0.136233, 0.166813]
d7 = [1.000000, -1.163967, 0.289580, -0.257657, 0.070043, 0.322202, 0.152398, -0.299706, -0.135807, 0.113612, 0.046204]
d8 = [1.000000, -1.187368, 0.084485, -0.021361, 0.319335, 0.104394, -0.187529, -0.018591, 0.019784, -0.099684, 0.112729]
d9 = [1.000000, -1.301857, 0.346400, -0.079583, 0.035974, 0.233064, 0.265024, -0.396072, -0.149948, 0.162073, 0.030705]
d10 = [1.000000, -1.491165, 1.112715, -1.109563, 0.609890, 0.098264, 0.494265, -0.776494, 0.522789, -0.605250, 0.352131]
#d11 = [1.000000, -1.659533, 1.192649, -1.000001, 0.758808, -0.265996, 0.593881, -0.701499, 0.136216, 0.053461, -0.022305]
#d12 = [1.000000, -1.459538, 0.492459, -0.191430, 0.155797, 0.352374, -0.096918, -0.164331, -0.001138, -0.149602, 0.126875]
#d13 = [1.000000, -1.530610, 0.584461, -0.144901, 0.120586, 0.181776, 0.012406, -0.201678, 0.143236, -0.243943, 0.132315]

#d1 = [1.000000, -0.769520, -0.205243, 0.081467, 0.040715, -0.056768, -0.067566, 0.076396, 0.081476, -0.029001, 0.048731]
#d2 = [1.000000, -0.837748, 0.700524, -1.171762, 1.027939, -0.828224, 0.800109, -0.660064, 0.343198, -0.242548, 0.077302]
#d3 = [1.000000, -0.722733, -0.009317, -0.699606, 0.775576, -0.429987, 0.590779, -0.408129, 0.078419, -0.272489, 0.211826]
#d4 = [1.000000, -0.159034, -0.488723, -0.271481, 0.272122, 0.046731, -0.187670, -0.228514, 0.033239, 0.192279, 0.172673]
#d5 = [1.000000, -0.885101, 0.063342, -0.243077, -0.032695, 0.317324, -0.191493, 0.013162, 0.031463, -0.051631, 0.084225]
#d6 = [1.000000, -0.814681, -0.112794, -0.020966, -0.014332, 0.060157, -0.002434, 0.005457, 0.113817, -0.101544, -0.041309]
#d7 = [1.000000, -0.788957, -0.278621, 0.168907, 0.020595, -0.120422, -0.067526, -0.001587, 0.113179, -0.040490, 0.077750]
#d8 = [1.000000, -0.841309, -0.220982, 0.074802, 0.169386, -0.187497, 0.090005, 0.130844, 0.002080, -0.053302, -0.109211]
#d9 = [1.000000, -0.935898, 0.320656, -0.216442, -0.066983, -0.126962, 0.371127, -0.125915, -0.065524, 0.177248, -0.166454]
#d10 =  [1.000000, -0.714431, -0.026362, -0.092115, 0.013910, 0.087901, -0.042022, -0.139675, -0.015572, 0.237563, -0.096452]

DLEN = 40

h1 = [1.000000, -0.779707, 0.504787, -0.785524, 0.050571, -0.151718, 0.158857, -0.085374, 0.249418, -0.191304, 0.071106]
h2 = [1.000000, -1.081799, 1.036896, -1.360530, 0.844695, -0.589043, 0.626537, -0.469642, 0.330885, -0.260253, -0.000046]
h3 = [1.000000, -0.903685, 1.163893, -1.125233, 0.657474, -0.613687, 0.436382, -0.290029, 0.174464, -0.183318, -0.099564]
h4 = [1.000000, -0.429807, 0.495585, -0.539585, -0.313746, -0.002478, -0.083161, 0.010477, 0.096790, -0.086517, -0.044105]
h5 = [1.000000, -0.810410, 0.821055, -0.894704, 0.233496, -0.272129, 0.544120, -0.474008, 0.426551, -0.430439, 0.061281]
h6 = [1.000000, -0.719822, 0.697343, -1.005737, 0.563553, -0.475852, 0.727525, -0.336941, 0.164122, -0.377252, -0.016358]
h7 = [1.000000, -0.694536, 0.595167, -0.615902, 0.002083, -0.134543, 0.152418, -0.087053, 0.097620, -0.161511, -0.002503]
h8 = [1.000000, -1.302171, 1.404637, -1.387161, 0.814309, -0.494465, 0.477782, -0.220082, -0.038705, -0.104256, -0.014416]

HLEN = 40

hello = [
        (h1, 10, HLEN),  (h2, 10, HLEN),  (h3, 10, HLEN),  (h4, 10, HLEN), 
        (h5, 10, HLEN),  (h6, 10, HLEN),  (h7, 10, HLEN),  (h8, 10, HLEN), 
        (e, 100, 100), (ll, 500, 100), (oo, 300, 50), (u, 300, 300), (null, 500, 1), 
       # (w1, 10, WLEN), (w2, 10, WLEN), (w3, 10, WLEN), (w4, 10, WLEN), (w5, 10, WLEN), 
       # (w6, 10, WLEN), (w7, 10, WLEN), (w8, 10, WLEN), 
        (u, 200, 50),
        (er, 2000, 200), 
        #(rr, 500, 500), 
        (ll, 1000, 50), 
        (d1, DLEN, 1),  (d2, DLEN, 1),  (d3, DLEN, 1),  (d4, DLEN, 1), 
        (d5, DLEN, 1),  (d6, DLEN, 1),  (d7, DLEN, 1),  (d8, DLEN, 1), 
        (d9, DLEN, 1),  (d10, DLEN, 1),   
#        (u, 300, 50),
#        (rr, 500, 500),
        (u, 20, 20),
        (null, 500, 1),

#        (d5, 10, DLEN),  (d6, 10, DLEN),  (d7, 10, DLEN),  (d8, 10, DLEN), 
#        (d9, 10, DLEN),  (d10, 10, DLEN),  (d11, 10, DLEN),  (d12, 10, DLEN), 
#        (null, 10, 0),
        ]

count = 0

dsyn = []

delay = np.zeros(10)

taps = np.zeros(11)

for i in range(3):
    
    for (phoneme, length, interp) in hello:

        taps_lerp = (np.array(phoneme) - taps) / interp
    #    taps = phoneme

        for i in range(0, length + interp):

            if (i < interp):
                taps += taps_lerp
            
            pulse = 0

            if count == 67:
                pulse = 1.0
                count = 0
            
            count += 1
            
            if (taps[0] == 0.0):
                accu = 0
            else:
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
dsyn *= 32768 * 0.05

wavfile.write("hello?.wav", 6000, dsyn.astype(np.int16))
