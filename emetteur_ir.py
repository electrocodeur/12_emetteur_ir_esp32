# George Bantique | tech.to.tinker@gmail.com

from machine import Pin
from ir_tx import NEC
from time import sleep

nec = NEC(Pin(26, Pin.OUT, value = 0))

while True:
    nec.transmit(0x0000, 0x0d)
    sleep(2)
    nec.transmit(0x0000, 0x1f)
    sleep(2)