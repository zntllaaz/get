import numpy as np
import time


def get_sin_wave_amplitude(freq, current_time):

    return (np.sin(2 * np.pi * freq * current_time) + 1) / 2


def get_triangle_wave_amplitude(freq, current_time):

    period = 1 / freq
    phase = (current_time % period) / period

    if phase < 0.5:
        return phase * 2

    return 2 - phase * 2


def wait_for_sampling_period(sampling_frequency):

    time.sleep(1 / sampling_frequency)