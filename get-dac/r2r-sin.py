import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, verbose=False)
    
    t = 0
    while True:
        norm_amp = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = norm_amp * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t += 1.0 / sampling_frequency
        
#except KeyboardInterrupt:
    #pass

finally:
    dac.deinit()


