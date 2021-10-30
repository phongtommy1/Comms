from digi.xbee.devices import XBeeDevice
from XBeePacket import XBeePacket
from digi.xbee.models.mode import OperatingMode

device1 = XBeeDevice("COMS", 9600)
device1.open()

device1.send_data_
opMode = OperatingMode.ESCAPED_API_MODE
packets = XBeePacket()
packets.create_packet(, opMode)
