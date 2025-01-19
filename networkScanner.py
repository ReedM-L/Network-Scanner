from scapy.all import *
from scapy.all import IP, ICMP

# ICMP Ping
packet = IP(dst = "192.168.1.0/30")
ans, unans = sr(packet/ICMP(), timeout=3)

# Sending packet

# Print results