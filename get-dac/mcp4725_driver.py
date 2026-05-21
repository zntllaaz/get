import smbus


class MCP4725:

    def __init__(self,
                 dynamic_range,
                 address=0x61,
                 verbose=True):

        self.bus = smbus.SMBus(1)
        self.address = address
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        self.wm = 0x00
        self.pds = 0x00

    def deinit(self):
        self.bus.close()

    def set_number(self, number):

        if not (0 <= number <= 4095):
            print("Диапазон 0..4095")
            return

        first_byte = self.wm | self.pds | (number >> 8)
        second_byte = number & 0xFF

        self.bus.write_byte_data(
            self.address,
            first_byte,
            second_byte
        )

        if self.verbose:
            print(f"Число: {number}")

    def set_voltage(self, voltage):

        if not (0 <= voltage <= self.dynamic_range):
            print("Ошибка диапазона")
            return

        number = int(voltage / self.dynamic_range * 4095)

        self.set_number(number)


if __name__ == "__main__":

    try:

        dac = MCP4725(5.0)

        while True:

            voltage = float(input("Введите напряжение: "))
            dac.set_voltage(voltage)

    finally:
        dac.deinit()