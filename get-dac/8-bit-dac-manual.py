import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setup(dac_bits, GPIO.OUT, initial=0)

dynamic_range = 3.3


def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Диапазон: 0 - {dynamic_range:.2f} В")
        return 0

    return int(voltage / dynamic_range * 255)


def number_to_dac(number):
    binary = [int(bit) for bit in f"{number:08b}"]
    GPIO.output(dac_bits, binary)


try:
    while True:
        try:
            voltage = float(input("Введите напряжение: "))

            number = voltage_to_number(voltage)

            number_to_dac(number)

            print(f"Число ЦАП: {number}")

        except ValueError:
            print("Ошибка ввода")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()