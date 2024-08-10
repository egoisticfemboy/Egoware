import numpy as np
import sounddevice as sd
import random

def creepy_sound(duration=30, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    
    freq1 = random.uniform(30, 50)  
    wave1 = 0.5 * np.sin(2 * np.pi * freq1 * t)
    
    
    freq2 = random.uniform(200, 400)  
    mod_rate = random.uniform(0.1, 0.5)  
    modulator = 1 + 0.5 * np.sin(2 * np.pi * mod_rate * t)
    wave2 = 0.3 * np.sin(2 * np.pi * freq2 * t) * modulator
    
    
    noise_amplitude = 0.1
    noise = noise_amplitude * np.random.normal(size=t.shape)
    
    
    for _ in range(random.randint(1, 3)):
        freq3 = random.uniform(500, 800)
        wave3 = 0.2 * np.sin(2 * np.pi * freq3 * t)
        wave2 += wave3 * np.sin(2 * np.pi * random.uniform(0.1, 1) * t)

    
    creepy_wave = wave1 + wave2 + noise
    creepy_wave = np.clip(creepy_wave, -1, 1)
    
    
    while True:
        sd.play(creepy_wave, sample_rate)
        sd.wait()


creepy_sound()
