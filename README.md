# Tutorial: chair monitoring system
> ##### By Max Halling (mh226ef)
###### tags: `FiPy` `WiFi`


## Introduction


This project aims to build a system that can monitor how you sit in an office chair, this includes the angle you are sitting in, for how long and notifies you when you have been spending a set amount of time in said chair. This is achieved by using two different sensors, one hall effect sensor to know when you are sitting in the chair. And one accelerometer to measure the angle you are currently sitting in. The database that is used for this project is Adafruit IO, this has the possibility to make a dashboard with the information required and can use webhooks to notify you. The system uses Wi-Fi to be able to connect to the service we are using.

The project might take 3 hours to complete depending on experience.


## Objective

Like most people currently I spend a lot of time in my chair in front of a computer, and I quite often do so for extended periods of time. Often for school, other times it’s because I am playing or watching something at the computer. So, what I wanted to achieve in this course was to build a monitoring system that can see how I sit, for how long and in some form notify me when I have sat for a longer period. 

This project was designed to remind me to get up from my chair, get a glass of water, take a walk or since I am fortunate enough to have a standing desk remind me to use it more often. Since we often sit by a computer at a desk for work, school etc I thought this might be useful to gain insight into your sitting habits. Especially since sitting down for extended periods of time isn’t really optimal for your health.

I hope to gain insight for how long I sit, how I sit and hopefully change for how long I sit in a chair without moving.


## Material


