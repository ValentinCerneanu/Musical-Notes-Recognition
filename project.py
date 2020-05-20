import sounddevice as sd
from scipy.io.wavfile import write
import pitch
import librosa
import librosa.display
from scipy.io import wavfile
# import scipy.signal as sp
import numpy as np
import matplotlib.pyplot as plt
# import time
import mydsp

fs=44100
duration=4
print("recording...............")

# record input sound from microphone
record_voice=sd.rec(int(duration * fs),samplerate=fs,channels=2)
sd.wait()       
write("sound_test_440.wav",fs,record_voice)

y, sr = librosa.load('sound_test_440.wav')

# Separate harmonics and percussives into two waveforms
y_harmonic, y_percussive = librosa.effects.hpss(y)

# Compute chroma features from the harmonic signal
chromagram = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)
print(chromagram)
plt.figure()

librosa.display.specshow(chromagram, y_axis='chroma', x_axis='time')

plt.title('chroma_cqt')
plt.colorbar()
plt.tight_layout()
plt.show()

