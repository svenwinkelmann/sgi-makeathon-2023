#! /bin/bash
cd Makeathon/
source .venv/bin/activate
cd Backend/
flask --app python-flask-server run --host=192.168.0.102
