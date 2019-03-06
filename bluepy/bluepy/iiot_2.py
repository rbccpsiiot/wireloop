import sys
import struct
import time
from bluepy.btle import Peripheral, UUID, DefaultDelegate

def _TI_UUID(val):
    return UUID("%08X-0451-4000-b000-000000000000" % (0xF0000000+val))

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        #for i in range(0,15):
	#	sys.stdout.write(((data[i])))
	#	sys.stdout.write(',')	
	print ' '.join("{:02x}".format(ord(c)) for c in data)	
	sys.stdout.flush()

if __name__ == '__main__':
    iiot_uuid = UUID(0x2800)

p = Peripheral("24:71:89:1A:A9:27")
p.setDelegate(MyDelegate())

data_UUID  = _TI_UUID(0xAA00)
sensor_UUID = _TI_UUID(0xAA01)
timestamp_UUID = _TI_UUID(0xAA02)
conf_UUID = 0x2902


data_service=p.getServiceByUUID(data_UUID)
print data_service

sensor_characteristic = data_service.getCharacteristics(sensor_UUID)
print sensor_characteristic

timestamp_characteristic = data_service.getCharacteristics(timestamp_UUID)
print timestamp_characteristic

data_descriptor = p.getDescriptors(data_service.hndStart, data_service.hndEnd)
timestamp_desc, = [timestamp_desc for timestamp_desc in data_descriptor if timestamp_desc.uuid==timestamp_UUID] 
print timestamp_desc

conf_desc, = [conf_desc for conf_desc in data_descriptor if conf_desc.uuid==conf_UUID] 
print conf_desc

sensor_desc, = [sensor_desc for sensor_desc in data_descriptor if sensor_desc.uuid==sensor_UUID]
print sensor_desc 

p.writeCharacteristic(conf_desc.handle,struct.pack('bb',0x01,0x00))
time.sleep(1)
p.writeCharacteristic(timestamp_desc.handle,'0')
time.sleep(1)
p.writeCharacteristic(timestamp_desc.handle,'0')
time.sleep(1)
p.writeCharacteristic(timestamp_desc.handle,'0')
time.sleep(1)
p.writeCharacteristic(timestamp_desc.handle,'0')
time.sleep(1)
p.writeCharacteristic(timestamp_desc.handle,'0')
time.sleep(1)
print("Connected")
p.writeCharacteristic(conf_desc.handle,struct.pack('bb',0x01,0x00))
if p.waitForNotifications(5.0):
	print "Data Received"
	#handleNotification() was called
