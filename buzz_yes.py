from gpiozero import Buzzer
from time import sleep

# Assuming the buzzer is connected to GPIO pin 26
buzzer_pin = 26
buzzer = Buzzer(buzzer_pin)

try:
    buzzer.on()  # Turn the buzzer on
    sleep(0.1)     # Beep for 1 second (adjust the duration as needed)
finally:
    buzzer.off()
