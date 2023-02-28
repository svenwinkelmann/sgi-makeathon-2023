from flask import Flask

app = Flask(__name__)
#Test Comment caliskan
#second comment
#third comment

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "<p>Hello, World!</p>"


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

    # put sensor data into a dict
    ret = {
        "temp":
        {
            "1": 25.5,
            "2": 24.3,
            "3": 19,
            "format": "C"
        },
        "humidity":
        {
            "1": 45
        }
    }

    # return it as json data
    return ret
