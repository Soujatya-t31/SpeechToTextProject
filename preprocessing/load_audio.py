import librosa

audio, sample_rate = librosa.load(
    "recordings/hello.wav",
    sr = None
)

duration = len(audio)/sample_rate

print("Audio info for Comp (NumPy Array): ",audio)
print("Sample rate: ", sample_rate)
print("duration: ", duration)
print("audio shape (sample rate x time(duration): )", audio.shape)
