import numpy as np
import sounddevice as sd
import time

def generate_alien_scream(duration=3, sample_rate=44100, volume_reduction=0.01):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    base_freq = 600  
    scream_wave = 0.5 * np.sin(2 * np.pi * base_freq * t)
    
    mod_freq = 4.0  
    modulation = 0.5 + 0.5 * np.sin(2 * np.pi * mod_freq * t)
    scream_wave *= modulation
    
    overtone1 = 0.3 * np.sin(2 * np.pi * (base_freq * 2) * t)
    overtone2 = 0.2 * np.sin(2 * np.pi * (base_freq * 3) * t)
    scream_wave += overtone1 + overtone2
    
    fade_in = np.linspace(0, 1, int(sample_rate * duration * 0.2))
    fade_out = np.linspace(1, 0, int(sample_rate * duration * 0.3))
    envelope = np.concatenate((fade_in, np.ones(len(t) - len(fade_in) - len(fade_out)), fade_out))
    scream_wave *= envelope
    
    delay = int(0.1 * sample_rate)  
    echo_wave = np.pad(scream_wave, (delay, 0))[:len(t)] * 0.5
    reverb_wave = np.pad(scream_wave, (2 * delay, 0))[:len(t)] * 0.3
    
    final_scream = scream_wave + echo_wave + reverb_wave
    final_scream = np.clip(final_scream, -1, 1)
    
    
    final_scream *= volume_reduction
    
    return final_scream

def three_min():
    sample_rate = 44100
    scream_duration = 3  
    scream_wave = generate_alien_scream(scream_duration, sample_rate)
    
    while True:
        sd.play(scream_wave, sample_rate)
        sd.wait()
        time.sleep(180)

three_min()
