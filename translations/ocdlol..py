        # Load S2T model, move to device, and run inference
        s2t_model = torch.jit.load("unity_on_device_s2t.ptl").to(device)
        with torch.no_grad():
            text = s2t_model(audio_input.cpu(), tgt_lang=TGT_LANG)  # Explicitly moving to CPU
        print(f"S2T Model Output: {text}")
