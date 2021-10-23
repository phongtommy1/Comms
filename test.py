from digi.xbee.devices import XBeeDevice
from digi.xbee.packets.base import XBeePacket
from digi.xbee.models.mode import OperatingMode
import struct

device1 = XBeeDevice("COM5", 9600)
device1.open()

# device1.send_data_broadcast("Hello")

# device1.close()

# data = struct.pack("2i?", 40, 26, True)
data = [2,3,4]
byte_array = bytearray(data)
print(byte_array)
# opMode = OperatingMode.ESCAPED_API_MODE

# packet = XBeePacket.create_packet(byte_array, opMode)

# cSum = packet.get_checksum()

#print(cSum)
