import numpy as np
import time

def get_sin_wave_amplitude(freq, t):
    #Возвращает нормализованную амплитуду синусоидального сигнала от 0 до 1

    raw_sin = np.sin(2 * np.pi * freq * t)
    normalized = (raw_sin + 1) / 2
    return normalized

def wait_for_sampling_period(sampling_frequency):
    #Ждет один период дискретизации
    
    time.sleep(1.0 / sampling_frequency)