| Item              | Link                    |Price|
| ----------------- |----------------------- |-------|
| Pysense 2.0 X      | [Pycom](https://pycom.io/product/pysense-2-0-x/)   |€29.65
| FiPy               | [Pycom](https://pycom.io/product/fipy/)     |€65.40
| Breadboard         | [Kjell](https://www.kjell.com/se/produkter/el-verktyg/elektronik/elektroniklabb/luxorparts-kopplingsdack-170-anslutningar-3-pack-p36282)    |€7,50
| Hall effect sensor (TLV49645)       | [Electrokit](https://www.electrokit.com/produkt/tlv49645-sip-3-hall-effektsensor-digital/)    | €1.7
| Magnet  | [Electrokit](https://www.electrokit.com/produkt/magnet-neo35-o8mm-x-4mm/) | €2.4
|Jumper cables male-male x10|[Electrokit](https://www.electrokit.com/produkt/labbsladd-20-pin-15cm-hane-hane/)|€2.7
|Jumper cables male-female x3|[Electrokit](https://www.electrokit.com/produkt/labbsladd-40-pin-30cm-hona-hane/)|€9.2
|10K Ω resistor|Anywhere|Cheap
|  | | **Total**   |
| || **€118.55**|

For this project I have used a Hall effect sensor, this is to measure the magnetic field. This is used to know when the person is sitting in the chair, this is done by placing the magnet on the piston of the office chair with the hall effect sensor out of reach when no one is currently sitting in it. And gets in range then the piston compresses.

The accelerometer that is built in to the Pysense 2.0 X is used to measure the angle the chair is currently in, this used to see if you are not currently sitting in what could be seen as an optimal position. 

You could go for a cheaper version of the development board that Pycom has to offer, either the LoPy4 or the WiPy 3.0 would be great choices since the multitude of connection choices doesn’t really matter in this case since, we use Wi-Fi only. I got mine in a bundle and might do something else with the board in the future. But if the single purpose for it is this project, something cheaper will suffice. Same for the Pysense 2.0 X, it isn’t really used to its full potential with all the sensors that aren’t used, since we only use it for the accelerometer. 

Everything isn't set in stone, you can pick and choose the breadboard, I opted to by a smaller one since I didn’t need the extra space when it comes to connecting sensors. Same goes for the length of cables, the only once that might be a bit important is the one that is going to reach the hall effect sensor later. Same with the magnet.

You will also need a computer to program and get everything up and running.


## Software

For the software that was used during this project and the development will be linked below, they are all free of charge and quite easy to get up and running. The things that are required to make this all work is either *Atom* or *VS code*, both IDE:s support *Pymakr* with is an addon that makes it possible to develop with MicroPython. This will also cover how you install them both, you will also need to download *Pycom Firmware Updater* and *Node.js*. All of which are linked below. 

This guide will be covering *Atom* as the chosen IDE since it was the one used during development. And we will install *Pymakr* in *Atom*

>Note: When you download Node.js, download **CURRENT** and not **LTS**.
* [Node.js](https://nodejs.org/en/download/current/)
* [Atom](https://atom.io/)
* [Pycom Firmware Updater](https://docs.pycom.io/updatefirmware/device/)

#### Building the foundation
Before we start with the project or anything for that matter, I would recommend you download Node.js first and follow the steps of the set-up process. It is quite easy to follow and just check the needed boxes when installing it, remember to install chocolatey when it asks you since it needs those files so Pymakr will work later. 

Next, I would recommend you install Atom, it is a breeze and shouldn’t prove difficult at all.
Now for the fun parts Pymaker the thing that will make you be able to do something with your FiPy. When you start Atom you will have an empty project and a welcome screen. 

![](https://i.imgur.com/Zaqqhiw.png)

* To find Pymakr you can either press “Install a package” to the right of the screen and then search “Pymakr” and install it.
* Or you can go into File -> Settings -> Install -> search “Pymakr” in the search field and then install it.

 

![](https://i.imgur.com/ynWgrsD.png)

If Pymakr doesn’t show up straight away don’t fret, either restart Atom or press in the bottom right coner on the “Pymakr” logo

![](https://i.imgur.com/Qrpwp7X.png)

It should look like this after you are done. 

#### Updating and flashing 
Now we can close atom for now and continue with our FiPy, which will need to be flashed. Install Pycom Firmware Updater if you haven’t already. If you have done that, we can continue with the next step. Connect the FiPy to your Pisense 2.0 X board, the LED on the FiPy should be on the same side as the USB port for the Pysense. You can see the two pictures as an example. After that you can connect the board with a Micro B usb-cable to your computer.
![](https://i.imgur.com/lCQyhe4.png)
![](https://i.imgur.com/SWxAbXr.png)

>Note: Be sure that the cable can transfer data!

After that open Pycom Firmware Updater and you will be greeted with this screen, just press continue unless you want to send in your data.

 ![](https://i.imgur.com/a8l3elf.png)

On the next step it is important that you note which port it is assigned to the COM# in my case it is 5, but that doesn’t matter. Next is that you want to be sure that you have development selected in Type and then we can continue to the next page.
 
![](https://i.imgur.com/YeeQDkH.png)

Here you want to check that the device type is the same as the one you got. Use FatFS as the File System and check all the boxes, Erase, Config, NVS and press continue. When the device is updated we can close the program and then open Atom again. 

![](https://i.imgur.com/zBEsKeH.png)


If you want more information regarding the choices you can read about them (https://docs.pycom.io/updatefirmware/device/).

#### Uploading code and the first project

With Atom open we can continue our journey to check if everything works, start by making a new project folder by pressing add folders and opening an empty folder that you have made, after you can see it in the project tab we can continue.
 

Now either your device will have been connected to Atom by default or we need to enable it. If you press the Connect Device you should be able to find yours, press it and it should light up a green circle next to the name.
![](https://i.imgur.com/i3gwJrt.png)
You should also have something like this called a REPL, in this you can just test it by typing print(“Hello world”) or just add two numbers, the response you get back is from the FiPy and not your PC.

![](https://i.imgur.com/6fgb03K.png)


Now to the code and how to upload it, if you right click the folder we created before you can create a new file name it “main.py” this is where our cool code will be. With main open copy and paste the code below into it. After that press the middle button in menu to the side of the REPL or press ctrl + alt + s. 
> Note: If you can't upload the code, be sure that you are in the folder with your code in Pymakr.

 ![](https://i.imgur.com/tpa0cEs.png)

And done! If everything is working correctly your FiPy should be switching colours with the LED from Red > Orange > Green.

###### Code
```python
import pycom
import time

pycom.heartbeat(False)
while True: #Forever loop
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1) #sleep for 1 second

    pycom.rgbled(0xFF3300)  # Orange
    time.sleep_ms(1000) #sleep for 1000 ms

    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
```
> Source: https://hackmd.io/@lnu-iot/rk4qNlajd

## Putting everything together

>Pinout

[Pysense 2.0 X](https://docs.pycom.io/gitbook/assets/pysense2-pinout.png)
[FiPy](https://docs.pycom.io/gitbook/assets/fipy-pinout.png)

Below you will find schematics on how everything should be connected, you can mirror this on a bigger breadboard if that is what you use. Since the Pysense shield doesn't really offer much when it comes to getting pins we need to have the FiPy on the breadboard so we can get the pins for it, in this case since we need one pin to connect the Hall effect senor so we can get the values from it. So the FiPy is on the breadboard, what now? Well, we start connecting the wires we need for the FiPy to even work, which is the red, yellow, blue, and orange wire. I would recommend looking at the pinout for both the Pysense and the FiPy to get a better understanding of how things are connected. 
*	Blue & orange, these are used to transfer data between the pc and the FiPy and the FiPy and the PC. So, we need it to upload code and for the FiPy to send information back to our PC. This is useful for debugging etc.
*	Red & Yellow, these are the power and ground pin. With these 4 wires we can power our device and even transfer data. But we want more!
*	Black cable is for 3.3V, we use this with our Hall effect sensor.
*	Green & white, these are the pins we need to connect to be able to use the accelerometer on our Pysense, we paid for it so lets use them instead of buying one separate.
*	Blue, this is the wire that sends the results back from our Hall effect sensor so we can know if something or someone is sitting in the chair.

> Note: When you connect everything it is very important that the cables goes in and out from the right place. The problem that might occur is that if you plug in a sensor in the 5v for example you might fry a sensor, so avoid that.

In the beginning start by just placing the right pin from the Pysense to the right pin on the breadboard that hosts the FiPy, it should be quite easy. When we connect the Hall effect sensor we just need to get another wire from the 3.3V row over to the spot where we are going to connect the sensor, same with ground and the sensor wire. If you have the flat side of the sensor facing you the 3.3V should go into the right leg of the sensor, ground in the middle and to the left the sensor wire. However, be sure that you keep 1 empty row between where you connect the sensor and the wires coming from the FiPy, this row will be used to place a 10k Ohm resistor. This will be connected in the holes between the 3.3V and the sensor wire.
As it stands right now, this is mainly in development. Mostly because the components are quite expensive for what it is currently doing. If this product would go to production I would exchange the FiPy to a generic ESP32 device, buy a separate accelerometer and cut down costs quite significantly.


![](https://i.imgur.com/gqSXlRo.png)

## Platform
The platform used for the project is Adafruit IO, this is a cloud-based database and is made to visualise data and offers other features as well. Is utilizes feeds that you combine with the dashboard to display the information/data that you want to be used. 

It is really easy to set up so that was a bonus, the negative side is that the data isn’t saved on a local device so you are limited the control you have over how the data is stored and any data breaches might leak it. However, I don’t really see this as a problem for now since the thing we are monitoring is just a chair, it isn’t really something that would be detrimental if it got leaked. And since it doesn’t really control anything in my home I wouldn’t really care if someone got access to it. 

If I had more time and another raspberry PI on hand I would have been interested on doing a TIG stack solution on it so I can host the data myself. Another reason I chose Adafruit IO is the ease of using a webhook to integrate notification with discord, here you can choose how often it should notify you and what values it should send.

## The code
The entire code can be found on [GitHub](https://github.com/plebgurt/IoT-Chair-monitoring-system), it should be quite easy to get it up and running. The only thing that isn’t included in the GitHub link is the "config.py" file, this is where you can store your Wi-Fi ssid and password, and all the feeds required to link your Adafruit IO feeds to the project. The structure can be found below.
>Note: Things worth pointing out is that the Wi-Fi needs to be 2.4GHz, and we will cover where to find the feeds later on.
```python=
#File name should be “config.py”
SSID = 'Wi-Fi name'
PASS = 'Wi-Fi pass'
AIO_USER = 'User'
AIO_KEY = 'Key'
AIO_UPRIGHT_TIME = 'Feed'
AIO_RECLINED_TIME = 'Feed'
AIO_ANGLE = 'Feed'
AIO_CURRENTLY_SITTING = 'Feed'
AIO_TOTAL_SITTING_TIME = 'Feed'
AIO_SEND_REMINDER = 'Feed'
```
For this project there is three downloaded libraries needed for this to work that is mqtt.py, pycoproc_2.py and LIS2HH12.py. MQTT is used for sending the data to Adafruit IO, pycoproc_2 is the library for the Pysense and LIS2HH12 is for the accelerometer. 
This is how we judge which pin we are going to receive the data from the external Hall effect sensor
halleffect = Pin('P15', mode=Pin.IN)
If you would like to change the pin that would be the place to do it.
When it comes to connecting the device there isn’t much you need to do except create your own config.py file, for example it is used like this in the boot.py when it comes to connecting you with you Adafruit database.
```python=
AIO_USER = config.AIO_USER
    AIO_KEY = config.AIO_KEY
    AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything

    # Use the MQTT protocol to connect to Adafruit IO
    client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
```
And for Wi-Fi it is quite similar in that it uses Config.SSID and Config.PASS
```python=
if not wlan.isconnected():          # Check if already connected
        print("Connecting to WiFi...")
        # Connect with your WiFi Credential
        wlan.connect(config.SSID, auth=(WLAN.WPA2, config.PASS))
        # Check if it is connected otherwise wait
        while not wlan.isconnected():
            pass
    print("Connected to Wifi")
```
Since this application sends data quite often and each time you send data you want to check if it gets successfully sent I figured that it would be easier to make a function that receives the MQTT topic and the values that is going to be sent, so I made this.
```python=
def send_data(inc_topic, value):
    try:
        connectiondata.CLIENT.publish(topic = inc_topic, msg=str(value))
        print('SENT: {}, {}'.format(inc_topic, value))
    except Exception as e:
        print('FAILED: {}, {}'.format(inc_topic, value))
```

I also noticed that Adafruit doesn’t really have anyway of making something send just once, or I must have just missed it. But I found a solution, it is a dictionary which contains the hour mark as a key and a bool as the value. This is to make sure it only get sent once per hour and this is handled by another feed in Adafruit. You can change these values if you want it to be less frequent, just remind you at the two hour mark or just the one hour mark. This only works with whole hours for now, so you can set a reminder for 45 minutes etc.
```python=
reminder_sent_dictionary = {0: False, 1 : False, 2 : False, 3 : False, 4 : False, 5 : False, 6 : False}

def send_reminder(time):
    if reminder_sent_dictionary.get(time) == False:
        send_data(config.AIO_SEND_REMINDER, time)
        reminder_sent_dictionary[time] = True
```

This is also how we figured out if the user is reclined in the chair using the accelerometer, it isn’t really complicated it checks the angle of the sensor and returns True if the value is over 10 and less than -10 degrees. This data is also sent to Adafruit IO.
```python=
def check_is_chair_reclined():
    send_data(config.AIO_ANGLE, acc.pitch())
    if acc.pitch() < -angle or acc.pitch() > angle:
        return True
    else:
        return False
```
This is how the code for documentation of our sitting time is calculated.
```python=
time_dictionary['start_time_reclined'] == 0
if time_dictionary['start_time_upright'] == 0:
    time_dictionary['start_time_upright'] = time.time()
current_time = time_dictionary['end_time'] - time_dictionary['start_time_upright']
time_dictionary['total_time_upright'] = current_time
send_data(config.AIO_UPRIGHT_TIME,time_convert_min(time_dictionary['total_time_upright']))
pycom.rgbled(0x00FF00)
```
This is for the upright position, so since we aren’t reclined anymore it resets the start time to zero, it checks if the upright start time is zero, if it is the timer starts otherwise it skips this step. After that it calculates how long you have been sitting by subtracting your end time which is updated every minute, this gets us the duration for how long the user has been sitting after that it adds it to the total time for sitting upright which we keep track of on our dashboard.

## Transmitting the data / connectivity

The device sends data every minute trough Wi-Fi to the Adafruit IO database, this uses MQTT so you can subscribe to the feed that you want information from. We also utilize webhooks to connect Adafruit IO to a channel in discord that can send a message when certain requirements are met. For example, if you have been sitting for mor than an hour Adafruit IO will send trigger an event and send a message to the bot on the discord server that you can see.

I chose to send it every minute because I still want a semi accurate estimate on how long you are sitting in the chair. It could be increased to 5 minutes in case the user has a battery and wants to prolong the lifetime of said battery. Since I didn’t receive mine in time for this report, I opted for a more accurate number instead. I also chose Wi-Fi since it would be hard to motivate using something else in this particular use case since it is mounted on a chair indoors and you will probably have Wi-Fi there. You could opt for LoRa or LTE, but I don’t really see any benefits of doing that for now. Maybe if you want to be sure it works even if the router stops working?

## Presenting the data

* Sign up and log in on [Adafruit.IO](https://accounts.adafruit.com/)
* Go to this link so you can see your control panel [IO.adafruit](https://io.adafruit.com/)
* Go into the IO page and press "Feeds"
![](https://i.imgur.com/vQ6PM31.png)

* Before we even start with the feeds you can press the yellow key icon in the top right corner, save the username and key, this will be put in the config file.

* Now we will create the feeds. You can either choose to have these in the default, but I opted to have them in their own group. Just press "New Feed" in the top and name it. It should look something like this when you are done.
![](https://i.imgur.com/nsKV6Ex.png)

* Go in on all the feeds by clicking the title of the feed, press the "Feed Info" button. Write down all the feeds MQTT, we will need these for later when we put it in the config file.

* Now you have all your info, create a config file with the code from before, and put the Wi-Fi ssid and password in it, do the same for the information we got from Adafruit.

* Now when that is done we can go to the tab called "Dashboards", create a new dashboard. Enter it and click the cog in the top right and choose "create new block".
* What we want now is:
    * Two indicators that will recive the feed for "Currently sitting" and "Current angle". These are to indicate if the user is sitting and is they are reclined. Currently sitting should be = 0, and the angle should be <= -10, add another condition and make that >= 10.
    * After we want two gauges, these are for counting the current time you have been sitting in a certain position. They use the feeds "Upright time" and "Reclined time". Set the max value to 59.
    * After that we will make two graphs, one for the "Current angle" feed, and the other one for "Total sitting time"
* Now you should have something that looks like this after you organize them, feel free to add or change certain blocks if you want to!
![](https://i.imgur.com/gvET4aS.png)


Now this is cool and all, but this is just displaying the data. If we forget to open the dashboard is won't help us get up and start moving and get reminded for sitting still for so long. We need to make a few actions. For this open the tab called "Actions"
* Before we do anything here we need to open Discord, create your own server or if you own one you can use that. 
* In a Text channel press the cog when you hover over it to open the settings, in there select "Integrations", create a webhook and copy the URL. And we are done with discord for now.
* Back to Adafruit, create a new action that is reactive.
* Your fields should look like this:
![](https://i.imgur.com/JuyA6rn.png)

If you want to get fancy and tag yourself when the bot pushes a message you can use this [tutorial](https://www.remote.tools/remote-work/how-to-find-discord-id) to find your ID and later edit the JSON file in the Action. The result could look like this.

![](https://i.imgur.com/p5xuxn0.png)

Which in return will give you a message on discord that looks like this.

![](https://i.imgur.com/tOKXSs5.png)

Adafruit also hosts your data for 30 days before it gets deleted, which isn't a problem for how I am currently using the service. In the future it might be good to make my own soloution so I can save the data for how long I want, and maybe add up the total amount of time spent in the chair for each day, how long the avarage session was etc. I chose Adafruit because of the features I just presented and the fact that if I wanted to host my own I would rather do it on a separate device than my main PC.

## Finalizing the design

I am quite pleased overall with how the project went. I got myself another ESP32 board and an OLED display that I could have on my desk that receives data and displays it without having to open Adafruit to see how long I have been sitting for. But unfortunately, time and the project got in the way for those ambitions but will continue to tinker on it and will update below if I succeeded. 

I think I might have used another sensor to feel if someone is in the chair other than the Hall effect sensor also, maybe an ultra-sonic one.  But since I have a cat at home, I didn’t want the risk of causing it discomfort with the noise, so this worked out anyways. 

I wish that I had time also to find some way to get a case or 3D-print a case for the project, I just reused the box the FiPy came with and cut and drilled some holes in it to be able to attach everything to one housing. I have learned a lot, more than I imagined I would and might have found a new hobby to tinker with. I already have a few things in mind that could be cool and useful to have. It also feels really cool to actually build it yourself I have done a fair bit of programming before, but it just feels different when you can hold something in your hand that does something simple rather than some complex algorithm on a computer.
![](https://i.imgur.com/Cm0qEDA.jpg)

![](https://i.imgur.com/qUpTceW.jpg)
