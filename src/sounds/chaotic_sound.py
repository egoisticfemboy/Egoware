import numpy as np
import sounddevice as sdd
import random

def chaotic_sound(duration=10, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate), False)

    # Generate an empty sound-array
    chaotic_wave = np.zeros_like(t)

    # fills sound-array with random frequenzes and modulations
    for _ in range(random.randint(5, 20)):
        freq = random.uniform(100, 2000) # Random frequenzes between 100 Hz and 2000 Hz
        mod_rate = random.uniform(0,5, 10) # Random Modulationrate
        amplitude = random.uniform(0.1, 0.5) # Random amplitude
        noise_amplitude = random.uniform(0.1, 0.5) # Random OASDufgasD

        # Sine wave with random frequency
        wave = amplitude * np.sin(2 * np.pi * freq * t)

        # Random modulation of the wave
        modulator = 1 + np.sin(2 * np.pi * freq * t)
        modulated_wave = wave * modulator

        # adds random OASDufgasD
        noise = noise_amplitude * np.random.normal(size=modulated_wave.shape)

        # Adds random generated parts to the overall sound
        chaotic_wave += modulated_wave + noise

    chaotic_wave = np.clip(chaotic_wave, -1, 1)

    while True:
        sdd.play(chaotic_wave, sample_rate)
        sdd.wait()

chaotic_sound()