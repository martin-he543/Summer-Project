# Must have uc480 folder in home directory environment
# Custom Documentation found at:
# https://ddietze.github.io/Py-Hardware-Support/uc480.html
# Instructions on finding necessary DLL (drivers):
# https://www.thorlabs.com/software/MUC/DCx/Drivers/32bit_README.TXT
# Where to find IDS DLLs:
# https://en.ids-imaging.com/download-details/AB.0010.1.34800.23.html?os=linux&version=&bus=64&floatcalc=#anc-software-18
# https://en.ids-imaging.com/download-details/AB.0010.1.34800.23.html#anc-software-18

import uc480
import pylab as pl

cam = uc480.uc480() # Create instance, connect to library
cam.connect() # Connect to Camera

img = cam.acquire() # Take single image
cam.disconnect() # Disconnect from camera

pl.imshow(img)
pl.show()


# DOCUMENTATION to uc480.uc480() commands
# You can use cam.____________ [Any of the following]
''' 

acquire(N=1)

    Synchronously captures some frames from the camera using the current settings and returns the averaged image.
    Parameters:	N (int) – Number of frames to acquire (> 1).
    Returns:	Averaged image.

acquireBinned(N=1)

    Record N frames from the camera using the current settings and return fully binned 1d arrays averaged over the N frames.
    Parameters:	N (int) – Number of images to acquire.
    Returns:	

        Averaged 1d array fully binned over the x-axis.
        Averaged 1d array fully binned over the y-axis.
        Maximum pixel intensity before binning, e.g. to detect over illumination.

acquireMax(N=1)

    Record N frames from the camera using the current settings and return the column / row with the maximum intensity.
    Parameters:	N (int) – Number of images to acquire.
    Returns:	

        Column with maximum intensity (1d array).
        Row with maximum intensity (1d array).

call(function, *args)

    Wrapper around library function calls to allow the user to call any library function.
    Parameters:	

        function (str) – Name of the library function to be executed.
        args (mixed) – Arguments to pass to the function.

    Raises:	

    uc480Error – if function could not be properly executed.

connect(ID=0, useDevID=False)

    Connect to the camera with the given cameraID. If cameraID is 0, connect to the first available camera. When connected, sensor information is read out, image memory is reserved and some default parameters are submitted.

        Changed in version 11-28-2016:

        Added useDevID to enable camera selection via cameraID or deviceID.

    Parameters:	

        ID (int) – ID of the camera to connect to. Set this to 0 to connect to the first available camera (default).
        useDevID (bool) – Set to True if camera should be identified by deviceID instead. By default (False), cameraID is used.

connect_to_library(library=None)

    Establish connection to uc480 library depending on operating system and version. If no library name is given (default), the function looks for

            uc480.dll on Win32
            uc480_64.dll on Win64
            libueye_api.so.3.82 on Linux32
            libueye_api64.so.3.82 on Linux64.

    Parameters:	library (str) – If not None, try to connect to the given library name.

create_buffer()

    Create image buffer for raw data from camera.

    Note

    This function is automatically invoked by connect().

disconnect()

    Disconnect a currently connected camera.

get_buffer()

    Copy data from camera buffer to numpy array and return typecast to uint8.

    Note

    This function is internally used by acquire(), acquireBinned(), and acquireMax() and there is normally no reason to directly call it.

get_cameras()

    Queries the number of connected cameras and prints a list with the available CameraIDs.

get_exposure()

    Returns current exposure time in milliseconds.

get_exposure_limits()

    Returns the supported limits for the exposure time (min, max, increment).

get_gain()

    Returns current gain setting.

get_gain_limits()

    Returns gain limits (min, max, increment).

get_sensor_size()

    Returns the sensor size as tuple: (width, height).

    If not connected yet, it returns a zero tuple.

    New in version 01-07-2016.

query(function, *args)

    Wrapper around library function calls to allow the user to call any library function AND query the response.
    Parameters:	

        function (str) – Name of the library function to be executed.
        args (mixed) – Arguments to pass to the function.

    Returns:	

    Result of function call.
    Raises:	

    uc480Error – if function could not be properly executed.

set_blacklevel(blck)

    Set blacklevel compensation on or off.

set_exposure(exp)

    Set exposure time in milliseconds.

set_gain(gain)

    Set the hardware gain.
    Parameters:	gain (int) – New gain setting (0 - 100).

set_gain_boost(onoff)

    Switch gain boost on or off.

stop()

    Same as disconnect.

    New in version 01-07-2016.
 '''