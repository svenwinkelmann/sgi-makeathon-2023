# create by caliskan
# backend
#
from flask import Flask
from plantdatabase import PlantDataBase

database = PlantDataBase()
database.create_table()

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    database.delete_data("plants")
