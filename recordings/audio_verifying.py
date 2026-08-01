# just for testing will delete soon

import librosa

audio, sr = librosa.load("outputs/preprocessed/Soujatya_Taluker_processed.wav", sr=None, mono=False)
print("Sample Rate:", sr)
print("Shape:", audio.shape)