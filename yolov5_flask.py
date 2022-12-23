from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello!!"


@app.route("/detectid", methods=['GET'])
def openwebcam():
    os.system("python yolov5/detect.py --source 0 --weights best.pt --conf 0.4 --save-crop")
    return "done"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
