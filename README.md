# RFID library for Jetson Family
This is a simple python library that provides a way to communicate jetson devices with MFRC522 modules

## Installation
The easier way to install is through pip
```
pip install Jetson-MFRC522
```
also you can install it manually by clone the repo and run pip install command
## Example
This is a simple example that read id and text in RFID card, tested in Jetson Nano.
```python
from time import sleep
import sys
from Jetson_MFRC522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
```
## Getting started on Jetson Nano

This library use the SPI communication, and custom GPIO Jetson library, by default use SPI1 interface of Jetson Nano, Configure the Jetso for SPI, use the command
```bash
sudo /opt/nvidia/jetson-io/jetson-io.py
```


![image](https://user-images.githubusercontent.com/35088759/195137955-cd688e92-e85c-42b6-b9d8-cccbe4dea9e0.png)

We select Configure 40-pin expansion header:



![image](https://user-images.githubusercontent.com/35088759/195138202-44eee403-d356-4609-99bc-3f17e37c2713.png)

in our case we select SPI1. Use the arrow keys to navigate to the desired entry, Return selects/deselects the entry. Select Back when done. You should see the new configuration on the main menu. Save and reboot to reconfigure pins.

### Wiring the RFID RC522

| RFID module  |  Jetson Nano | 
|---|---|
|SDA   | PIN 24               |
|  SCK |   PIN 23            |   
|  MOSI | PIN 19  |   
|  MISO | PIN 21  |   
|  GND | PIN 6  |   
|  RST | PIN 22  |   
|  3.3V | PIN 1  |
