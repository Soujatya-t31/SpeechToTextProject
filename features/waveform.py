import os
import librosa
import matplotlib.pyplot as plt
import numpy as np

# load audio
audio, sr = librosa.load("recordings/Good_Morning.wav", sr = None)

# create output directory if it doesn't exist
os.makedirs("outputs/waveforms", exist_ok = True)

# Time values
time = np.arange(len(audio)) / sr 

plt.figure(figsize=(12, 4))
plt.plot(time, audio)

plt.title("Waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.tight_layout()

plt.savefig("outputs/waveforms/sample_waveform.png")
plt.show()