from flask import Flask
import picamera


app = Flask(__name__)
camera = picamera.PiCamera()


@app.route('/start-video')
def start_video():
    camera.start_recording('/path/to/video.h264')
    return "Video recording started"


@app.route('/stop-video')
def stop_video():
    camera.stop_recording()
    return "Video recording stopped"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
