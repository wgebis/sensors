import serial
import binascii
import codecs

ser = serial.Serial('/dev/ttyS0') 
r = ser.read(24)
pm1_cf=int.from_bytes(r[4:6], 'big')
pm25_cf=int.from_bytes(r[6:8], 'big')
pm10_cf=int.from_bytes(r[8:10], 'big')
pm1=int.from_bytes(r[10:12], 'big')
pm25=int.from_bytes(r[12:14], 'big')
pm10=int.from_bytes(r[14:16], 'big')

print([pm1_cf, pm25_cf, pm10_cf, pm1, pm25, pm10])

