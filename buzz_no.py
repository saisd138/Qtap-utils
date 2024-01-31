from gpiozero import Buzzer
from time import sleep

# Assuming the buzzer is connected to GPIO pin 26
buzzer_pin = 26
buzzer = Buzzer(buzzer_pin)

try:
    for _ in range(5):  # Beep thrice
        buzzer.on()      # Turn the buzzer on
        sleep(0.3)       # On delay of 0.5 seconds
        buzzer.off()     # Turn the buzzer off
        sleep(0.1)       # Off delay of 0.2 seconds
except KeyboardInterrupt:
    pass  # Handle keyboard interrupt if needed
