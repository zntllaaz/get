import time

import pwm_dac
import signal_generator as sg


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


try:

    dac = pwm_dac.PWM_DAC(
        12,
        500,
        3.29,
        True
    )

    start = time.time()

    while True:

        current_time = time.time() - start
        voltage = amplitude * sg.get_sin_wave_amplitude(
            signal_frequency,
            current_time
        )

        dac.set_voltage(voltage)

        sg.wait_for_sampling_period(
            sampling_frequency
        )

finally:

    dac.deinit()