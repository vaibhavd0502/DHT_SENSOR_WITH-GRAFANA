import Adafruit_DHT

class TmpHumSensor:
    def __init__(self, pin) -> None:
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT22

    def getTempHum(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            return {"tmp": temperature, "hum": humidity}
        else:
            return None
