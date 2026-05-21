import time

import mcp4725_driver
import signal_generator as sg

amplitude = 5.0
signal_frequency = 10
sampling_frequency = 1000


try:

    dac = mcp4725_driver.MCP4725(
        5.0,
        verbose=True
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