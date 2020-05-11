"""
Characteristics    |   Functionality
---------------------------------------
color              |
brand              |
ACPower            |
headphone          |
                   |
power_led          | power_switch  ( ON / OFF)
mode_led           | mode_switch   ( AM / FM )
frequency          | band_tuner    ( 88 - 108 )
volume             | volume_tuner  ( 1 - 10 )
---------------------------------------

Go to the market and buy a new Radio
Switch ON the radio
Set the mode to FM
Set the frequency to 102.2
Set the volume to 8
Listen to your song
Switch OFF the radio
Destroy the Radio
"""

class Radio:

    # Class Variables
    color = "brown"
    brand = "Philips"
    ACPower = False
    headphone = False    
    
    # Constructor
    def __init__(self):
        # Instance variables
        self.power_led = "ON"
        self.mode_led = None
        self.frequency = 0.0
        self.volume = 0
        print("Your Radio is Ready to be Played ")

    # Instance Method
    def power_switch(self,power_status):
        self.power_led = power_status
        print("Your Radio Power is " + str(self.power_led))

    # Instance Method
    def mode_switch(self,mode_status):
        self.mode_led = mode_status
        print("Your Radio Mode is set to " + str(self.mode_led))
    
    # Instance Method
    def band_tuner(self,freq_value):
        self.frequency = freq_value
        print("Your Radio frequency is set to " + str(self.frequency))

    # Instance Method
    def volume_tuner(self,vol_value):
        self.volume = vol_value
        print("Your Radio volume is set to " + str(self.volume))


#Make a Actual Radio from the blueprint
chunnu_ka_radio = Radio()
print("Color of my Radio = " + str(Radio.color))
print("Brand of my Radio = " + str(Radio.brand))

#Switch ON the radio
chunnu_ka_radio.power_switch("ON")

#Set the mode to FM
chunnu_ka_radio.mode_switch("FM")

#Set the frequency to 102.2
chunnu_ka_radio.band_tuner(102.2)

#Set the volume to 8
chunnu_ka_radio.volume_tuner(8)

#Listen to your song


#Switch OFF the radio
chunnu_ka_radio.power_switch("OFF")


# Destroy the Radio
chunnu_ka_radio = None
