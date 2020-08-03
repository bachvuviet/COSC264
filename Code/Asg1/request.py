# Packet Structure (request.py)
# Bach Vu
# 01/08/2020

from packet import *

class DT_Request(DT_Packet):
    def __init__(self, mode):
        super().__init__(0x0001) 
        self.requestType = mode # 0x0001 or 0x0002
        
    def __repr__(self):
        return type(self).__name__ + " with request type: {} ".format(self.requestType)     
    
    def header_errorCode(self):
        error_code = 0
        if self.MagicNum != 0x497E:
            error_code = 1
        elif self.packetType != 0x0001:
            error_code = 2
        elif self.requestType < 0x0001 or self.requestType > 0x0002:
            error_code = 3
            
        return error_code
    
    def encodePacket(self):
        # Error check
        check = self.isValid()
        if check != True:
            return check
        
        # Header
        header = ""
        header += self.intToBinaryString(self.MagicNum,16)
        header += self.intToBinaryString(self.packetType,16)
        header += self.intToBinaryString(self.requestType,16)
        header = int(header, 2).to_bytes(6, byteorder='big')
        
        # Pack
        packet = bytearray()
        packet += header
        return packet
    
    @staticmethod
    def decodePacket(packet):        
        mode = int.from_bytes(packet[4:], byteorder="big")
        requestPack = DT_Request(mode)

        # Error check
        check = requestPack.isValid()
        if check != True:
            return check        
        return requestPack
