import time                   # Allows use of time.sleep() for delays
import pycom                  # Base library for Pycom devices
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
import config                 # The users stored data for connection to WIFI and Adafruit
import connectiondata         # Saves WLAN and Client generated in boot.py
from network import WLAN      # For operation of WiFi network
from pycoproc_2 import Pycoproc # Needed for getting access to accelerometer on the pysense board
from LIS2HH12 import LIS2HH12   # Libary for the accelerometer
from machine import Pin         # Imports the use of pins

halleffect = Pin('P15', mode=Pin.IN)
py = Pycoproc()
acc = LIS2HH12(py)

send_data_intervalls = 60 # seconds
time_dictionary = {'start_time_upright' : 0, 'start_time_reclined' : 0, 'total_time_upright' : 0, 'total_time_reclined' : 0, 'end_time' : 0, 'total_time' : 0}
is_sitting = False;
reminder_sent_dictionary = {0: False, 1 : False, 2 : False, 3 : False, 4 : False, 5 : False, 6 : False}

def check_is_chair_reclined():
    print("Pitch: " + str(acc.pitch()))
    send_data(config.AIO_ANGLE, acc.pitch())
    if acc.pitch() < -40 or acc.pitch() > 40:
        return True
    else:
        return False

def time_convert_min(sec):
    min = sec // 60
    hour = min // 60
    dispMin = min % 60
    return dispMin

def time_convert_hour(sec):
    min = sec // 60
    hour = min // 60
    dispHour = hour % 60
    return dispHour

def send_data(inc_topic, value):
    try:
        connectiondata.CLIENT.publish(topic = inc_topic, msg=str(value))
        print('SENT: {}, {}'.format(inc_topic, value))
    except Exception as e:
        print('FAILED: {}, {}'.format(inc_topic, value))

def send_reminder(time):
    if reminder_sent_dictionary.get(time) == False:
        send_data(config.AIO_SEND_REMINDER, time)
        reminder_sent_dictionary[time] = True

def reset_data():
    global is_sitting
    if is_sitting == True:
        print("I am here in reset")
        for key in time_dictionary.keys():
            time_dictionary[str(key)] = 0

        send_data(config.AIO_RECLINED_TIME, time_convert_min(time_dictionary['total_time_reclined']))
        send_data(config.AIO_UPRIGHT_TIME, time_convert_min(time_dictionary['total_time_upright']))
        is_sitting = False

    pycom.rgbled(0xFF0000)

try:                      # Code between try: and finally: may cause an error
                          # so ensure the client disconnects the server if
                          # that happens.
    while 1:              # Repeat this loop forever

            hall_sensor = halleffect()
            send_data(config.AIO_CURRENTLY_SITTING, hall_sensor)

            if hall_sensor == 0:

                if is_sitting == False:
                    is_sitting = True
                time_dictionary['end_time'] = time.time()
                is_chair_reclined = check_is_chair_reclined()

                if is_chair_reclined == True:
                    time_dictionary['start_time_upright'] == 0
                    if time_dictionary['start_time_reclined'] == 0:
                        time_dictionary['start_time_reclined'] = time.time()
                    current_time = time_dictionary['end_time'] - time_dictionary['start_time_reclined']
                    time_dictionary['total_time_reclined'] =  current_time
                    send_data(config.AIO_RECLINED_TIME, time_convert_min(time_dictionary['total_time_reclined']))
                    pycom.rgbled(0xFFFF00)

                else:
                    time_dictionary['start_time_reclined'] == 0
                    if time_dictionary['start_time_upright'] == 0:
                        time_dictionary['start_time_upright'] = time.time()
                    current_time = time_dictionary['end_time'] - time_dictionary['start_time_upright']
                    time_dictionary['total_time_upright'] = current_time
                    send_data(config.AIO_UPRIGHT_TIME, time_convert_min(time_dictionary['total_time_upright']))
                    pycom.rgbled(0x00FF00)

            else:
                reset_data()

            time_dictionary['total_time'] = time_dictionary['total_time_upright'] + time_dictionary['total_time_reclined']
            send_reminder(time_convert_hour(time_dictionary['total_time']))
            send_data(config.AIO_TOTAL_SITTING_TIME, (time_convert_hour(time_dictionary['total_time']) + (time_convert_min(time_dictionary['total_time']) / 60)))


            time.sleep(send_data_intervalls)

finally:                                 # If an exception is thrown ...
    connectiondata.CLIENT.disconnect()   # ... disconnect the client and clean up.
    connectiondata.CLIENT = None
    connectiondata.WLAN.disconnect()
    connectiondata.WLAN = None
    pycom.rgbled(0x000022)  # Status blue: stopped
    print("Disconnected from Adafruit IO.")
