import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import librosa.display
import matplotlib.pyplot as plt
fs=44100
duration=4
print("recording...............")

# record input sound from microphone
record_voice=sd.rec(int(duration * fs),samplerate=fs,channels=2)
sd.wait()       
write("sound_test_440.wav",fs,record_voice)

y, sr = librosa.load('sound_E4.wav')

# Separate harmonics and percussives into two waveforms
y_harmonic, y_percussive = librosa.effects.hpss(y)

# Compute chroma features from the harmonic signal
chromagram = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)

plt.figure()

librosa.display.specshow(chromagram, y_axis='chroma', x_axis='time')

plt.title('chroma_cqt')
plt.colorbar()
plt.tight_layout()
plt.show()

columns = int(chromagram.size/12)

#for j in range(columns):
#    for i in range(12):
#        print("{:.2f}".format(chromagram[i][j]), end =" ")
#    print()
    
freqOfNotes = [None] * 12

for i in range(12):
    cnt = 0;
    for j in range(columns):
        if chromagram[i][j] == 1:
            cnt = cnt + 1
    freqOfNotes[i] = cnt;
    
length = len(freqOfNotes)     
maxFreq = 0
for i in range(length):
    if freqOfNotes[i] > maxFreq:
        maxFreq = freqOfNotes[i]
        maxFreqIndex = i;

print(freqOfNotes)
print(maxFreqIndex)

switcher = {
        0: "C",
        1: "C#",
        2: "D",
        3: "D#",
        4: "E",
        5: "F",
        6: "F#",
        7: "G",
        8: "G#",
        9: "A",
        10: "A#",
        11: "B"
    }

print("Musical note recognized is: ", switcher.get(maxFreqIndex, "Invalid note"))

