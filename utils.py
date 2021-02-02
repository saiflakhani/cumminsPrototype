def twos_complement_rssi(n, w=8):
    if n & (1 << (w - 1)): n = n - (1 << w)
    return n