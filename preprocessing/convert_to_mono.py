import os
import librosa
import soundfile as sf

audio, sr = librosa.load(
    "recordings/hello.wav",
    sr=None,
    mono=True
)

os.makedirs(
    "outputs/mono",
    exist_ok=True
)

sf.write(
    "outputs/mono/hello_mono.wav",
    audio,
    sr
)

print("Converted to Mono")

