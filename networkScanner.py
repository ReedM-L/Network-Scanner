from scapy.all import *
from scapy.all import IP, ICMP, TCP
import sys


def ipValidation(ip_address):
    parts = ip_address.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        numVal = int(part)
        if numVal < 0 or numVal > 255:
            return False
    return True


def Ping(ip_address):
    with open("results.txt", "w") as f:
        packet = IP(dst = ip_address)
        ans, unans = sr(packet/ICMP(), timeout=3)
        if ans:
            f.write(ans)
            print("Scanning ports: 0-1000")
            port = range(0,1000)
            for current_port in port:
                response = sr(packet/TCP(dport = current_port, flags="S"))
                f.write(str(current_port)+ ": " + str(response))
        else:
            print(unans)
    

        
def main():
    ip_address = input("Enter the IP address to scan: ")
    if ipValidation(ip_address):
        confirmation = input("Continue with scan of network? Y/N: ")
        if confirmation == "Y" or confirmation == "y":
            Ping(ip_address)
        else:
            sys.exit()
    else:
        print("Invalid IP address")


if __name__ == "__main__":
    main()
