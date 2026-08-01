import os
import librosa
import soundfile as sf


audio, sr = librosa.load(
    "recordings/hello.wav",
    sr=None
)

trimmed_audio, _ = librosa.effects.trim(
    audio,
    top_db=40
)

os.makedirs(
    "outputs/trimmed",
    exist_ok=True
)

sf.write(
    "outputs/trimmed/hello_sample_trimmed.wav",
    trimmed_audio,
    sr
)

print("Silence Removed")