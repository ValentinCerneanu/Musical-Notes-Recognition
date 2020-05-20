import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
def mySine(A, f, theta0, t):
    x=A*np.sin(2*np.pi*f*t+theta0)
    return x
def myPlay(x,fs):
    sd.play(x,fs)
def plotInTime(x,fs):
    t=np.arange(0,np.size(x,0)/fs,1/fs)
    plt.plot(t,x)
    plt.grid(True)
def plotInFrequency(x,fs):
    N=int(np.size(x,0)/2)
    f=np.arange(0,fs/2,fs/2/N)
    x=np.abs(np.fft.fft(x[:,0]))
    x=x[:N]
    plt.plot(f,x)
    plt.grid(True)
def myDFT(x):
    N=np.size(x)
    X=np.zeros([N,1],dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k]+=x[n]*np.exp(-2j*np.pi*k*n/N)
    return(X)
def fadeIn(x,fs,dt):
    nSamples=dt*fs
    effect=np.linspace(0,1,nSamples)
    effect=np.stack((effect,effect),axis=0).T
    nTotal=len(x)
    if nSamples<nTotal:
        y=x[:nSamples]*effect
        y=np.concatenate((y,x[nSamples:,:]),axis=0)
    else:
        y=y*effect[:nTotal]
    return(y)
def myRamp(t,m,ad):
    N = len(t)
    y = np.zeros(N)
    for i in range(1,N):
        if t[i] >= -ad:
            y[i] = m*(t[i] + ad)
    return y
def find_pitch(audiofile):
    fs,x = wav.read(audiofile)
    ms20=int((fs/50))
    ms2=int(fs/500)

    x=[i/32767 for i in x]

    y=plt.acorr(x,maxlags=ms20,normed=True)

    y=y[1]
    z=y[round(len(y)/2):]
    z=z[ms2:ms20]
    zmax=max(z)

    index=np.where(z==zmax)
    index=index[0][0]

    pitch=fs/(ms2+index+2)

    return pitch