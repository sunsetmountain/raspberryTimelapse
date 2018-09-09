from time import sleep
import picamera

WAIT_TIME = 10

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    for filename in camera.capture_continuous('/home/pi/timelapse/img{timestamp:%D-%m-%y_%H-%M-%S}.jpg'):
        sleep(WAIT_TIME)
