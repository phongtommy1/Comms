from digi.xbee.models.mode import OperatingMode
from digi.xbee.exception import InvalidOperatingModeException, InvalidPacketException
from digi.xbee.packets.base import XBeeAPIPacket, DictKeys
from digi.xbee.packets.aft import ApiFrameType


class XBeePacket(XBeeAPIPacket):
    def __init__(self, op_mode=OperatingMode.API_MODE):
        """
        Class constructor. Instantiates a new :class:`.XBeePacket` object.

        Args:
            op_mode (:class:`.OperatingMode`, optional, default=`OperatingMode.API_MODE`):
                The mode in which the frame was captured.
        """
        self._op_mode = op_mode
        if op_mode not in (OperatingMode.API_MODE, OperatingMode.ESCAPED_API_MODE):
            self._op_mode = OperatingMode.API_MODE

    @staticmethod
    def create_packet(raw, operating_mode):
        """
        Override method.
        Returns:
            :class:`.ATCommPacket`
        Raises:
            InvalidPacketException: if the bytearray length is less than 8.
                (start delim. + length (2 bytes) + frame type
                + frame id + command (2 bytes) + checksum = 8 bytes).
            InvalidPacketException: if the length field of 'raw' is different
                from its real length. (length field: bytes 2 and 3)
            InvalidPacketException: if the first byte of 'raw' is not the
                header byte. See :class:`.SpecialByte`.
            InvalidPacketException: if the calculated checksum is different
                from the checksum field value (last byte).
            InvalidPacketException: if the frame type is different from
                :attr:`.ApiFrameType.AT_COMMAND`.
            InvalidOperatingModeException: if `operating_mode` is not supported.
        .. seealso::
           | :meth:`.XBeePacket.create_packet`
           | :meth:`.XBeeAPIPacket._check_api_packet`
        """
        if operating_mode not in (OperatingMode.ESCAPED_API_MODE,
                                  OperatingMode.API_MODE):
            raise InvalidOperatingModeException(op_mode=operating_mode)

        XBeeAPIPacket._check_api_packet(
            raw, min_length=XBeePacket.__MIN_PACKET_LENGTH)

        if raw[3] != ApiFrameType.AT_COMMAND.code:
            raise InvalidPacketException(
                message="This packet is not an AT command packet.")

        return XBeePacket(
            raw[4], raw[5:7],
            parameter=raw[7:-
                          1] if len(raw) > XBeePacket.__MIN_PACKET_LENGTH else None,
            op_mode=operating_mode)
