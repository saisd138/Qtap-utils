from ina219 import INA219
import time

# Set the I2C address
ina_address = 0x40

# Shunt resistance in ohms (adjust this based on your hardware)
shunt_ohms = 0.1

# Create an INA219 instance with the specified I2C address and shunt resistance
ina = INA219(shunt_ohms, address=ina_address)

# Retry the configuration up to 3 times
for _ in range(3):
    try:
        # Configure INA219 to use the 16V shunt voltage range
        ina.configure(voltage_range=ina.RANGE_16V)
        break  # If successful, exit the loop
    except OSError as e:
        print(f"I2C communication error: {e}")
        time.sleep(1)  # Wait for 1 second before retrying

def get_battery_info():
    # Wake up the INA219
    ina.wake()

    # Wait for 1 second
    time.sleep(1)

    # Read the voltage from the INA219 sensor
    voltage = ina.voltage()+0.15

    # Read the current from the INA219 sensor
    current = ina.current()  # This value is in Amperes

    # Define the minimum and maximum voltage for the battery
    min_voltage = 3.0
    max_voltage = 4.1
    #for 2s battery config
    # min_voltage = 6
    # max_voltage = 8.2

    # Calculate the battery percentage
    battery_percentage = ((voltage - min_voltage) / (max_voltage - min_voltage)) * 100
    if(battery_percentage > 100):battery_percentage = 100
    if(battery_percentage < 0):battery_percentage = 0
    # Put the INA219 to sleep
    ina.sleep()

    return voltage, current, battery_percentage

# Get voltage, current, and battery percentage
voltage, current, battery_percentage = get_battery_info()

# Print the results
print(f"Voltage: {voltage:.2f}V")
print(f"Current: {current:.2f}A")
print(f"Battery Percentage: {battery_percentage:.2f}%")
