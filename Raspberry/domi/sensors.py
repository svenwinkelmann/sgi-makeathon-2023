from picamera import PiCamera
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
import board
import adafruit_dht
import smbus
import time

#Connect Sensors
#Camera 
#camera = PiCamera()

#Air Temp&Humidity
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

#Earth Humidity
chanel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(chanel, GPIO.IN)

# Brightness Sensor
bus = smbus.SMBus(1)
bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)


def readSensors():
    #Connect Sensors
    #Camera 
    #camera = PiCamera()

    #Air Temp&Humidity
    dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

    #Earth Humidity
    chanel = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(chanel, GPIO.IN)
    #Camera
    #camera.start_preview()
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    #name = "/home/pi/Pictures/{}.jpg".format(ts)
    #camera.capture(name)
    print("Camera on")
    #camera.stop_preview()

    #Air Temp&Humidity
    temperature_c = dhtDevice.temperature
    humidity = dhtDevice.humidity
    print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))


    #Earth Humidit:
    ground_humidity = GPIO.input(chanel)
    print("Earth Humitiy: {}".format(ground_humidity))


    #Brightness Sensor
    # Read data back from 0x0C(12) with command register, 0x80(128), 2 bytes
    # ch0 LSB, ch0 MSB
    data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

    # Read data back from 0x0E(14) with command register, 0x80(128), 2 bytes
    # ch1 LSB, ch1 MSB
    data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

    # Convert the data
    ch0 = data[1] * 256 + data[0]
    ch1 = data1[1] * 256 + data1[0]
    light_intesity = ch0-ch1

    # Output data to screen
    print("Visible Value :%d lux" %(ch0 - ch1))

    return {"Air_Temperature": temperature_c,
            "Air_Humidity": humidity,
            "Ground Humidity": ground_humidity,
            "Light_Intensity": light_intesity
    }



def main():
    test = readSensors()

if __name__ == "__main__":
    main()