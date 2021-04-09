from VNH5019 import VNH5019
from time import sleep
from machine import Pin
from machine import PWM
from machine import ADC

up = Pin(6, Pin.IN)
down = Pin(7, Pin.IN)


motor_1 = VNH5019(cs = True, pos = True)
motor_2 = VNH5019(3, 4, 5, False, pos = True, pos_pin=28)


while True:
    if up is True:
        motor_1.drive_cw()
        motor_2.client(motor_1.motor_pos())
    if down is True:
        motor_1.drive_ccw()
        motor_2.client(motor_1.motor_pos())
    else:
        motor_1.stop()
        motor_2.stop()
