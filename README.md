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
