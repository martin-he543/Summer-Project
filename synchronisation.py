## The other files are mere demos of each individual step required.
# 1. Ability to connect to OpenFlexure Delta Stage - control stepper motors.
# 2. Ability to import uc480 library, which controls ThorLabs CCD and CMOS cameras.
# 3. Ability to capture pictures using these ThorLabs Cameras.

## [1] - EXAMPLE COMMANDS TO MOVE DELTA STAGE
# This code is for running on the Raspberry Pi. It cannot be run remotely (as of yet).
# NOTE - Python Libraries required: "(pip3 install) openflexure_microscope_client"
# You must have latest version of numpy (>2.20). If not, "run pip3 install numpy --upgrade"

import openflexure_microscope_client as ofm_client
from PIL import Image

microscope = ofm_client.find_first_microscope() # Connect to OFM Delta Stage
#microscope = ofm_client.MicroscopeClient("microscope.local:5000") # Use if above script does not work.
pos = microscope.position
pos_array = microscope.get_position_array()
print(pos)

pos['x'] += 100
print(pos_array)

pos['y'] -= 100
print(pos)

image = microscope.capture_image() # now PIL image object
image = microscope.capture_image_to_disk()
# autofocus() # to autofocus object, with OpenFlexure software

## [2] - CONTROLLING THORLABS CMOS & CCDs
# Must have uc480 folder in home directory environment
# [Backup uc480 module: https://instrumental-lib.readthedocs.io/en/stable/uc480-cameras.html]
# Instructions on finding necessary DLL (drivers):
# https://www.thorlabs.com/software/MUC/DCx/Drivers/32bit_README.TXT
# Where to find IDS DLLs:
# https://en.ids-imaging.com/download-details/AB.0010.1.34800.23.html?os=linux&version=&bus=64&floatcalc=#anc-software-18
# https://en.ids-imaging.com/download-details/AB.0010.1.34800.23.html#anc-software-18

import uc480
import pylab as pl

# Custom Documentation found at:
# https://ddietze.github.io/Py-Hardware-Support/uc480.html

cam = uc480.uc480() # Create instance, connect to library
cam.connect() # Connect to Camera

img = cam.acquire() # Take single image
cam.disconnect() # Disconnect from camera

pl.imshow(img)
pl.show()

