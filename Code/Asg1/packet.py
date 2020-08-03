# Packet Interface (packet.py)
# Bach Vu
# 01/08/2020

from abc import abstractmethod

class DT_Packet:
    def __init__(self, packetType):        
        self.MagicNum = 0x497E
        self.packetType = packetType
    
    def intToBinaryString(self, decimal, str_len):
        return bin(decimal)[2:].zfill(str_len)

    @abstractmethod   
    def __repr__(self):
        """ Output log """  
        
    def isValid(self):
        """ Check conditions of a Packet Type """
        error_code = self.header_errorCode()
        if error_code != 0:
            return error_code        
        return True
        
    @abstractmethod
    def header_errorCode(self):
        """ Check conditions of a Packet header """    
     
    @abstractmethod   
    def encodePacket(self):
        """ Get the actual bytearray store data of this packet """
     
          
    


    
