# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:36:39 2020

@author: user
"""
"""
Code Challenge 1
  Filename:
      radio.py

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
    def __init__(self, switch, mode, frequency, volume):
        self.switch = switch
        self.mode = mode
        self.frequency = frequency 
        self.volume = volume

    def On_Radio(self):
        return "Radio is Switch "+self.switch \
               + "\nSet the mode to" + self.mode \
               + '\nFrequency   ' + self.frequency \
               + '\nVolume '+ self.volume 
    
    def Off_Radio(self):
        return "Radio is switch "+self.switch
    
    def __del__(self): 
        print('\nRadio Destroyed')

        
New_Radio = Radio("ON","FM","102.2","8")        

print(New_Radio.On_Radio())

New_Radio.switch = "OFF"

print(New_Radio.Off_Radio())

del New_Radio
