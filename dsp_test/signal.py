import math
import random
import matplotlib.pyplot as plt
import numpy as np

# sinx/x
def K_i(index, fc, M):
    if(index == M/2):
        return 2 * math.pi * fc
    else:
        return math.sin(2 * math.pi * fc * (index - M / 2) )/(index - M / 2)
# Hamming window
def Hamm(index):
    return 0.54 - 0.46 * math.cos(2 * math.pi * index / M)
# Blackman window
def Black(index):
    return 0.42 - 0.5 * math.cos(2 * math.pi * index / M) + 0.08 * math.cos(4 * math.pi * index / M)
# settings
M = 150
fs = 20000
fc = 1000
fc_ = fc / fs

K = []

rand_signal = []
filtred_signal = []
# create random signal
for i in range(0, 5000):
    rand_signal.append( random.randrange(-20,20,1) + 100 * math.cos(2 * math.pi * i * 150/5000) + 20 * math.cos(2 * math.pi * i * 1000/5000) )

BW = 4/M
print(str("Bandwidth = {:f}".format(BW)))
print(str("fc = {:f}".format(fc_)))

Norm = 0
for i in range(0,M+1):
    k_new = K_i(i,fc_,M)*Hamm(i)
    Norm = k_new if (k_new > Norm) else Norm
    K.append(k_new)

for i in range(0, len(K)):
    K[i] = K[i] / Norm
# finding filtred signal
sum = 0
for i in range(len(K), len(rand_signal)):
    for j in range(len(K)):
        sum += K[j]*rand_signal[i-j]
    filtred_signal.append(sum/10)
    sum = 0

# working with plot
y=np.array(K)
filtred_signal_np=np.array(filtred_signal)
rand_signal_np=np.array(rand_signal)
plt.plot(filtred_signal_np)
plt.plot(rand_signal_np)

plt.show()