# Client Application (client.py)
# Bach Vu
# 01/08/2020

from packet import *
from request import *
from response import *
from socket import *

class DTClient():
    def __init__(self, target):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.target = target
        
    def postRequest(self, request):
        packet = request.encodePacket()
        if isinstance(packet, bytearray):
            self.socket.sendto(packet, self.target)
            print("Request sent success! Waiting for response ... ")
        else:
            print("Request sent failed with code {}! Try again ... ".format(packet))
        
    def getResponse(self):
        response = None
        while response == None:
            data, addr = self.socket.recvfrom(1024) # in byte
            if addr == None:
                time.sleep(1.0) # in sec
                continue
    
def main():
    print("Welcome to DT Finder (Client)")
    DT_Client = DTClient(('127.0.0.1',5000))
    while True:
        message = input("""
Option:
        Find Server Time: 1
        Find Server date: 2
        Exit: X
Choice: """)
        if message == 'X':
            break
        elif message != '1' and message != '2':
            print("Unknown choice. Please try again")
            continue
        
        #request = DT_Request(int(message))
        request = DT_Response(1, 1) # date in Eng
        DT_Client.postRequest(request)  
        #DT_Client.getResponse()
    print("Seee you again!")

if __name__ == "__main__":
    main()