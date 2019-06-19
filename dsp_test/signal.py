import math
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, rfft, irfft

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
# Bit reverce
def bit_reverce(value,rez):
    ret_v = 0
    for i in range(0, rez):
        ret_v |= ( value & 1 ) << (rez - i - 1)
        value >>= 1
    return ret_v
def signal(index,rez,n,freq1,freq2,line_):
    ret_signal = 0
    step_freq = ( freq2 - freq1 ) / n
    freq = freq1
    for i in range(0, n):
        ret_signal += line_[i] * math.cos(2 * math.pi * index * freq / rez )
        freq += step_freq
    return ret_signal
# settings
M = 511
fs = 20000
fc = 1000
fc_ = fc / fs

K = []

s_l =4096

N = 11
A = 100

line = [0.1 * A, 0.3 * A, 0.5 * A, 0.6 * A, 0.8 * A, 0.99 * A, 0.8 * A, 0.6 * A, 0.5 * A, 0.3 * A, 0.1 * A]

rand_signal = []
filtred_signal = []
# create random signal
for i in range(0, s_l):
    rand_signal.append( random.randrange(-20,20,1) + signal(i,s_l,N,500,600,line) + 100 * math.cos(2 * math.pi * i * 150/s_l) + 50 * math.cos(2 * math.pi * i * 110/s_l) + 50 * math.cos(2 * math.pi * i * 190/s_l) + 20 * math.cos(2 * math.pi * i * 1000/s_l) )

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
for i in range(0,len(rand_signal)):
    for j in range(len(K)):
        sum += 0 if ( (i-j) < 0 ) else K[j]*rand_signal[i-j]
    filtred_signal.append(sum)
    sum = 0

achx = []
print(len(K))
for i in range(0, 128):
    achx_new = ( 0 if (bit_reverce((i * 2) + 0,8)>M) else - K[bit_reverce((i * 2) + 0,8)] ) + ( 0 if (bit_reverce((i * 2) + 1,8)>M) else ( + K[bit_reverce((i * 2) + 1,8)] ) )
    achx.append(achx_new)

rand_signal_fft = fft(rand_signal)
filtred_signal_fft = fft(filtred_signal)
achx_ = rfft(K)

# working with plot
y=np.array(K)
filtred_signal_np=np.array(filtred_signal)
rand_signal_np=np.array(rand_signal)
rand_signal_fft_np=np.array(rand_signal_fft[0:s_l>>1].real/s_l)
filtred_signal_fft_np=np.array(filtred_signal_fft[0:s_l>>1].real/s_l)
#K_np=np.array(K)
achx_=np.array(achx_)
#plt.plot(filtred_signal_np)
#plt.plot(rand_signal_np)
#plt.plot(K_np)
plt.plot(filtred_signal_fft_np)
plt.plot(rand_signal_fft_np)
#plt.plot(achx_.real)

plt.show()