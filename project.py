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


record_voice=sd.rec(int(duration * fs),samplerate=fs,channels=2)
sd.wait()       
write("sound_E4.wav",fs,record_voice)

# wave_data, samplerate=librosa.load('sound.wav')

# plt.subplot(211)
# plt.plot(wave_data) 
# plt.title('wave')
# pitches, magnitudes = librosa.piptrack(y=wave_data, sr=samplerate)
# plt.subplot(212)
# plt.imshow(pitches[:100, :], aspect="auto", interpolation="nearest", origin="bottom")
# plt.title('pitches')
y, sr = librosa.load('sound.wav')

# Set the hop length; at 22050 Hz, 512 samples ~= 23ms
hop_length = 512

# Separate harmonics and percussives into two waveforms
y_harmonic, y_percussive = librosa.effects.hpss(y)

# Beat track on the percussive signal
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,
                                             sr=sr)

# Compute MFCC features from the raw signal
mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)

# And the first-order differences (delta features)
mfcc_delta = librosa.feature.delta(mfcc)

# Stack and synchronize between beat events
# This time, we'll use the mean value (default) instead of median
beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]),
                                    beat_frames)

# Compute chroma features from the harmonic signal
chromagram = librosa.feature.chroma_cqt(y=y_harmonic,
                                        sr=sr)
plt.figure()
librosa.display.specshow(chromagram, y_axis='chroma', x_axis='time')
plt.title('chroma_cqt')
plt.colorbar()
plt.tight_layout()
plt.show()


# p = mydsp.find_pitch('sound.wav')
# print('pitch =', p)

# fs, x = wavfile.read('sound.wav')
# plt.close('all')
# plt.figure()
# mydsp.plotInTime(x,fs)
# plt.title('Original Signal')
# plt.figure()
# mydsp.plotInFrequency(x,fs)
# plt.title('Spectrum for the Original Signal')
# mydsp.myPlay(x,fs)

