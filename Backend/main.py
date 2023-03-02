# create by caliskan
# backend
#
from flask import Flask
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
# init end #


# If Drive command, send to Raspi
@app.route("/drive/<int:plant_id>", methods=['GET'])
def drive_to_plant(plant_id):
    response = requests.get(f"http://{rapi_ip}:{port}/all")  # Will hopefully wait till data arrives
    response_json = response.json()
    database.insert_measurement_data(response_json['plant_id'],
                                     response_json['sensordata_temp'],
                                     response_json['sensordata_humidity'])
    return database.get_latest_data(plant_id=plant_id)


if __name__ == "__main__":
    app.run(host=host_ip, port=port, debug=True)
