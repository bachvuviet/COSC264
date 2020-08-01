# Packet Structure (response.py)
# Bach Vu
# 01/08/2020

from packet import *
from datetime import datetime
from language import DT_Language

class DT_Response(DT_Packet):
    def __init__(self, language, mode, time=None):
        super().__init__(0x0002)
        self.languageCode = language
        self.DTlanguage = DT_Language(language, mode) 
        if time == None:
            self.now = datetime.now() # Time when obj created
        else:
            self.now = time
        
    def __repr__(self):
        out = type(self).__name__ + " with response type: {}\n".format(self.languageCode) 
        out += self.DTlanguage.DTtoString(self.now.day, self.now.month, self.now.year, self.now.hour, self.now.minute)
        return out
    
    def isValid(self):
        return True
    
    def header_errorCode(self):
        pass   
    
    def encodePacket(self):
        """ Get the actual bytearray store data of this packet """
        # Error check
        check = self.isValid()
        if check != True:
            return check
        
        # Payload
        payload = bytearray()
        #payload = self.DTlanguage.DTtoString(self.now.day, self.now.month, self.now.year, self.now.hour, self.now.minute)
        #payload = bytearray(payload, 'utf8')
        
        # Header
        header = ""
        header += self.intToBinaryString(self.MagicNum,16)
        header += self.intToBinaryString(self.packetType,16)
        header += self.intToBinaryString(self.languageCode,16)
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
    
    def decodePacket(packet):
        """ Turn bytearray to object """ 
        language = int.from_bytes(packet[4:6], byteorder="big")
        year = int.from_bytes(packet[6:8], byteorder="big")
        month = int.from_bytes(packet[8:9], byteorder="big")
        day = int.from_bytes(packet[9:10], byteorder="big")
        hour = int.from_bytes(packet[10:11], byteorder="big")
        minute = int.from_bytes(packet[11:12], byteorder="big")
        time = datetime(year, month, day, hour, minute, 0, 0)        
        return DT_Response(language, 2, time)