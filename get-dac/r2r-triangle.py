import time

import r2r_dac
import signal_generator as sg


amplitude = 3.2
signal_frequency = 5
sampling_frequency = 1000


try:

    dac = r2r_dac.R2R_DAC(
        [16, 20, 21, 25, 26, 17, 27, 22],
        3.2
    )

    start = time.time()

    while True:

        current_time = time.time() - start

        voltage = amplitude * sg.get_triangle_wave_amplitude(
            signal_frequency,
            current_time
        )

        dac.set_voltage(voltage)

        sg.wait_for_sampling_period(
            sampling_frequency
        )

finally:

    dac.deinit()