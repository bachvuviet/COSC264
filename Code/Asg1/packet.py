# Packet Interface (packet.py)
# Bach Vu
# 01/08/2020

from abc import abstractmethod

class DT_Packet:
    def __init__(self, packetType):        
        self.MagicNum = 0x497E
        self.packetType = packetType

    @staticmethod
    def intToBinStr(decimal, str_len):
        return bin(decimal)[2:].zfill(str_len)  
        
    @staticmethod
    def byteArrToInt(byte):
        return int.from_bytes(byte, byteorder="big")

    def isValid(self):
        """ Check conditions of a Packet Type """
        return self.header_errorCode()

    @abstractmethod   
    def __repr__(self):
        """ Output log """
        
    @abstractmethod
    def header_errorCode(self):
        """ Check conditions of a Packet Type """    
     
    @abstractmethod   
    def encodePacket(self):
        """ Get the actual bytearray store data of this packet """
        
    @abstractmethod
    def decodePacket(packet):
        """ Turn bytearray to object """   
          
    


    
