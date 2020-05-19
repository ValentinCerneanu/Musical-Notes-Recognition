import sounddevice as sd
from scipy.io.wavfile import write

from scipy.io import wavfile
import scipy.signal as sp
import numpy as np
import matplotlib.pyplot as plt
import time
import mydsp

fs=44100
duration=4
print("recording...............")


record_voice=sd.rec(int(duration * fs),samplerate=fs,channels=2)
sd.wait()       
write("sound.wav",fs,record_voice)

fs, x = wavfile.read('sound.wav')
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.close('all')
mydsp.plotInTime(x,fs)
plt.title('Original Signal')
mydsp.plotInFrequency(x,fs)
plt.title('Spectrum for the Original Signal')


