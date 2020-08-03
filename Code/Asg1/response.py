# Packet Structure (response.py)
# Bach Vu
# 01/08/2020

from packet import *
from datetime import datetime
from language import DT_Language

class DT_Response(DT_Packet):
    def __init__(self, language, mode, time=None):
        super().__init__(0x0002) 
        self.language = language
        if time == None:
            self.now = datetime.now() # Time when obj created
        else:
            self.now = time
        self.DTlanguage = DT_Language(language, mode, self.now)
        
    def __repr__(self):
        return type(self).__name__ + ":" 
    
    def getDT_str(self):
        return self.DTlanguage.DTtoString()
        
    def header_errorCode(self):
        error_code = 0
        if self.MagicNum != 0x497E:
            error_code = 1
        elif self.packetType != 0x0002:
            error_code = 2
        elif self.language < 0x0001 or self.language > 0x0003:
            error_code = 3
        elif self.now.year < 0 or self.now.year > 2100:
            error_code = 4
        elif self.now.month < 1 or self.now.month > 12:
            error_code = 5
        elif self.now.day < 1 or self.now.day > 31:
            error_code = 6
        elif self.now.hour < 0 or self.now.hour > 23:
            error_code = 7
        elif self.now.minute < 0 or self.now.minute > 59:
            error_code = 8        
            
        return error_code
    
    def encodePacket(self):
        """ Get the actual bytearray store data of this packet """
        # Error check
        check = self.isValid()
        if check != True:
            return check
        
        # Payload
        payload = bytearray()
        #payload = bytearray(payload, 'utf8')
        
        # Header
        header = ""
        header += self.intToBinaryString(self.MagicNum,16)
        header += self.intToBinaryString(self.packetType,16)
        header += self.intToBinaryString(self.language,16)
        header += self.intToBinaryString(self.now.year,16)
        header += self.intToBinaryString(self.now.month,8)
        header += self.intToBinaryString(self.now.day,8)
        header += self.intToBinaryString(self.now.hour,8)
        header += self.intToBinaryString(self.now.minute,8)
        header += self.intToBinaryString(0,8)
        header = int(header, 2).to_bytes(13, byteorder='big')
        
        
        # Pack
        packet = bytearray()
        packet += header
        packet += payload
        return packet        
    
    @staticmethod
    def decodePacket(packet, mode):        
        """ Turn bytearray to object """        
        language = int.from_bytes(packet[4:6], byteorder="big")
        year = int.from_bytes(packet[6:8], byteorder="big")
        month = int.from_bytes(packet[8:9], byteorder="big")
        day = int.from_bytes(packet[9:10], byteorder="big")
        hour = int.from_bytes(packet[10:11], byteorder="big")
        minute = int.from_bytes(packet[11:12], byteorder="big")
        time = datetime(year, month, day, hour, minute, 0, 0)

        # Error check
        responsePack = DT_Response(language, mode, time)
        check = responsePack.isValid()
        if check != True:
            return check        
        return responsePack