import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):

        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):

        if not isinstance(number, int):
            print("Нужно целое число")
            return

        if not (0 <= number <= 255):
            print("Диапазон 0..255")
            return

        binary = [int(bit) for bit in f"{number:08b}"]

        GPIO.output(self.gpio_bits, binary)

        if self.verbose:
            print(f"Число: {number}")

    def set_voltage(self, voltage):

        if not (0 <= voltage <= self.dynamic_range):
            print("Напряжение вне диапазона")
            return

        number = int(voltage / self.dynamic_range * 255)

        self.set_number(number)

        if self.verbose:
            print(f"Напряжение: {voltage:.2f} В")


if __name__ == "__main__":

    try:
        dac = R2R_DAC(
            [16, 20, 21, 25, 26, 17, 27, 22],
            3.183,
            True
        )

        while True:

            voltage = float(input("Введите напряжение: "))

            dac.set_voltage(voltage)

    finally:
        dac.deinit()