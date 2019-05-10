import time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

from modules import cbpi
from modules.core.props import Property
from modules.core.hardware import ActorBase

@cbpi.actor       
class i2cPWM(ActorBase):

    mx = Property.Select("Element Number", options=[1,2,3,4], description="number between 1 and 4")
    frequency = Property.Number("Cycles Per Second", configurable=True)
    
    speed = 250
    power = 100
    stopped = True
    
    # create a default object, no changes to I2C address or frequency
    mh = Adafruit_MotorHAT(addr=0x60)
    myMotor = mh.getMotor(1)
    
    def init(self):
        self.mh = Adafruit_MotorHAT(addr=0x60, freq=int(self.frequency))
        self.myMotor = self.mh.getMotor(int(self.mx))   
            
    def on(self, power):
        self.stopped = False
        self.myMotor.setSpeed(255)
        self.myMotor.run(Adafruit_MotorHAT.FORWARD)
        
    def set_power(self, power):
        if power is not None:
            i2cPWM.power = power
        if self.stopped is False:
            self.myMotor.setSpeed(int(i2cPWM.power))
        
    def off(self):
        self.stopped = True
        self.myMotor.setSpeed(0)
        self.myMotor.run(Adafruit_MotorHAT.RELEASE)