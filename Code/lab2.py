# Lab2

def transmission_delay1 (packetLength_bytes, rate_mbps):
    # 1 MBps = 8 Mbps
    return packetLength_bytes / (rate_mbps * 1000000/8)

def transmission_delay2 (packetLength_bytes, rate_bps):
    return (packetLength_bytes*8) / rate_bps

def total_time (cableLength_KM, packetLength_b):
    propagation_delay = cableLength_KM / 200000
    transmission_delay = packetLength_b / (10 * 10**9)
    return (propagation_delay + transmission_delay) *1000 # in ms

def queueing_delay (rate_bps, numPackets, packetLength_b):
    transmission_delay = packetLength_b / rate_bps
    return transmission_delay * numPackets

def average_trials (P):
    # Geometric of the second kind (successful trial to be counted) 
    return 1/(1-P)

def per_from_ber (bitErrorProb, packetLen_b):
    # Binom model on Bernoli trial (X bit correct)
    # prob of X >= 1000 in packetLen_b trial
    avg_correct_bit = (1-bitErrorProb)**packetLen_b
    # prob of X < 1000 in packetLen_b trial
    return 1 - avg_correct_bit

def avg_trials_from_ber (bit_error_probability, packetLength_b):
    # Geometric of the second kind (successful trial to be counted) 
    P = per_from_ber(bit_error_probability, packetLength_b)
    return 1/(1-P)    
    
def test():
    print ("{:.3f}".format(transmission_delay1(1000000, 4)))
    print ("{:.3f}".format(transmission_delay2(1000000, 4000000)))
    print ("{:.4f}".format(total_time(10000, 8000)))
    print ("{:.3f}".format(queueing_delay(1000000, 7, 10000)))
    print ("{:.3f}".format(queueing_delay(100000000, 20, 12000)*1000))
    print ("{:.3f}".format(average_trials(0.1)))
    print ("{:.3f}".format(average_trials(0.2)))
    print ("{:.3f}".format(per_from_ber(0.0001, 1000)))
    print ("{:.3f}".format(avg_trials_from_ber(0.0001, 1000)))
    print ("{:.3f}".format(avg_trials_from_ber(0.005, 1000)), "trails")
    print ("{:.3f}".format(avg_trials_from_ber(0.001, 2000)), "trails")
test()