import numpy as np
import sounddevice as sdd
import time

def beepenis(frequency=1000, duration=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = duration * np.sin(2 * np.pi * frequency * t)
    sdd.play(wave, sample_rate)
    sdd.wait

while True:
    beepenis()
    time.sleep(60)