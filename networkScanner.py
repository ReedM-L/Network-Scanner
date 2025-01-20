from scapy.all import *
from scapy.all import IP, ICMP, TCP

# ICMP Ping

packet = IP(dst = "8.8.8.8")
ans, unans = sr(packet/ICMP()/TCP(dport=80,flags="S"), timeout=3)

if (ans):
    response = sr1(packet/TCP(dport=80, flags="S"))

# Sending packet

# Print results