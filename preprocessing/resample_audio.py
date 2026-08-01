import os
import librosa
import soundfile as sf


audio, sr = librosa.load(
    "recordings/hello.wav",
    sr=16000
)

os.makedirs(
    "outputs/resampled",
    exist_ok=True
)

sf.write(
    "outputs/resampled/hello_sample_16k.wav",
    audio,
    16000
)

print("Resampled Successfully")