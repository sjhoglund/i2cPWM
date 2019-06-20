# i2cPWM
Craftbeerpi3 plugin to control actors using i2c

This plugin was created to work with Adafruit's DC & Stepper Motor HAT for Raspberry Pi (https://www.adafruit.com/product/2348)

Reason for using this HAT is to take advantage of a the fully-dedicated PWM driver chip. The PWM control is amazing!

Steps are as follows:

1. Install and configure i2c (https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)
2. Reboot!
3. Install and configure SPI (next page from step 11)
4. Reboot!
5. Install Adafruit robot hat Lib (https://learn.adafruit.com/simple-raspberry-pi-robot/software)
