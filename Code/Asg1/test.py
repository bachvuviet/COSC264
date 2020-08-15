# Testing only (test.py)
# Bach Vu
# 08/08/2020

import datetime
from socket import *

test_Socket = socket(AF_INET, SOCK_DGRAM)
test_Socket.setblocking(0)

def test_decodeRequest():
    # Just run test to send fault request to server
    target = ('127.0.1.1', 63999)
    testPack = bytearray(b'I~\x00\x01\x00\x01') # Correct
    test_Socket.sendto(testPack, target)
    testPack = bytearray(b'I~\x00\x01\x00\x02') # Correct
    test_Socket.sendto(testPack, target)
    testPack = bytearray(b'I~\x00\x01\x00\x03') # Incorrect requestType
    test_Socket.sendto(testPack, target)
    testPack = bytearray(b'I~\x00\x02\x00\x02') # Incorrect packetType
    test_Socket.sendto(testPack, target)
    testPack = bytearray(b'E`\x00\x02\x00\x02') # Incorrect magicNum
    test_Socket.sendto(testPack, target)
    testPack = bytearray(b'I~\x00\x01\x00') # Incorrect packet size
    test_Socket.sendto(testPack, target)

def test_decodeResponse():
    # Disable socket sending of server
    # Adjust client wait time to 1000, request like normal, 
    # get ip and port from server, then use test.py to send message to that client

    target = ('127.0.0.1', 57979)
    testPack = bytearray(b'I~\x00\x02\x00\x03\x07\xe4\x08\x0f\x12+\x15Die Uhrzeit ist 18:43') # Correct sample
    # testPack = bytearray(b'I~\x00\x01\x00') # Incorrect packet size
    # testPack = bytearray(b'I~\x00\x02\x00\x03\x07\xe4\x08\x0f\x12+\x15Die Uhrzeit ist 18:4') # Incorrect message len
    # testPack = bytearray(b'I~\x00\x02\x00\x03\x07\xe4\x08\x0f\x12+\x15Die Uhrzeit ist 18:43') # Incorrect packet size
    # testPack = bytearray(b'I~\x00\x02\x00\x03\x07\xe4\x08\x0f\x12+\x15Die Uhrzeit ist 18:43') # Incorrect packet size
    # testPack = bytearray(b'I~\x00\x02\x00\x03\x07\xe4\x08\x0f\x12+\x15Die Uhrzeit ist 18:43') # Incorrect packet size
    # testPack = bytearray(b'I~\x00\x02\x00\x03\x07\xe4\x08\x0f\x12+\x15Die Uhrzeit ist 18:43') # Incorrect packet size
    test_Socket.sendto(testPack, target)

if __name__ == "__main__":
    # test_decodeRequest()
    test_decodeResponse()

