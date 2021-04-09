from machine import Pin
from machine import PWM
from machine import ADC

class VNH5019():
    def __init__(self, motor_cw = 0, motor_ccw = 1, motor_pwm = 2, cs = False, cs_pin = 26, pos = False, pos_pin = 27):
        """Defaults are set up to work with the first motor instance. 
        Pins will need to be updated for the second instance"""

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
        if pos == True:
            self.motor_pot = ADC(pos_pin)

        #class variables
        self.cs_val = 0
        self.position_val = 0
        self.def_gain = .75

    def drive_cw(self, duty = (65535*self.def_gain)):
        self.speed.duty_u16(duty)
        self.cw.on()
        self.ccw.off()

    def drive_ccw(self, duty = (65535*self.def_gain)):
        self.speed.duty_u16(duty)
        self.ccw.on()
        self.cw.off()

    def stop(self):
        self.speed.duty_u16(0)
        self.cw.off()
        self.ccw.off()

    def cs_read(self):
        for i in range(9):
            self.cs_val += self.cur_sens.read_u16()
        self.cs_val = self.cs_val/10
        return self.cs_val

    def motor_pos(self):
        for i in range(9):
            self.position_val += self.motor_pot.read_u16()
        self.position_val = self.position_val/10
        return self.position_val

    def client(self, host, gain = .75):
        skew = host - self.motor_pos()
        
        if skew >0:
            gain = 

        if skew <0:
            if skew < 1000: 
                 
            if host >= self.motor_pos():
