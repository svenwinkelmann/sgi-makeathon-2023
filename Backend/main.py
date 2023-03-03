# create by caliskan
# backend
#
from flask import Flask, jsonify, request
from plantdatabase import PlantDataBase
import requests

# init #
database = PlantDataBase()
database.create_table()
host_ip = '127.0.0.1'
port = 5000
raspi_ip = '192.168.0.106'
app = Flask(__name__)
ROBOT_STATUS = True
DATA_AVAILABLE = False
PLANT_NUM = 6
# init end #

"""
GLOBAL FUNCTIONS:
"""


def change_robot_state(s: bool):
    global ROBOT_STATUS
    ROBOT_STATUS = s


"""
RASPI RESPONSE:
"""


@app.route("/drive", methods=['POST'])
def raspi_response():
    response_json = request.get_json()
    change_robot_state(True)
    for i in range(5):
        database.insert_measurement_data(response_json[i]['plant_id'],
                                         response_json[i]['sensordata_temp'],
                                         response_json[i]['sensordata_humidity'])


@app.route("/measurement_test", methods=['GET'])
def measurement_test():
    response = requests.get(f"http://{raspi_ip}:{port}/measurement_test")
    response_json = response.json()
    return jsonify(response_json)




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


@app.route("/drive", methods=['GET'])
def drive_all_plants():
    if not ROBOT_STATUS:
        return
    requests.get(f"http://{raspi_ip}:{port}/all")
    change_robot_state(False)


@app.route("/drive/<int:plant_id>", methods=['GET'])
def drive_plant(plant_id):
    if not ROBOT_STATUS:
        return
    requests.get(f"http://{raspi_ip}:{port}/drive/{plant_id}")
    change_robot_state(False)


@app.route("/data", methods=['GET'])
def get_data():
    """
    FROM FE -> command to give latest data -> returns latest data
    :param plant_id:
    :return:
    """
    data_list = []
    for i in range(6):
        data_list.append(database.get_latest_data(plant_id=(i + 1)))
    print(data_list)
    complete_json = {"plants":data_list, "robot_status":ROBOT_STATUS}
    return jsonify(complete_json)


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
