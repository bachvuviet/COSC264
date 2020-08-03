# Client Application (client.py)
# Bach Vu
# 01/08/2020

from packet import *
from request import *
from response import *
from socket import *
import sys, select

class DTClient():
    def __init__(self, target):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.setblocking(0)
        self.target = target
        
    def postRequest(self, request):
        packet = request.encodePacket()
        if isinstance(packet, bytearray):
            self.socket.sendto(packet, self.target)
            print("Request sent to {}:{}! Waiting for response ... ".format(self.target[0], self.target[1]))
        else:
            print("Request sent failed with code {}! Try again ... ".format(packet))
        
    def getResponse(self):
        ready = select.select([self.socket], [], [], 5)
        if ready[0]:
            data, addr = self.socket.recvfrom(1024)
            return data
        return None

################## Main Program ##################
def main():
    print("\nWelcome to DT Finder (Client)")
    # Error Checking
    errMess = [
        "Argument input error.\n    python client.py {mode} {host_target} {port_eng/maori/ger}",
        "Ports input must be integer (whole number).",
        "Port must be between 1024 and 64000 inclusively!",
        "mode must be 'time' or 'date'."
    ]   
    errCode = checkInputArgv()
    if errCode != 0:
        print(errMess[errCode-1])
        sys.exit()    
    
    # Request
    host, port = sys.argv[2], int(sys.argv[3])
    DT_client = DTClient((host, port))  
    mo = 1 if sys.argv[1] == 'date' else 2
    request = DT_Request(mo)
    DT_client.postRequest(request)
     
    # Response
    response = DT_client.getResponse()
    if not response:
        print("A response discarded. Packet length error!")
        return
    if len(response) < 13:
        print("A response discarded. Packet length error!")
        return
    response = DT_Response.decodePacket(response, mo)
    
    if isinstance(response, int):
        print("A response discarded. Error code: " + request)
    elif response:
        print(response.getDT_str() + '\n')
    else:
        print("Check your destination. We received no data after 5sec (time-out)\n")

def checkInputArgv():
    if len(sys.argv) != 4:
        return 1    

    mode = sys.argv[1]
    try:
        port = int(sys.argv[3])
    except BaseException:
        return 2
    
    if port < 1024 or port > 64000:
        return 3
    if mode != "date" and mode != "time":
        return 4
    return 0

if __name__ == "__main__":
    main()