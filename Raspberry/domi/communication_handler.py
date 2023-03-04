from flask import Flask, jsonify
import time
# from sensors import readSensors
import requests
import threading
import json

app = Flask(__name__)

# init
backend_ip = '127.0.0.1'

#

"""
GLOBAL FUNCTIONS:
"""


def send_data_to_back_end():
    """
    test_data
    """
    time.sleep(20)
    test_measurements = {
        "plant_id": 2,
        "sensordata_temp": 3,
        "sensordata_humidity": 4,
        "pest_infestation": 5,
        "light_intensity": 6
    }

    requests.post(f"http://{backend_ip}:5000/drive/result/1", json=test_measurements)


"""
SENSOR TEST FUNCTION
"""


@app.route("/measurement_test", methods=['GET'])
def measurement_test():
    pass
    # return readSensors()


"""

"""


@app.route("/drive/<int:plant_id>", methods=['GET'])
def drive_plant_raspi(plant_id):
    t = threading.Thread(target=send_data_to_back_end)
    t.start()
    return jsonify({"Success": True})


@app.route("/move/<position>", methods=['POST'])
def post_move(position):
    if position == 'plant1':
        return f"I moved to position: {position}"
    # control motors or whatever you like
    return f"Somewhere moved, no idea where to: {position}"


"""@app.route("/all", methods=['GET'])
def get_all():
    # read sensor data
    # TODO
    time.sleep(10)
    # put sensor data into a dict
    ret = {
        "plant_id": 1,
        "sensordata_temp": 20.5,
        "sensordata_humidity": 23.5
    }

    # return it as json data
    return ret"""

app.run(host='127.0.0.1', port=20000)
