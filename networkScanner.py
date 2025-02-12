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
    try:
        with open("results.txt", "w") as f:
            packet = IP(dst = ip_address)
            ans, unans = sr(packet/ICMP(), timeout=3)
            responseList = []
            norespList = []
            if ans:
                print(ans.summary())
                print("Scanning ports: 0-1000")
                port = range(0,1000)
                for current_port in port:
                    resp, noResp = sr(packet/TCP(dport = current_port, flags="S",timeout=2))
                    responseList.append(resp)
                    norespList.append(noResp)
            else:
                print(unans)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: You do not have permission to access this file.")
    except Exception as e:
        print(f"Unexpected error has occured: {e}")
    finally:
        f.close()
        
    
        
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
