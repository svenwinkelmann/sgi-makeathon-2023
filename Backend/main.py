# create by caliskan
# backend
#
from flask import Flask, jsonify, request
from plantdatabase import PlantDataBase
import requests
from http import HTTPStatus

# init #
database = PlantDataBase()
database.create_table()
host_ip = '127.0.0.1'
port = 5000
rapi_ip = '192.168.0.106'
app = Flask(__name__)
robot_available = True
task_id = [1]
# init end #


@app.route("/drive/task/<int:task_id>", methods=['POST'])
def receive_task_data():
    """
    Use this Method for new data from Raspi with specific task_id
    :return: 200 if data was correct transmitted
    """
    json_data = request.get_json()
    return 200


@app.route("/drive/status", methods=['GET'])
def robot_status():
    return jsonify({"available": robot_available is not robot_available})


@app.route("/data/<int:plant_id>")
def get_data(plant_id):
    return jsonify(database.get_latest_data(plant_id=plant_id))


# If Drive command, send to Raspi
@app.route("/drive/<int:plant_id>", methods=['GET'])
def drive_task(plant_id):
    pass


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
