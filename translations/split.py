# splitting into chunks so its manageable 
#!pip install pydub
from pydub import AudioSegment

def split_wav(file_name):
    audio = AudioSegment.from_wav(file_name)
    length_audio = len(audio)
    half_an_hour = 1 * 60 * 1000 # 30 minutes in milliseconds

    for i in range(0, length_audio, half_an_hour):
        split_audio = audio[i:i+half_an_hour]
        split_file_name = file_name.split('.')[0] + '_' + str(i//half_an_hour) + '.wav'
        split_audio.export(split_file_name, format="wav")
        print(f"Part {i//half_an_hour} has been created")

file_name = 'andrej_english.wav'
split_wav(file_name)
