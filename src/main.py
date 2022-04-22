from scd30_i2c import SCD30
import RPi.GPIO as GPIO
import time

# variables
co2, temp, rh = 0, 0, 0

# initialise SCD30 sensor
scd30 = SCD30()

# configure settings for SCD30 sensor
scd30.set_measurement_interval(60)
scd30.start_periodic_measurement()
time.sleep(2)

# setup DC motor
GPIO.setmode(GPIO.BCM)
Motor1A = 24
Motor1B = 23
Motor1E = 25
GPIO.setup(Motor1A,GPIO.OUT)  # all pins as outputs
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)


def onMotor():
    # set up GPIO pins
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)

def offMotor():
    GPIO.output(Motor1E,GPIO.LOW)


if __name__ == '__main__':
    while True:
        if scd30.get_data_ready():
            m = scd30.read_measurement()
            if m is not None:
                co2, temp, rh = m[0], m[1], m[2]
                # create socket and send data to phoenix socket
                print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
            time.sleep(2)
        else:
            time.sleep(0.2)
        
        # if relative humidity level is less than 95%, turn on DC motor (i.e. automatic water spray)
        if rh < 95:
            onMotor()
        else:
            offMotor()