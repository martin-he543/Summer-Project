# Designed for Raspberry Pi 
# Check for connected Resolutions "v4l2-ctl --list-formats-ext"

''' For USB Webcams ''' 
import cv2
#hello 

# Use "ls /dev/" to find which port has /video_ port
cam = cv2.VideoCapture("/dev/video5") # initialise camera
s, img = cam.read()
if s: # only run when no errors
    print("no error")
    cv2.namedWindow("cam-test")
    cv2.imshow("cam-test",img)
    cv2.waitKey(0) # 0 = wait until clicked, otherwise window showtime in ms
    cv2.imwrite("hello.jpg",img) # save image
    cv2.destroyWindow("cam-test")
    
cam.release() # release resource


''' For ThorLabs Cams ''' 
import cv2
import numpy as np
from instrumental.drivers.cameras import uc480

instruments = uc480.list_instruments()
cam = uc480.UC480_Camera(instruments[0])
cam.start_live_video(framerate = "10Hz")

while cam.is_open:
     
     frame = cam.grab_image(timeout='100s', copy=True, exposure_time='10ms')
     
     frame1 = np.stack((frame,) * 3,-1) #make frame as 1 channel image
     frame1 = frame1.astype(np.uint8)
     gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

     #now u can apply opencv features
     cv2.imshow('Camera', gray)    
     if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cam.close()
cv2.destroyAllWindows()