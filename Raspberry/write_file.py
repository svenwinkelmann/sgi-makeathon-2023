import random
import datetime

f = open("test2.txt", "w")
f.write("Temp: {}\n".format(random.randint(0, 10)))
f.write("Humidity: {}\n".format(random.randint(0, 10)))
f.write("Timestamp: {}".format(datetime.datetime.now()))

f.close()