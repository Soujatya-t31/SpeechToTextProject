import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

#Load audio
audio, sr = librosa.load("recordings/Good_Morning.wav", sr = None)

#Create output directory
os.makedirs("outputs/spectrograms", exist_ok = True)

#Compute STFT
D = librosa.stft(audio)

#convert amplitude to decibels
S_db = librosa.amplitude_to_db(np.abs(D), ref = np.max)

plt.figure(figsize=(12,5))

librosa.display.specshow(
    S_db,
    sr = sr,
    x_axis = "time",
    y_axis = "hz"
)

plt.colorbar(label = "Intensity (dB)")
plt.title("Spectrogram")

plt.tight_layout()

plt.savefig("outputs/spectrograms/Good_Morning_spectrogram.png")

plt.show()