# Superquiz 1

def header_errorCode(version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, 
                     timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    error_code = 0
    if version != 4:
        error_code = 1
    elif hdrlen > 2**4 - 1 or hdrlen < 5 :
        error_code = 2
    elif tosdscp > 2**6 - 1 or tosdscp < 0:
        error_code = 3    
    elif totallength > 2**16 - 1 or totallength < 0:
        error_code = 4
    elif identification > 2**16 - 1 or identification < 0:
        error_code = 5    
    elif flags > 2**3 - 1 or flags < 0:
        error_code = 6
    elif fragmentoffset > 2**13 - 1 or fragmentoffset < 0:
        error_code = 7
    elif timetolive > 2**8 - 1 or timetolive < 0:
        error_code = 8
    elif protocoltype > 2**8 -1 or protocoltype < 0:
        error_code = 9
    elif headerchecksum > 2**16 - 1 or headerchecksum < 0:
        error_code = 10
    elif sourceaddress > 2**32 - 1 or sourceaddress < 0:
        error_code = 11
    elif destinationaddress > 2**32 - 1 or destinationaddress < 0:
        error_code = 12    
    
    return error_code
def intToBinaryString(decimal, str_len):
    #print(bin(decimal))
    return bin(decimal)[2:].zfill(str_len)

def checksumPacket(pkt, expected):
    X = 0
    for i in range(0, 20, 2):    
        X += pkt[i]<<8 | pkt[i+1]  # get 16bit int at a time
        
    while X > 0xFFFF:
        X0 = X & 0xFFFF # get last 16bit from X
        X1 = X >> 16 # get the rest from X
        X = X0 + X1
    return X == expected

def checksumHeader(pkt, head_len):
    X = 0
    for i in range(0, 4*head_len, 2):    
        X += pkt[i]<<8 | pkt[i+1]  # get 16bit int at a time
    while X > 0xFFFF:
        X0 = X & 0xFFFF # get last 16bit from X
        X1 = X >> 16 # get the rest from X
        X = X0 + X1
    return X^0xFFFF
    

def composepacket (version, hdrlen, tosdscp, totallength, identification, flags,
                   fragmentoffset, timetolive, protocoltype, headerchecksum, 
                   sourceaddress, destinationaddress):
    error_code = header_errorCode(version, drlen, tosdscp, identification, flags, fragmentoffset, 
                                  timetolive, protocoltype, sourceaddress, destinationaddress)
    
    if error_code != 0:
        return error_code
    
    packet = ""
    packet += intToBinaryString(version,4)
    packet += intToBinaryString(hdrlen,4)
    packet += intToBinaryString(tosdscp,6)
    packet += intToBinaryString(0,2)
    packet += intToBinaryString(totallength,16)
    packet += intToBinaryString(identification,16)
    packet += intToBinaryString(flags,3)
    packet += intToBinaryString(fragmentoffset,13)
    packet += intToBinaryString(timetolive,8)
    packet += intToBinaryString(protocoltype,8)
    packet += intToBinaryString(headerchecksum,16)
    packet += intToBinaryString(sourceaddress,32)
    packet += intToBinaryString(destinationaddress,32)
    
    # convert string to binary int, then to byte array (32x5 = 160bits = 20 bytes)
    packet = int(packet, 2).to_bytes(20, byteorder='big')
    packet = bytearray() + packet
    return packet



    
def basicpacketcheck (packet):
    version = (packet[0] & 0xF0) >> 4
    dataLen = int.from_bytes(packet[2:4], byteorder="big")
    if len(packet) < 20:
        return 1    # not full header
    if version != 4:
        return 2
    if not checksumPacket(packet, 0xFFFF):
        return 3
    if dataLen != len(packet):
        return 4
    return True

def destaddress (packet):
    ip_dest = int.from_bytes(packet[16:], byteorder="big")
    ip_dest_str = str.format("{}.{}.{}.{}", (ip_dest & 0xFF000000)>>24,
                             (ip_dest & 0xFF0000)>>16, (ip_dest & 0xFF00)>>8, ip_dest & 0xFF)
    return ip_dest, ip_dest_str

def payload (packet):
    head_len = 4* (packet[0] & 0x0F) >> 0 # measured in byte
    return packet[head_len:]
       
def revisedcompose(hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive, 
                   protocoltype, sourceaddress, destinationaddress, payload):
    # Error check
    version = 4
    headerchecksum = 0
    totallength = 4* hdrlen + len(payload)
    error_code = header_errorCode(version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, 
                                  timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress)
    if error_code != 0:
        return error_code
    
    # Check sum (validity)
    header = ""    
    header += intToBinaryString(version,4)
    header += intToBinaryString(hdrlen,4)
    header += intToBinaryString(tosdscp,6)
    header += intToBinaryString(0,2)
    header += intToBinaryString(totallength,16)
    header += intToBinaryString(identification,16)
    header += intToBinaryString(flags,3)
    header += intToBinaryString(fragmentoffset,13)
    header += intToBinaryString(timetolive,8)
    header += intToBinaryString(protocoltype,8)
    header += intToBinaryString(headerchecksum,16) # Temp check sum
    header += intToBinaryString(sourceaddress,32)
    header += intToBinaryString(destinationaddress,32)
    for i in range(6, hdrlen+1):
        header += intToBinaryString(0,32) # optional header bytes
    header = bytearray() + int(header, 2).to_bytes(4* hdrlen, byteorder='big')
    
    headerchecksum = checksumHeader(header, hdrlen)
    if headerchecksum > 2**16 - 1 or headerchecksum < 0:
        return 10     
    header[10:12] = headerchecksum.to_bytes(2, byteorder='big')
    
    # Pack
    packet = bytearray()
    packet += header
    packet += payload
    return packet

def ques1():
    print(composepacket(5,5,0,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[18])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[19])
    print(composepacket(4,16,0,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,15,64,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,15,63,65536,24200,0,63,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,15,63,65535,65536,0,63,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,15,63,65535,65535,8,63,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,15,63,65535,65535,7,8192,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,15,63,65535,65535,7,8191,256,6,4711, 2190815565, 3232270145))
    print(composepacket(4,15,63,65535,65535,7,8191,255,256,4711, 2190815565, 3232270145))
    print(composepacket(4,15,63,65535,65535,7,8191,255,255,65536, 2190815565, 3232270145))
    print(composepacket(4,15,63,65535,65535,7,8191,255,255,65535, 4294967296, 3232270145))
    print(composepacket(4,15,63,65535,65535,7,8191,255,255,65535, 4294967295, 4294967296))
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[0])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[1])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[2])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[3])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[4])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[5])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[6])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[7])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[8])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[9])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[10])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[11])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[12])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[13])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[14])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[15])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[16])
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[17])
    print(composepacket(4,-3,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,5,0,1500,-24200,0,63,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,5,0,1500,24200,0,63,22,6,-4711, 2190815565, 3232270145))    
    
