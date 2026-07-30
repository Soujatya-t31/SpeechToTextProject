# just for testing will delete soon

import librosa

audio, sr = librosa.load("recordings/Good_Morning.wav", sr=None, mono=False)
print("Sample Rate:", sr)
print("Shape:", audio.shape)