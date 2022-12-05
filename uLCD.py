# led_test_client.py
# Test client for erpc led server example
# Author: becksteing
# Date: 5/13/2019
# Blinks LEDs on a connected Mbed-enabled board running the erpc LED server example

from time import sleep
import erpc
from uLCD_show import *
import sys


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python led.py <serial port to use>")
        exit()

    # Initialize all erpc infrastructure
    xport = erpc.transport.SerialTransport(sys.argv[1], 9600)
    client_mgr = erpc.client.ClientManager(xport, erpc.basic_codec.BasicCodec)
    client = client.uLCDServiceClient(client_mgr)

    print("Call putc")
    client.putC(65)
    sleep(0.5)
    client.putC(76)
    sleep(0.5)
    client.putC(76)
    sleep(0.5)
    client.putC(69)
    sleep(0.5)
    client.putC(78)

    print("Call locate")
    client.locate(9, 0)
