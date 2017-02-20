This is a simple editor for the kboard, primarily intended for linux users. Well, really it's intended for myself, but anyone is welcome to use it. The only functionality this offers over the official editor from KMI is opportunity to set bend to separate ranges for up and down, and some sensitivities can be set to a larger range. That and linux compatibility.

This is very unofficial and for all I know you could brick your kboard or send your children to war or something else awful so absolutely no guarantees offered or implied.


## Installation

There is no installation required, as it is meant to be used in the interactive python interpreter. It should be compatible with both python2.7 and python 3, but most distros only have pygame packaged for python 2.7 even though pygame is python3 compatible. For convenience you can copy kboard.py to usr/local/lib/python2.7/dist-packages/ and it will be available regardless of where your terminal is when you run python. Otherwise you need to be sure you are in this directory when you run python.

There are a few simple dependencies for using this script. On ubuntu install them all simply by typing:
    sudo apt-get install python2.7 python-pygame

And it will get what you need.


## Usage

Once that is done simply run the commands:

```{python}
python
import kboard #this will show you the current configuration
#you can change whatever you like such as:
kboard.setOnThreshold(25) #tab will autocomplete, and tab 2x will show you what all the various set functions are.
exit() #leave python
```


The kboard module sends the sysex through the alsa midi_through output port, so be sure to connect that to the kboard.

Most functions allow a range of 0-127, but exceptions are noted below. Some of the ranges indicated are what the KMI app limits you to, though in this app they aren't actually limited to this range. Out of bounds values are clamped to the min or max.
Here is the complete list of available functions and their description:

```{python}
kboard.load("filename") # saves the current configuration sysex to a file
kboard.save("filename") # loads a saved file into the current configuration
kboard.setChannel(v) # 0-15 zero indexed midi channel
kboard.setOnThreshold(v) # threshold for turning on a note

kboard.setPadBendMax(v) # 0-12 semitones, range of upward bend from pad
kboard.setPadBendMin(v) # 0-12 semitones, range of downward bend from pad

kboard.setPressureCC(v) # CC number for pressure
kboard.setPressureChanPressureMode("v") # Yes/No send channel pressure messages instead of CC
kboard.setPressureDisabledReturn("v") # Yes/No sets whether to send a CC when Pressure is disabled
kboard.setPressureDisabledReturnValue(v) # CC value when pressure is disabled
kboard.setPressureSensitivity(v) # 60-126

kboard.setTiltBendMax(v) # 0-12 semitones, range of upward bend from tilt
kboard.setTiltBendMin(v) # 0-12 semitones, range of downward bend from tilt
kboard.setTiltBendMode("v") # Yes/No sets whether tilt sends bend or CC messages
kboard.setTiltCC(v) # CC number for tilt when tilt bend mode is off
kboard.setTiltDisabledReturn(v) # Yes/No sets whether to send a CC when Pressure is disabled
kboard.setTiltDisabledReturnValue(v) # CC value when tilt disabled
kboard.setTiltSensitivity(v) # 57-127

kboard.curves # shows list of available velocity curves
kboard.setVelocityCurve("v") # lin/log/sin/cos/exp/inv
kboard.setVelocitySensitivity(v) # 0-255

kboard.reset() # resets the current configuration to the default values
```

After each action the configuration is sent to the kboard and is shown such as:
```
Configuration to send to KBoard:

 Channel:                       0
 Pressure CC:                   1
 Pressure sends Chan. Pressure: No
 Tilt CC:                       127
 Tilt sends Bend:               Yes
 Pad Bend Max:                 +12 semitone
 Pad Bend Min:                 -12 semitone
 Tilt Bend Max:                +1 semitone
 Tilt Bend Min:                -1 semitone
 Velocity Sensitivity:          100
 Pressure Sensitivity:          100
 Tilt Sensitivity:              77

 Velocity Curve:                lin
 Return a Value...
   when Pressure Disabled:      Yes
    Disabled Pressure Value:    127
   when Tilt Disabled:          Yes
    Disabled Tilt Value:        127
 Note-On Threshold:             16
```
This is the conguration that was just sent or will be sent if you call kboard.send(). There is no way to read the current configuration of the kboard.
