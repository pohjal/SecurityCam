from flask import Flask
import picamera
import time

app = Flask(__name__)

@app.route('/start-video')
def start_video():
    try:
        camera = picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 30
        camera.start_recording('/home/leevi/SecurityCam/back-end/venv/data/video.h264')
        return "Video recording started"
    except Exception as e:
        return f"Error starting video recording: {str(e)}"

@app.route('/stop-video')
def stop_video():
    try:
        camera = picamera.PiCamera()
        camera.stop_recording()
        camera.close()
        return "Video recording stopped"
    except Exception as e:
        return f"Error stopping video recording: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
