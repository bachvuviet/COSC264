# Server Application (server.py)
# Bach Vu
# 01/08/2020

from packet import *
from request import *
from response import *
from socket import *
import time

class DTServer():
    def __init__(self, ip, ports):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind((ip, ports[0]))
        self.hostIP = ip
        print("Server started on {}:{}".format(ip, ports[0]))
        #for port in ports:

    def getRequest(self):
        data, addr = self.socket.recvfrom(1024) # in byte
        return data, addr        
    
def mainloop():
    print("Welcome to DT Finder (Server)")
    DT_Server = DTServer('127.0.0.1', [5000, 5001, 5002])
    while True:
        print("Waiting DT_request")
        data, addr = DT_Server.getRequest()
        if addr == None:
            time.sleep(1.0) # in sec
            continue
        elif len(data) != 6:
            print("Packet length error!")
            #continue
        
        request = DT_Response.decodePacket(data)
        print(request)
        #if request.requestType == 0x0001:
            #print("Received packet asking for textual representation of the current date.")
        #elif request.requestType == 0x0002:
            #print("Received packet asking for textual representation of the current time of day.")
        # Reply    
    
if __name__ == "__main__":
    mainloop()