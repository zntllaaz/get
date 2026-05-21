import RPi.GPIO as GPIO


class PWM_DAC:

    def __init__(self,
                 gpio_pin,
                 pwm_frequency,
                 dynamic_range,
                 verbose=False):

        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, pwm_frequency)
        self.pwm.start(0)

    def deinit(self):

        self.pwm.stop()
        GPIO.cleanup()

    def set_voltage(self, voltage):

        if not (0 <= voltage <= self.dynamic_range):
            print("Ошибка диапазона")
            return

        duty = voltage / self.dynamic_range * 100

        self.pwm.ChangeDutyCycle(duty)

        if self.verbose:
            print(f"Напряжение: {voltage:.2f} В")


if __name__ == "__main__":

    try:

        dac = PWM_DAC(12, 500, 3.290, True)

        while True:

            voltage = float(input("Введите напряжение: "))

            dac.set_voltage(voltage)

    finally:
        dac.deinit()