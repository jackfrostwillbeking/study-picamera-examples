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
import numpy as np
import cv2
import time

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

app = Flask(__name__)

# video_camera = VideoCamera(flip=False)
class Const(object):
    CAMERA_DEMO = os.getenv('CAMERA_DEMO', 'Cannot load the env')
    message = CAMERA_DEMO
    app.jinja_env.globals.update(message)


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
#         frame = camera.get_frame()
        frame = get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def get_frame():
    camera.capture(rawCapture, format="bgr", use_video_port=True)
    frame = rawCapture.array
    decoded_objs = decode(frame)
    frame = display(frame, decoded_objs)
    ret, jpeg = cv2.imencode('.jpg', frame)
    rawCapture.truncate(0)

    return jpeg.tobytes()

def decode(frame):
    decoded_objs = pyzbar.decode(frame, scan_locations=True)
    for obj in decoded_objs:
        print(datetime.now().strftime('%H:%M:%S.%f'))
        print('Type: ', obj.type)
        print('Data: ', obj.data)
    
    return decoded_objs

def display(frame, decoded_objs):
    for decoded_obj in decoded_objs:
        left, top, width, height = decoded_obj.rect
        frame = cv2.rectangle(frame,
                              (left, top),
                              (left + width, height + top),
                              (0, 0, 255), 2)
    return frame
        
# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(video_camera),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)

