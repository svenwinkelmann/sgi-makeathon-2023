from flask import Flask
import time
from sensors import readSensors
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "<p>Hello, World!</p>"

"""
SENSOR TEST FUNCTION
"""

@app.route("/measurement_test", methods=['GET'])
def measurement_test():
    return readSensors()

"""

"""
@app.route("/temp/<int:sensor_id>", methods=['GET'])
def get_temperature(sensor_id):
    if sensor_id == 1:
        # here we need to read our sensor values
        return "23.4"
    elif sensor_id == 2:
        return "21.0"
    else:
        return "not found"


@app.route("/move/<position>", methods=['POST'])
def post_move(position):
    if position == 'plant1':
        return f"I moved to position: {position}"
    # control motors or whatever you like
    return f"Somewhere moved, no idea where to: {position}"


@app.route("/all", methods=['GET'])
def get_all():
    # read sensor data
    # TODO
    time.sleep(10)
    # put sensor data into a dict
    ret = {
        "plant_id": 1,
        "sensordata_temp":20.5,
        "sensordata_humidity": 23.5
    }

    # return it as json data
    return ret

app.run(host='192.168.0.106', port=5000)
