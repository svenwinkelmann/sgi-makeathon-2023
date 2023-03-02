# create by caliskan
# backend
#
from flask import Flask
from plantdatabase import PlantDataBase
import requests

database = PlantDataBase()
database.create_table()

app = Flask(__name__)


def request_data(plant_id: str):
    requests.get(url=f"http://192.168.0.XX:XXX/{plant_id}")


@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/plant/<str:plant_id>", methods=['GET'])
def get_plant_data(plant_id):
    request_data(plant_id=plant_id)


if __name__ == "__main__":
    app.run(host='192.168.0.102', port=5000, debug=True)
