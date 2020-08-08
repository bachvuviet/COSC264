# Packet Structure (request.py)
# Bach Vu
# 01/08/2020

from packet import *

class DT_Request(DT_Packet):
    ErrorMessage = [
        "Expecting received packet have MagicNum 0x497E.",
        "Expecting received packet have packetType 0x0001.",
        "Undefined outupt Type [date/time]?",
        "Packet header is shorter than expected"
    ]    
    def __init__(self, mode):
        super().__init__(0x0001) 
        self.requestType = mode # 0x0001 or 0x0002
        
    def __repr__(self):
        return type(self).__name__ + " with request type: " + ("DATE" if self.requestType==1 else "TIME")
    
    def header_errorCode(self):
        error_code = 0
        if self.MagicNum != 0x497E:
            error_code = 1
        elif self.packetType != 0x0001:
            error_code = 2
        elif self.requestType < 0x0 or self.requestType > 0x0002:
            error_code = 3
            
        return error_code
    
    def encodePacket(self):
        # Error check
        check = self.isValid()
        if check != 0:
            return check
        
        # Header
        header = ""
        header += DT_Packet.intToBinStr(self.MagicNum,16)
        header += DT_Packet.intToBinStr(self.packetType,16)
        header += DT_Packet.intToBinStr(self.requestType,16)
        header  = int(header, 2).to_bytes(6, byteorder='big')
        
        # Pack
        packet = bytearray()
        packet += header
        #packet += payload
        return packet
    
    @staticmethod
    def decodePacket(packet):
        if len(packet) < 6:
            return 4        
        mode = DT_Packet.byteArrToInt(packet[4:])
        requestPack = DT_Request(mode)

        # Error check
        check = requestPack.isValid()
        if check != 0:
            return check        
        return requestPack