def ques2():
    print(basicpacketcheck(bytearray ([0x45, 0x0, 0x0, 0x1e, 0x4, 0xd2, 0x0, 0x0, 0x40, 0x6, 0x20, 0xb4, 0x12, 0x34, 0x56, 0x78, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])))
    print(basicpacketcheck(bytearray ([0x45, 0x0, 0x0, 0x1e, 0x16, 0x2e, 0x0, 0x0, 0x40, 0x6, 0xcd, 0x59, 0x66, 0x66, 0x44, 0x44, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])))
    print(basicpacketcheck(bytearray ([0x45, 0x0, 0x0, 0x1b, 0x12, 0x67, 0x20, 0xe, 0x20, 0x6, 0x35, 0x58, 0x66, 0x66, 0x44, 0x44, 0x55, 0x44, 0x33, 0x22, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])))
    print(basicpacketcheck(bytearray ([0x45, 0x0, 0x0, 0x1b, 0x12, 0x67, 0x20, 0xe, 0x20, 0x6, 0x35, 0x58, 0x66, 0x66, 0x44, 0x44, 0x55, 0x44, 0x33, 0x22, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])))
    print(basicpacketcheck(bytearray ([0x45, 0x0, 0x0, 0x1b, 0x12, 0x67, 0x20, 0xe, 0x20, 0x6, 0x35, 0x58, 0x66, 0x66, 0x44, 0x44, 0x55, 0x44, 0x33, 0x22, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])))
    print(basicpacketcheck(bytearray ([0x45, 0x0, 0x0, 0x1b, 0x12, 0x67, 0x20, 0xe, 0x20, 0x6, 0x35, 0x58, 0x66, 0x66])))
    print(basicpacketcheck(bytearray ([0x55, 0x0, 0x0, 0x1b, 0x12, 0x67, 0x20, 0xe, 0x20, 0x6, 0x35, 0x58, 0x66, 0x66, 0x44, 0x44, 0x55, 0x44, 0x33, 0x22, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])))
    print(basicpacketcheck(bytearray ([0x46, 0x0, 0x0, 0x1e, 0x16, 0x2e, 0x0, 0x0, 0x40, 0x6, 0xcd, 0x59, 0x66, 0x66, 0x44, 0x44, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])))
    print(basicpacketcheck(bytearray ([0x45, 0x0, 0x0, 0x1e, 0x16, 0x2e, 0x0, 0x0, 0x40, 0x6, 0xce, 0x59, 0x66, 0x66, 0x44, 0x44, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])))
    #print(basicpacketcheck(composepacket(4, 5, 0, 44, 0x3333, 2, 47, 32, 0x06, 0x44336655, 0x34567890)))
    #print(basicpacketcheck(composepacket(4, 5, 0, 44, 0x5555, 2, 47, 35, 0x06, 0x44336655, 0x34567890)))
    #print(basicpacketcheck(composepacket(4, 5, 0, 44, 0x3333, 2, 4755, 32, 0x06, 0x44336655, 0x34567890)))    

