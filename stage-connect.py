# This code is for running on the Raspberry Pi. It cannot be run remotely (as of yet).
# NOTE - Python Libraries required: (pip3 install) openflexure_microscope_client

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

# autofocus()