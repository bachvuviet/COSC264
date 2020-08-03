# Client Application (client.py)
# Bach Vu
# 01/08/2020

from packet import *
from request import *
from response import *
from socket import *
import sys, time, select

class DTClient():
    def __init__(self, target):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.target = target
        
    def postRequest(self, request):
        packet = request.encodePacket()
        if isinstance(packet, bytearray):
            self.socket.sendto(packet, self.target)
            print("Request sent to {}:{}! Waiting for response ... ".format(self.target[0], self.target[1]))
        else:
            print("Request sent failed with code {}! Try again ... ".format(packet))
        
    def getResponse(self, mode):
        data, addr = self.socket.recvfrom(1024)
        return DT_Response.decodePacket(data, mode)       

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
    
    host, port = sys.argv[2], int(sys.argv[3])
    DT_client = DTClient((host, port))  
    mo = 1 if sys.argv[1] == 'date' else 2
    request = DT_Request(mo)
    DT_client.postRequest(request)
    
    response = None
    count = 0
    while response is None and count < 5:
        time.sleep(1)
        count += 1
        response = DT_client.getResponse(mo)
    print(response.getDT_str() + '\n')

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