def ques3():
    print(destaddress(bytearray(b'E\x00\x00\x1e\x04\xd2\x00\x00@\x06\x00\x00\x00\x124V3DUf')))
    #print(destaddress(composepacket(4, 5, 0, 30, 1234, 0, 0, 0, 64, 0x06, 0x123456, 0x33445566)))

def ques4():
    print(payload(bytearray(b'E\x00\x00\x17\x00\x00\x00\x00@\x06i\x8d\x11"3DUfw\x88\x10\x11\x12')))
    print(payload(bytearray(b'F\x00\x00\x1e\x00\x00\x00\x00@\x06h\x86\x11"3DUfw\x88\x00\x00\x00\x00\x13\x14\x15\x16\x17\x18')))
    
def ques5():
    print(revisedcompose (6, 24, 4711, 0, 22, 64, 0x06, 0x22334455, 0x66778899, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15])))
    print(revisedcompose(16,0,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
    print(revisedcompose(4,0,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
    print(revisedcompose(5,64,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
    print(revisedcompose(5,63,0x10000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
    print(revisedcompose(5,63,4711,8,63,22,0x06, 2190815565, 3232270145, bytearray([])))
    print(revisedcompose(5,63,4711,0,8192,22,0x06, 2190815565, 3232270145, bytearray([])))
    print(revisedcompose(5,63,4711,0,8191,256,0x06, 2190815565, 3232270145, bytearray([])))
    print(revisedcompose(5,63,4711,0,8191,64,256, 2190815565, 3232270145, bytearray([])))
    print(revisedcompose(5,63,4711,0,8191,64,0x06, 4294967296, 3232270145, bytearray([])))
    print(revisedcompose(5,63,4711,0,8191,64,0x06, 2190815565, 4294967296, bytearray([])))
    print(revisedcompose (5, 24, 4711, 0, 22, 64, 0x06, 0x22334455, 0x66778899, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17])))
    print(revisedcompose (5, 24, 4711, 0, 22, 64, 0x06, 0x66778899, 0x22334455, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17])))
        
def test():
    #ques1()
    #ques2()
    #ques3()
    #ques4()
    ques5()
    
test()