import numpy as np
import sounddevice as sdd

def bbc(frequency=1000, mod_rate=5, noise_amplitude=0.2, duration=10, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    modulator = 1.0 + 0.5 * np.sin(2 * np.pi * mod_rate * t)
    modulated_wave = wave * modulator

    noise = noise_amplitude * np.random.normal(size=modulated_wave.shape)
    bc = modulated_wave + noise

    while True:
        sdd.play(bc, sample_rate)
        sdd.wait()

bbc()