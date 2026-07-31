import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


# Load audio
audio, sr = librosa.load(
    "recordings/Good_Morning.wav",
    sr=None
)


# Create output folder
os.makedirs(
    "outputs/mel",
    exist_ok=True
)


# Generate Mel Spectrogram
mel_spec = librosa.feature.melspectrogram(
    y=audio,
    sr=sr,
    n_mels=128,
    fmax=8000
)


# Convert power to decibels
mel_db = librosa.power_to_db(
    mel_spec,
    ref=np.max
)


# Create figure
plt.figure(figsize=(12,5))


# Display Mel Spectrogram
librosa.display.specshow(
    mel_db,
    sr=sr,
    x_axis="time",
    y_axis="mel"
)


# Color bar
plt.colorbar(
    label="Intensity (dB)"
)


plt.title(
    "Mel Spectrogram"
)


plt.tight_layout()


# Save output
plt.savefig(
    "outputs/mel/mel_spectrogram.png"
)


plt.show()