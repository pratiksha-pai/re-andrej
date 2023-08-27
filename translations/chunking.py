# !pip install fairseq2==0.1 pydub yt-dlp
# !git clone https://github.com/facebookresearch/seamless_communication.git
# %cd seamless_communication
# !git checkout 01c1042841f9bce66902eb2c7512dbdd71d42112 # We will use a stable version; if you want to use the latest version, comment out this line.
# !pip install .


from seamless_communication.models.inference import Translator
from IPython.display import Audio
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub import AudioSegment
import torchaudio
import torch
import os

def save_and_play_audio(path_save, audio, sample_rate):
    torchaudio.save(
        path_save,
        audio[0].cpu(),
        sample_rate=sample_rate,
    )

    audio_play = Audio(path_save, rate=sample_rate, autoplay=True, normalize=True)
    display(audio_play)

def split_audio_with_max_duration(input_file, output_directory, min_silence_len=2500, silence_thresh=-60, max_chunk_duration=15000):

    sound = AudioSegment.from_wav(input_file)

    # Splitting on silence
    audio_chunks = split_on_silence(sound, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    # split for max_chunk_duration
    final_audio_chunks = []
    for chunk in audio_chunks:
        if len(chunk) > max_chunk_duration:
            num_subchunks = len(chunk) // max_chunk_duration + 1
            subchunk_size = len(chunk) // num_subchunks
            for i in range(num_subchunks):
                start_idx = i * subchunk_size
                end_idx = (i + 1) * subchunk_size
                subchunk = chunk[start_idx:end_idx]
                final_audio_chunks.append(subchunk)
        else:
            final_audio_chunks.append(chunk)

    # Export wav
    for i, chunk in enumerate(final_audio_chunks):
        output_file = f"{output_directory}/chunk{i}.wav"
        print("Exporting file", output_file)
        chunk.export(output_file, format="wav")


input_audio_file = "andrej_english.wav"
output_directory = "output"

split_audio_with_max_duration(input_audio_file, output_directory)

