import torchaudio
import torch

TEST_AUDIO_PATH = "andrej_english.wav"
TGT_LANG = "hin"
OUTPUT_FOLDER = "output"


audio_input, _ = torchaudio.load(TEST_AUDIO_PATH) # Load waveform using torchaudio

s2t_model = torch.jit.load("unity_on_device_s2t.ptl") # Load exported S2T model
with torch.no_grad():
    text = s2t_model(audio_input, tgt_lang=TGT_LANG) # Forward call with tgt_lang specified for ASR or S2TT
print(text) # Show text output 

s2st_model = torch.jit.load("unity_on_device.ptl")
with torch.no_grad():
    text, units, waveform = s2st_model(audio_input, tgt_lang=TGT_LANG) # S2ST model also returns waveform
print(text)
torchaudio.save(f"{OUTPUT_FOLDER}/result.wav", waveform.unsqueeze(0), sample_rate=16000) # Save output waveform to local file