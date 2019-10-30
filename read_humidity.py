import board
import busio
import adafruit_am2320
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_am2320.AM2320(i2c)
print('Humidity = {0} % Temperature = {1}'.format(sensor.relative_humidity,sensor.temperature))
