from flask import Flask, render_template, Response
from processor.simple_streamer import SimpleStreamer as VideoCamera
# from processor.pedestrian_detector import PedestrianDetector as VideoCamera
#from processor.motion_detector import MotionDetector as VideoCamera
import time
import threading
import os

from pyzbar import pyzbar
from picamera.array import PiRGBArray
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

# video_camera = VideoCamera(flip=False)


app = Flask(__name__)

@app.route('/')
def index():
#     CAMERA_DEMO = os.getenv('CAMERA_DEMO', 'Cannot load the env')
#     message = CAMERA_DEMO
#     return render_template('index.html', message=message)
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# def gen(camera):
def gen():
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)

