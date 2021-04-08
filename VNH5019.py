from machine import Pin
from machine import PWM
from machine import ADC

class VNH5019():
    def __init__(self, motor_cw = 0, motor_ccw = 1, motor_pwm = 2, cs = False, cs_pin = 26):
    
        #set up motor direction inputs
        self.cw = Pin(motor_cw, Pin.OUT)
        self.ccw = Pin(motor_ccw, Pin.OUT)
        #set up motor speed
        self.speed = PWM(Pin(motor_pwm))
        self.speed.freq(1000)
        self.speed.duty_u16(0)
        #set up cs
        if cs == True:
            self.cur_sens = ADC(cs_pin)

        #class variables
        self.value = 0

    def drive_cw(self, duty = 65535):
        self.speed.duty_u16(duty)
        self.cw.on()
        self.ccw.off()

    def drive_ccw(self, duty = 65535):
        self.speed.duty_u16(duty)
        self.ccw.on()
        self.cw.off()

    def stop(self):
        self.speed.duty_u16(0)
        self.cw.off()
        self.ccw.off()
    
    def cs_read(self):
        for i in range(9):
            self.value += self.cur_sens.read_u16()
        self.value = self.value/10
        return self.value

        
