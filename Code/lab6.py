# Lab6

import math

def number_fdma_channels (b_hz, g_hz, u_hz):
    return math.floor((b_hz-g_hz) / (g_hz+u_hz))

def number_tdma_users (s_s, g_s, u_s):
    return math.floor(s_s / (g_s+u_s))

def p_persistent_csma_collision_probability (p):
    return p* 1/(2-p)

def p_persistent_csma_access_delay (p):
    return (1-p)/p

def test():
    # print (number_fdma_channels(1000000, 200, 20000))
    # print (number_fdma_channels(1000000, 1000, 20000))
    # print (number_fdma_channels(1000000, 1000, 30000))

    # print (number_tdma_users(1, 0.001, 0.008))
    # print (number_tdma_users(0.1, 0.001, 0.005))

    # print ("{:.3f}".format(p_persistent_csma_collision_probability(0.2)))
    # print ("{:.3f}".format(p_persistent_csma_collision_probability(0.4)))

    print ("{:.3f}".format(p_persistent_csma_access_delay(0.1)))

    # Q19: 2**min(10, coll)-1
    # 0.5 + 1.5 + 3.5 + 7.5 = 13 slot times

test()