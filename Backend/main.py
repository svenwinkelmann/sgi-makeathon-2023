# create by caliskan
# backend
#
from flask import Flask, jsonify, request
from plantdatabase import PlantDataBase
import requests
import threading

# init #
database = PlantDataBase()
database.create_table()
host_ip = '192.168.0.110'
port = 5000
raspi_ip = '192.168.0.106'
app = Flask(__name__)
ROBOT_AVAILABLE = True
DATA_AVAILABLE = False
TASK_ID = 0
# init end #

"""
GLOBAL FUNCTIONS:
"""


def increment_task_if():
    global TASK_ID
    TASK_ID += 1


def change_robot_state(s: bool):
    global ROBOT_AVAILABLE
    ROBOT_AVAILABLE = s


"""
RASPI RELATED:
"""


# If drive command, send to Raspi


@app.route("/drive/task/<int:raspi_task_id>", methods=['POST'])

"""
def receive_task_data(raspi_task_id):
    
    FROM RASPI -> GET DATA -> insert in database -> send it to FE
    :return: 200 if data was correct transmitted
    
    response_json = request.get_json()
    database.insert_measurement_data(response_json['plant_id'],
                                     response_json['sensordata_temp'],
                                     response_json['sensordata_humidity'])
    database.get_latest_data(response_json['plant_id'], task_id=raspi_task_id)
    change_robot_state(True)"""


"""
FRONTEND RELATED:
"""


@app.route("/drive/<int:plant_id>", methods=['GET'])
def drive_task(plant_id):
    """
    FROM FE -> drive command
    :param plant_id:
    """
    increment_task_if()
    requests.get(f"http://{raspi_ip}:{port}/{TASK_ID}")
    change_robot_state(False)


@app.route("/data/<int:plant_id>")
def get_data(plant_id):
    """
    FROM FE -> command to give latest data -> returns latest data
    :param plant_id:
    :return:
    """
    return jsonify(database.get_latest_data(plant_id=plant_id, task_id=TASK_ID))


@app.route("/drive/status", methods=['GET'])
def robot_status():
    """
    FROM FE -> returns, if roboter available
    :return:
    """
    return jsonify({"available": ROBOT_AVAILABLE})


"""def drive_to_plant(plant_id):
    response = requests.get(f"http://{rapi_ip}:{port}/all")  # Will hopefully wait till data arrives
    if response.status_code != HTTPStatus.OK:  # Return False if not successfully
        return False
    response_json = response.json()
    database.insert_measurement_data(response_json['plant_id'],
                                     response_json['sensordata_temp'],
                                     response_json['sensordata_humidity'])
    return jsonify(database.get_latest_data(plant_id=plant_id))"""

if __name__ == "__main__":
    app.run(host=host_ip, port=port, debug=True)
