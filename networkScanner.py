from scapy.all import *
from scapy.all import IP, ICMP, TCP

# ICMP Ping
def ipValidation(ip_address):
    parts = ip_address.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        numVal = int(part)
        if part < 0 or part > 255:
            return False


def Ping(ip_address):
    packet = IP(dst = ip_address)
    ans, unans = sr(packet/ICMP(), timeout=3)
    if ans:
        print(ans)
        print("Scanning ports: 0-1000")
        port = range(0,1000)
        while(port in port):
            response = sr1(packet/TCP(dport = port, flags="S"))
            print(response)
    else:
        print(unans)

        
def main():
    ip_address = input("Enter the IP address to scan: ")
    if ipValidation(ip_address):
        confimation = input("Continue with ping of network? Y/N")
        if confimation == "Y" or "y":
            Ping(ip_address)
        else:
            sys.exit()


if __name__ == "__main__":
    main()
