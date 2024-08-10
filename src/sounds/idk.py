import numpy as np
import sounddevice as sdd

def idk(frequency=100, mod_rate=100, noise_amplitude=0.3, duration=5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(3 * np.pi * frequency * t)

    modulator = 1.2 + 1 * np.sin(3.3 * np.pi * mod_rate * t)
    modulated_wave = wave * modulator

    noise = noise_amplitude * np.random.normal(size=modulated_wave.shape)
    bc = modulated_wave + noise + 0.01

    while True:
        sdd.play(bc, sample_rate)
        sdd.wait()

idk()