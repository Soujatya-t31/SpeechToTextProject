import os
import librosa
import soundfile as sf
import numpy as np


audio, sr = librosa.load(
    "recordings/Soujatya_Talukder.wav",
    sr=16000,
    mono=True
)

audio, _ = librosa.effects.trim(audio)

audio = audio / np.max(np.abs(audio))

os.makedirs(
    "outputs/preprocessed",
    exist_ok=True
)

sf.write(
    "outputs/preprocessed/Soujatya_Taluker_processed.wav",
    audio,
    sr
)

print("Preprocessing Complete")