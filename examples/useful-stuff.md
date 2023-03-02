# Some useful stuff

## GIT
- Command line tool: https://git-scm.com/
- Useful commands: https://www.syncfusion.com/blogs/post/top-10-git-commands-every-developer-should-know.aspx
- Nice GUI: https://www.sourcetreeapp.com/

## Python 

### Python Virtual Environments
Create Virtual Environment:
	```python -m venv .venv```

Activate VE:

- ```.venv/Scripts/activate.bat``` (Win CMD)
- ```.venv/Scripts/activate.ps1``` (Win PS)
- ```source .venv/bin/activate``` (Linux/mac bash)

Deactivate VE:
- ```.venv/Scripts/deactivate.bat``` (Win CMD)
- ```.venv/Scripts/deactivate.ps1``` (Win PS)
- ```deactivate``` (Linux/mac bash)

Install requirements.txt:
```pip install -r requirements.txt```

Freeze requirements
```pip freeze > requirements.txt```

### Python Flask
https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application

```flask --app python-flask-server run``` to run server on localhost
```flask --app python-flask-server run --host=192.168.1.x``` to define own host


To send requests to your service, https://www.postman.com/downloads/ is a good application.

## MQTT
- https://www.youtube.com/watch?v=EIxdz-2rhLs&ab_channel=RuiSantos
- MQTT Explorer: https://mqtt-explorer.com/
- MQTT Broker: https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/
- Maybe this tool could be helpful to manage the logic: https://nodered.org/
- how we can use MQTT with Arduino IDE: https://randomnerdtutorials.com/esp32-mqtt-publish-subscribe-arduino-ide/

## Matter
- https://github.com/project-chip/connectedhomeip
- https://blog.espressif.com/announcing-matter-previously-chip-on-esp32-84164316c0e3