### Control commands:
# 
# 1. Reading status(reading the satus of the relay (on/off))
# 0x55  0x56  0x00  0x00  0x00  0x00  0x00  0xAB
#  
# 2.Relay open (issue this command,Relay open,COM connect to NO)
# Channel 1 : 0x55  0x56  0x00  0x00  0x00  0x01  0x01  0xAD
# Channel 2 : 0x55  0x56  0x00  0x00  0x00  0x02  0x01  0xAE
#  
# 3. Relay close (issue this command,Relay close,COM disconnect NO,and COM connect to NC)
# Channel 1 : 0x55  0x56  0x00  0x00  0x00  0x01  0x02  0xAE
# Channel 2 : 0x55  0x56  0x00  0x00  0x00  0x02  0x02  0xAF
#  
# 4. Relay toggle(Relay status reversal,if COM connect to NO,this commands will Disconnect COM to NO and Reverse COM connect to NC,and vice versa)
# Channel 1 : 0x55  0x56  0x00  0x00  0x00  0x01  0x03  0xAF
# Channel 2 : 0x55  0x56  0x00  0x00  0x00  0x02  0x03  0xB0
#  
# 5. Relay momentary(Relay COM connect to NO,disconnect after 200MS)
# Channel 1 : 0x55  0x56  0x00  0x00  0x00  0x01  0x04  0xB0
# Channel 2 : 0x55  0x56  0x00  0x00  0x00  0x02  0x04  0xB1
# 
# Once issue a command,will have a return fame,7th byte of return fame mean the satus of realy.
# 
### Return command 
#  
# 1.Return relay open(return this command,mean COM connect to NO)
# Channel 1 :  0x33  0x3C  0x00  0x00  0x00  0x01  0x01  0x71
# Channel 2 :  0x33  0x3C  0x00  0x00  0x00  0x02  0x01  0x72
#  
# 2.Return relay close(return this command,mean COM disconnect NO , and COM connect to NC)
# Channel 1 : 0x33  0x3C  0x00  0x00  0x00  0x01  0x02  0x72
# Channel 2 : 0x33  0x3C  0x00  0x00  0x00  0x02  0x02  0x73

import time
import serial

ser = serial.Serial(port='/dev/ttyUSB1')

command = b'\x55\x56\x00\x00\x00\x01\x04\xB0'
ser.write(command)
time.sleep(1)

#command = b'\x55\x56\x00\x00\x00\x02\x04\xB1'
#ser.write(command)
#time.sleep(1)

ser.close()
