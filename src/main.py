import time
import RPi.GPIO as GPIO
import schedule

# Pins
moisture1_pin = 38
moisture2_pin = 40
dht11_pin = 28
lights_pin = 32
ldr_m_pin = 12
ldr_t_pin = 10
pump_pin = 8
water_level_pin = 36

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(lights_pin, GPIO.OUT)
GPIO.setup(moisture1_pin, GPIO.IN)
GPIO.setup(moisture2_pin, GPIO.IN)
GPIO.setup(pump_pin, GPIO.OUT)
GPIO.setup(water_level_pin, GPIO.IN)
lights = GPIO.PWM(lights_pin, 50)
lights.start(0)

# Ideal light levels at different times of the day
# Gathered from actual trials
ideal_light_levels = [0, 1, 2, 3, 4]


# Mapping values to get optimum brightness level of lights
def map_values(value, start1, stop1, start2, stop2):
    outgoing = start2 + (stop2 - start2) * \
        ((value - start1) / (stop1 - start1))
    return outgoing

# Check current light levels
# Code from https://www.instructables.com/id/Raspberry-Pi-GPIO-Circuits-Using-an-LDR-Analogue-S/


def check_light_level():
    cap = 0.000001
    adj = 2.130620985
    i = 0
    t = 0
    while (i < 10):
        GPIO.setup(ldr_m_pin, GPIO.OUT)
        GPIO.setup(ldr_t_pin, GPIO.OUT)
        GPIO.output(ldr_m_pin, False)
        GPIO.output(ldr_t_pin, False)
        time.sleep(0.2)
        GPIO.setup(ldr_m_pin, GPIO.IN)
        time.sleep(0.2)
        GPIO.output(ldr_t_pin, True)
        starttime = time.time()
        endtime = time.time()
        while (GPIO.input(ldr_m_pin) == GPIO.LOW):
            endtime = time.time()
        measureresistance = endtime-starttime

        res = (measureresistance/cap)*adj
        i = i+1
        t = t+res
    t = t/i
    return(t)

# Is water present for pumping?


def water_present():
    if(GPIO.input(water_level_pin)):
        return False
    else:
        return True

# Is the soil moist enough?


def check_moisture():
    m1 = GPIO.input(moisture1_pin)
    m2 = GPIO.input(moisture2_pin)
    if(m1 or m2):
        print("Low Water")
        return False
    else:
        print("Already wet")
        return True

# Pump water


def water():
    if(water_present()):
        print("Water present")
        pump_failure = 10
        while((check_moisture() == False) and (pump_failure > 0)):
            print("Filling")
            GPIO.output(pump_pin, True)
            pump_failure -= 1
            time.sleep(10)
            GPIO.output(pump_pin, False)
            time.sleep(.1)  # Slight delay to let current stabilise

        if(pump_failure == 0):
            print("Check pump")
    else:
        print("Check water level")

# Does the plant need more lights?


def lights(current_time):
    # Temporary code until ideal values are identified
    print("current time = ", current_time)
    print("light levels = ", check_light_level())


def lights_off():
    print("Lights off")
    lights.ChangeDutyCycle(0)


def lights_on(level):
    lights.ChangeDutyCycle(level)


def check_all():
    print("Light level = ", check_light_level())
    print("Moisture Sensor1 = ", GPIO.input(moisture1_pin))
    print("Moisture Sensor2 = ", GPIO.input(moisture2_pin))
    print("Moisture Sensor3 = ", GPIO.input(water_level_pin))
    lights_on(100)
    time.sleep(1)
    lights_off()
    GPIO.output(pump_pin, True)
    time.sleep(1)
    GPIO.output(pump_pin, False)


# Schedules
schedule.every().monday.at("11:00").do(water)
schedule.every().day.at("08:00").do(lights, current_time=0)
schedule.every().day.at("10:00").do(lights, current_time=1)
schedule.every().day.at("12:00").do(lights, current_time=2)
schedule.every().day.at("02:00").do(lights, current_time=3)
schedule.every().day.at("04:00").do(lights, current_time=4)
schedule.every().day.at("06:00").do(lights_off)


if __name__ == '__main__':
    while(True):
        # schedule.run_pending()
        check_all()

p.stop()
GPIO.cleanup()
