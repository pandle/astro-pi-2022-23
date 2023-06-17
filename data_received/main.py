import csv
import cv2
import numpy as np

from datetime import datetime, timedelta
from gpiozero import MotionSensor
from io import BytesIO
from logzero import logger, logfile
from orbit import ISS
from pathlib import Path
from picamera import PiCamera
from sense_hat import SenseHat
from time import sleep


### SENSOR FUNCTIONS ###
def detect_motion(motion_sensor: MotionSensor) -> int:
    """
    Detects motion using the `motion_sensor` sensor. It is important that
    the motion_sensor is connected to GPIO pin 12.

    Args:
        motion_sensor [MotionSensor]: The motion sensor to be used
    
    Returns:
        motion_detected [int]: The motion value detected by the sensor. It can
            be either 0 (no motion) or 1 (motion detected).
    """
    motion_detected = motion_sensor.value
    return motion_detected

def capture_image(camera: PiCamera, image_format: str = "jpeg") -> BytesIO:
    """Captures an image from the given PiCamera, using the specified
    format, which defaults to JPEG.
    Remember to close the camera outside the function call.

    Args:
        camera [PiCamera]: the PiCamera instance from which to capture the photo
        format [str]: the image format to return 
    
    Returns:
        stream [BytesIO]: A stream of bytes representing the image, following
            the specified format
    """
    stream = BytesIO()
    camera.start_preview()
    sleep(1)
    camera.capture(stream, format=image_format)
    camera.stop_preview()

    return stream

def recognize_humans(image_stream: BytesIO):
    """
    Recognizes any humans present in the image (represented by the image stream)
    and returns the amount of said humans recognised.

    Args:
        image_stream [BytesIO]: the byte stream that represents the image

    Returns:
        n_humans [int]: How many humans are recognized from analyzing the image.
    """
    data = np.fromstring(
        image_stream.getvalue(), dtype=np.uint8
    )
    
    image = cv2.imdecode(data, 1)
    
    # Initialize HOG descriptor (used for human recognition)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(
        cv2.HOGDescriptor_getDefaultPeopleDetector()
    )

    # Recognise humans in the image
    # `humans` is the list of humans recognised
    (humans, _) = hog.detectMultiScale(
        image,
        winStride=(10, 10),
        padding=(24, 24),
        scale=1.05
    )
    # `n_humans` is the amount of humans recognised
    n_humans = len(humans)

    return n_humans

### CSV FUNCTIONS ###
def create_csv_file(data_file):
    """Create a new CSV file and add the header row"""
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = (
            "counter", "date_time", "latitude", "longitude",
            "temperature", "humidity", "pressure",
            "pitch", "roll", "yaw",
            "accel_x", "accel_y", "accel_z",
            "gyro_x", "gyro_y", "gyro_z",
            "mag_x", "mag_y", "mag_z",
            "motion_detected", "humans_detected" 
         )

        writer.writerow(header)

