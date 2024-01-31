#!/usr/bin/env python

from ina219 import INA219
from ina219 import DeviceRangeError
from subprocess import run
from time import sleep
#from gpiozero import LED


SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 0.8

def read():
    ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
    ina.configure(ina.RANGE_16V)
    ina.wake()
    sleep(1)
    voltage = ina.voltage()+0.1
    print("Battery_Voltage: %.3f V" % voltage)
    try:
        print("Discharge_ Current: %.3f mA" % ina.current())
        bat = (voltage - 2.8) / (4.1 - 2.8) * 100
        if(bat > 100):bat = 100
        if(bat < 0):bat = 0
        print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
        print("battery_percent: %d " % bat)

        ina.sleep()

    except DeviceRangeError as e:
        # Current out of device range with specified shunt resistor
     print(e)

if __name__ == "__main__":
    read()
