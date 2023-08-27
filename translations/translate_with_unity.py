import os
import torchaudio
import torch

torch.autograd.set_detect_anomaly(True)

def chunk_audio(audio, chunk_size):
    num_samples = audio.shape[1]
    num_chunks = num_samples // chunk_size
    chunks = [audio[:, i*chunk_size:(i+1)*chunk_size] for i in range(num_chunks)]
    return chunks

os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
torch.backends.cudnn.enabled = False


TEST_AUDIO_PATH = "chunks/chunk0.wav"
TGT_LANG = "hin"
OUTPUT_FOLDER = "output"
CHUNK_SIZE = 16000  # 1 second if sample rate is 16kHz

if not os.path.exists(TEST_AUDIO_PATH):
    print(f"Error: Audio file {TEST_AUDIO_PATH} does not exist.")
elif not os.path.exists("unity_on_device_s2t.ptl") or not os.path.exists("unity_on_device.ptl"):
    print("Error: Model files do not exist.")
elif not os.path.exists(OUTPUT_FOLDER):
    print(f"Error: Output folder {OUTPUT_FOLDER} does not exist.")
else:
    device = 'cpu'
    print(f"Running on {device}")

    try:
        audio_input, _ = torchaudio.load(TEST_AUDIO_PATH)
        print(f"Audio file successfully loaded. Shape: {audio_input.shape}")

        audio_chunks = chunk_audio(audio_input, CHUNK_SIZE)

        s2st_model = torch.jit.load("unity_on_device.ptl").to(device)
        
        output_texts = []
        output_waveforms = []
        with torch.no_grad():
            for audio_chunk in audio_chunks:
                
                print(f"Debug: Chunk shape: {audio_chunk.shape}, Chunk type: {audio_chunk.dtype}")  
                text, units, waveform = s2st_model(audio_chunk.to(device), tgt_lang=TGT_LANG)
                output_texts.append(text)
                output_waveforms.append(waveform)
                
        # Concatenate outputs if necessary
        final_text = ' '.join(output_texts)
        final_waveform = torch.cat(output_waveforms, dim=1)
        
        print(f"S2ST Model Output: {final_text}")

        torchaudio.save(f"{OUTPUT_FOLDER}/result.wav", final_waveform.unsqueeze(0), sample_rate=CHUNK_SIZE)
        print("Output waveform saved.")
    except Exception as e:
        print(f"An error occurred: {e}")


# ece-linlabsrv01.ece.gatech.edu