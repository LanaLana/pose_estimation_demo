#!/usr/bin/env python
from flask import Flask, render_template, Response, request, json
import time
# import json

app = Flask(__name__)
TIME_FILE = './time.txt'


def read_txt(file):
    with open(file, 'r') as f:
        t = f.read()
        return t
        
        
def write_txt(file, text):
    with open(file, 'w') as f:
        f.write(text)
        
        
def read_json(file):
    with open(file, 'r') as f:
        t = json.load(f)
        return t


class Camera(object):
    def __init__(self):
        filenames = []
        for i in range(5003):
            filenames += ['frames_with_pose/frame_{}.jpg'.format(i)]
        self.frames = [open(frame, 'rb').read() for frame in filenames]

    def get_frame(self):
        time.sleep(1 / 25)
        t = int(read_txt(TIME_FILE))
        write_txt(TIME_FILE, str((t + 1) % len(self.frames)))
        return self.frames[t % len(self.frames)]
    
    
class Camera2(object):
    def __init__(self):
        filenames = []
        for i in range(5003):
            filenames += ['concatenated_frames/frame_{}.jpg'.format(i)]
        self.frames = [open(frame, 'rb').read() for frame in filenames]
        self.last_t = 0

    def get_frame(self):
        try:
            time.sleep(1 / 25)
            t = int(read_txt(TIME_FILE))
            self.last_t = t
    #         write_txt(TIME_FILE, str((t + 1) % len(self.frames)))
            return self.frames[t % len(self.frames)]
        except:
            return self.frames[self.last_t % len(self.frames)]
    
        
@app.route('/')
def index():
#     print(app.root_path)
    write_txt(TIME_FILE, '0')
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/image_feed')
def image_feed():
    return Response(gen(Camera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/get_data", methods=['GET', 'POST'])
def get_data():
    t = read_txt(TIME_FILE)
    p = read_json('pose_estimation.json')
    return p[t]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
