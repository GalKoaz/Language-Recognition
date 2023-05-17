import os
import numpy as np
import librosa
import soundfile as sf
from pydub import AudioSegment
from concurrent.futures import ThreadPoolExecutor


def transform_audio(audio_data, sr, n_steps=None, noise_mean=0., noise_std=None, speed_rate=None):
    if n_steps is not None:
        audio_data = librosa.effects.pitch_shift(audio_data, sr=sr, n_steps=n_steps)
    if noise_std is not None:
        noise = np.random.normal(noise_mean, noise_std, audio_data.shape)
        audio_data = np.clip(audio_data + noise, -1., 1.)
    if speed_rate is not None:
        audio_data = librosa.effects.time_stretch(audio_data, rate=speed_rate)
    return audio_data


def convert_and_transform(file_path):
    # Convert to WAV
    sound = AudioSegment.from_mp3(file_path)
    fname_without_ext = os.path.splitext(file_path)[0]
    wav_path = f"{fname_without_ext}.wav"
    sound.export(wav_path, format="wav")
    os.remove(file_path)  # delete original file

    # Load WAV and transform audio
    audio_data, sr = librosa.load(wav_path, sr=None)
    audio_data_transformed = transform_audio(
        audio_data, sr, n_steps=0, noise_mean=0., noise_std=0.00, speed_rate=1
    )

    # Save the transformed audio to a new file
    sf.write(wav_path, audio_data_transformed, sr)
    return 1


def load():
    counter = 0
    rootDir = 'C:\\Users\\koazg\\Desktop\\same_size_lang'
    mp3_files = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        print(f'Found directory: {dirName}')
        for fname in fileList:
            if fname.endswith('.mp3'):
                mp3_files.append(os.path.join(dirName, fname))

    with ThreadPoolExecutor() as executor:
        results = executor.map(convert_and_transform, mp3_files)
        counter = sum(results)

    print('=============================')
    print(f'Total Data files loaded: {counter}')
    print('=============================')


if __name__ == '__main__':
    load()