def add_csv_data(data_file, data):
    """Add a row of data to the data_file CSV"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def add_sensor_metrics(
    sense: SenseHat, motion_sensor: MotionSensor, 
    camera: PiCamera, params: tuple,
    detect_humans: bool = False # default value is set to False
) -> tuple:

    """
    Utilize SenseHat, MotionSensor and PiCamera sensors to measure data and data
    to the `params` tuple, which will be used to save the data in the CSV.
    Human detection only happens if `detect_humans` is set to True (default value: False), 
    since it is a time-consuming operation. 

    Args:
        sense [SenseHat]: The Sense Hat to use
        motion_sensor [MotionSensor]: The motion sensor to use
        camera [PiCamera]: The camera to use
        params [tuple]: The parameter tuple containing the data to insert in the CSV
        detect_humans [bool]: Whether the program should detect humans or not. (Default: False)
    
    Returns:
        params [tuple]: The new tuple containing all the data
    """
    
    # Measure environment
    temperature = round(sense.temperature, 8)
    humidity = round(sense.humidity, 8)
    pressure = round(sense.get_pressure(), 8)

    # Measure orientation, accelerometer, gyroscope and magnetometer values
    orientation = sense.get_orientation()
    accel = sense.get_accelerometer_raw()
    gyro = sense.get_gyroscope_raw()
    mag = sense.get_compass_raw()

    # Motion detection
    motion_detected = detect_motion(motion_sensor)

    if motion_detected > 0:
        logger.info("Motion detected")

    n_humans = 0 # Default value
    if detect_humans == True:
        # Get byte stream representing image and analyze it for human presence.
        # The image will not be saved, since it is saved in memory inside 
        # the `image_stream` stream
        image_stream = capture_image(camera) #Default format: "jpeg"
        n_humans = recognize_humans(image_stream)
        logger.info(f"Humans detected: {n_humans}")

    params = add_metrics(
        [
            temperature, humidity, pressure,
            orientation["pitch"], orientation["roll"], orientation["yaw"],
            accel["x"], accel["y"], accel["z"],
            gyro["x"], gyro["y"], gyro["z"],
            mag["x"], mag["y"], mag["z"],
            motion_detected, n_humans
        ],
        params
    )
    return params

def add_metrics(metrics: list, params: tuple):
    """Add the `metrics` list on params tuple"""
    # `*metrics` is used to unpack the `metrics` list, which means all of its
    # elements are passed as elements of the new tuple on the right side of the +.
    # The comma is necessary to make sure that python reades `(*metrics, )` as a tuple.
    params = params + (*metrics, ) 
    return params

### CONFIGURATION ###
base_folder = Path(__file__).parent.resolve()

# Set a logfile name
logfile(base_folder/"events.log")

# Set up Sense Hat and clear LED Matrix
sense = SenseHat()
sense.clear() 

# Set up camera
cam = PiCamera()
cam.resolution = (1296, 972)
# Set up motion sensor on GPIO pin 12 (Reference: docs)
motion_sensor = MotionSensor(pin=12)

# Initialise the CSV file
data_file = base_folder/"data.csv"
create_csv_file(data_file)

# Initialise the photo counter
counter = 1

# Initialise LED matrix values
current_led = 0 # Led to light up
led_x = 0
led_y = 0

# Initialise the number of iterations before a picture is taken
CAMERA_DELAY = 60

# Record the start and current time
start_time = datetime.now()
now_time = datetime.now()

# How long the experiment should be run.
# In this case, 178 is chosen (instead of 180) in case something goes wrong
# with the timings
TOTAL_MINS = 177

#### MAIN LOOP ####
logger.info("Experiment started")

# Run the main loop for (almost) three hours
while (now_time < start_time + timedelta(minutes=TOTAL_MINS)):
    try:
        # Set LED Matrix. According to the number of measurements, light a different led.
        # The algorithm traverses the entire LED matrix grid.
        if (counter % 10) == 0:
            # Calculate the x and y coordinates for the current_led
            led_y = current_led // 8
            led_x = current_led - 8*led_y
            # Clear the last pixel
            sense.clear()
            # Draw the new pixel
            sense.set_pixel(led_x, led_y, 255, 255, 255)
            # Increment the led counter by 1. There is the modulo operation
            # because there are only 64 leds in the matrix.
            current_led = (current_led + 1) % 64
        
        if (counter % CAMERA_DELAY) == 0:
            # If a photo is taken in this iteration, turn the pixel green
            sense.set_pixel(led_x, led_y, 0, 255, 0)

        # Log event
        logger.info(f"Iteration {counter} started")

        params = ()

        # Get coordinates of location on Earth below the ISS
        location = ISS.coordinates()

        # Detect humans using the human detection function only once
        # every CAMERA_DELAY measurements. 
        detect_humans = False
        if counter % CAMERA_DELAY == 0:
            detect_humans = True

        # Get sensor metrics
        params = add_sensor_metrics(sense, motion_sensor, cam, params, detect_humans)

        # Save the data to the file "jpeg"
        data = (
            counter,
            datetime.now(),
            location.latitude.degrees,
            location.longitude.degrees,
            *params # Unpack the parameter tuple inside the data tuple
        )
        add_csv_data(data_file, data)

        counter += 1

        # Pause the program for 20 ms
        sleep(0.02)

        # Update the current time
        now_time = datetime.now()

    # If an exception is thrown, log it, and continue the experiment
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')

cam.close()
sense.clear()
logger.info(f"Experiment finished successfully!")
