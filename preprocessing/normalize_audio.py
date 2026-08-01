import os
import librosa
import soundfile as sf
import numpy as np


audio, sr = librosa.load(
    "recordings/hello.wav",
    sr=None
)

audio = audio / np.max(np.abs(audio))

os.makedirs(
    "outputs/normalized",
    exist_ok=True
)

sf.write(
    "outputs/normalized/hello_sample_normalized.wav",
    audio,
    sr
)

print("Normalization Complete")