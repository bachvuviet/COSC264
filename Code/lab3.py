# Lab2

def connection_setup_delay (cableLength_km, speedOfLight_kms, dataRate_bps, 
                            messageLength_b, processingTimes_s):   
    propagation_delay = cableLength_km / speedOfLight_kms
    transmission_delay = messageLength_b / dataRate_bps
    proocess_delay = processingTimes_s
    
    total_delay = 2* 2*(propagation_delay + transmission_delay + proocess_delay)
    return total_delay

def message_delay (connSetupTime_s, cableLength_km, speedOfLight_kms, messageLength_b, dataRate_bps):
    mess_delay = 2*cableLength_km / speedOfLight_kms + messageLength_b / dataRate_bps
    return connSetupTime_s + mess_delay

def total_number_bits (maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    M = messageLength_b

    total_bit = 0
    num_packet = M // S
    if M / S  != num_packet:
        total_bit += O + M % S
    total_bit += num_packet * (S+O)
    return total_bit

def packet_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b):
    L = linkLength_km
    C = speedOfLight_kms
    P = processingDelay_s
    R = dataRate_bps
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    
    delay = L/C + P
    return 2*delay + 2*(S+O)/R

def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b
    
    packet_delay = packet_transfer_time(l, c, p, r, s, o) # only for first packet
    packet_num = m/s -1 # total bit - 1 packet size
    return packet_delay + packet_num * (s+o)/r # concurent has no delay
    
def test():
    print ("{:.4f}".format(connection_setup_delay(10000, 200000, 1000000, 1000, 0.001)))
    print ("{:.4f}".format(connection_setup_delay(10000, 200000, 1000000, 4000, 0.001)))
    print ("{:.3f}".format(message_delay(0.305, 15000, 200000, 5000, 1000000)))
    print ("{:.3f}".format(message_delay(0.2, 10000, 200000, 1000, 1000000)))
    print ("{:.3f}".format(message_delay(0.2, 10000, 200000, 1000000000, 1000000)))
        
    print ("{:.1f}".format(total_number_bits(1000, 100, 10000)))
    print ("{:.4f}".format(packet_transfer_time(10000, 200000, 0.001, 1000000, 1000, 100)))
    print ("{:.5f}".format(packet_transfer_time (15000, 250000, 0.001, 1000000, 4192, 100)))
    print ("{:.4f}".format(total_transfer_time(20000, 200000, 0.001, 1000000, 1000, 100, 5000)))
    print ("{:.5f}".format(total_transfer_time (10000, 200000, 0.001, 1000000, 1000, 100, 1000000000)))
    
test()