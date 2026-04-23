import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

bits = [22, 27, 17, 26, 25 ,21, 20, 16]
GPIO.setup(bits, GPIO.OUT)
GPIO.output(bits, 0)

dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за пределы ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    
    return int(voltage / dynamic_range * 255) 

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def number2dac(number):
    dac = dec2bin(number)
    GPIO.output(bits, dac)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number2dac(number)

        except ValueError:
            print("Вы ввели не число! Попробуйте еще раз!")

finally:
    GPIO.output(bits, 0)
    GPIO.cleanup()
