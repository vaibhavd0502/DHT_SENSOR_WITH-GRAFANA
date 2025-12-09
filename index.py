from tmpHumDb import TmpHumDb
from tmpHumSensor import TmpHumSensor

sensorId = "s1"  # Unique ID for your sensor
tmpHumDb = TmpHumDb(
    hostStr="localhost",  # Update with your details
    dbPort=5432,
    dbStr="postgres",
    uNameStr="postgres",
    dbPassStr="Password@12345"
)
sensor = TmpHumSensor(pin=18)

tmpHumDict = sensor.getTempHum()
if tmpHumDict is None:
    print("Error retrieving temp hum from sensor")
    exit(0)

tmpHumDb.insertData(tmpHumDict["tmp"], tmpHumDict["hum"], sensorId)
print("Data logged successfully!")
