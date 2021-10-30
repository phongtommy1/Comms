import struct
from xbee.python2to3 import byteToInt, intToByte


class APIFrame:

    def __init__(self, data=b'', escaped=False):
        self.data = data
        self.raw_data = b''
        self.escaped = escaped
        self._unescape_next_byte = False

    def checksum(self):
        total = 0

        for byte in self.data:
            total += byteToInt(byte)

        total = total & 0xFF

        return intToByte(0xFF - total)

    def verify(self, checksum):
        total = 0

        # Add together all bytes
        for byte in self.data:
            total += byteToInt(byte)

        # Add checksum too
        total += byteToInt(chksum)

        # Only keep low bits
        total &= 0xFF

        # Check result
        return total == 0xFF
