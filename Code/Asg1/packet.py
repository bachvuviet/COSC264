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
        
    @abstractmethod
    def isValid(self):
        """ Check conditions of a Packet Type """
        
    @abstractmethod
    def header_errorCode(self):
        """ Check conditions of a Packet Type """    
     
    @abstractmethod   
    def encodePacket(self):
        """ Get the actual bytearray store data of this packet """
        
    @abstractmethod
    def decodePacket(packet):
        """ Turn bytearray to object """   
          
    


    
