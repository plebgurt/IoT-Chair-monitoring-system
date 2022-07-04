from network import WLAN      # For operation of WiFi network
import time                   # Allows use of time.sleep() for delays
import pycom                  # Base library for Pycom devices
from mqtt import MQTTClient  # For use of MQTT protocol to talk to Adafruit IO
import ubinascii              # Needed to run any MicroPython code
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
import config                 # Imports config that contains user information
import connectiondata

def connect_wifi():
    global wlan
    pycom.heartbeat(False)
    time.sleep(0.1) # Workaround for a bug.
                    # Above line is not actioned if another
                    # process occurs immediately afterwards
    pycom.rgbled(0xff0000)  # Status red = not working
    pycom.wifi_mode_on_boot(WLAN.STA)   # choose station mode on boot
    wlan = WLAN() # get current object, without changing the mode
    # Set STA on soft rest
    if machine.reset_cause() != machine.SOFT_RESET:
        wlan.init(mode=WLAN.STA)        # Put modem on Station mode
    if not wlan.isconnected():          # Check if already connected
        print("Connecting to WiFi...")
        # Connect with your WiFi Credential
        wlan.connect(config.SSID, auth=(WLAN.WPA2, config.PASS))
        # Check if it is connected otherwise wait
        while not wlan.isconnected():
            pass
    print("Connected to Wifi")
    pycom.rgbled(0xffd7000) # Status orange: partially working
    time.sleep_ms(500)
    # Print the IP assigned by router
    print('network config:', wlan.ifconfig(id=0))

def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    print((topic, msg))

def connect_adafruit():
    global client
    AIO_SERVER = "io.adafruit.com"
    AIO_PORT = 1883
    AIO_USER = config.AIO_USER
    AIO_KEY = config.AIO_KEY
    AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything


    # Use the MQTT protocol to connect to Adafruit IO
    client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
    CLIENT = client
    # Subscribed messages will be delivered to this callback
    client.set_callback(sub_cb)
    client.connect()

    pycom.rgbled(0x00ff00) # Status green: online to Adafruit IO
    time.sleep(0.5)


connect_wifi()
connect_adafruit()
connectiondata.WLAN = wlan
connectiondata.CLIENT = client
