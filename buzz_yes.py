from time import sleep
from gpiozero import LED

buzz = LED (26)


 buzz.on ()
 sleep (0.3)
 buzz.off()
 sleep(.3)
