# Lab4

import math

def number_fragments (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes    
    return math.ceil(s / (m-o))

def last_fragment_size (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    pack_full = math.floor(s / (m-o))
    return s - (m-o)*pack_full + o

def test():
    print (number_fragments(10000, 100, 1000))
    print (last_fragment_size(10000, 100, 1000))
    # Q19: data 1.5kB, message = data + 20Byte TCP header
    # Q22: message 10kB, 20-byte IP header is appended to each packet
    print(last_fragment_size(10000, 20, 1500)) 
    # Q23: First fragment = 20B IP-head + 20B TCP-head + 1460B data
    # Second fragment = 20B IP-head + 1480B data +... + last fragment = 1140B
    
test()