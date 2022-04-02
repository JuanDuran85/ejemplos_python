"""_summary_

    Working with library socket

"""

import socket
import ipaddress

# get host name from socket
print(f"{socket.gethostname() = }")

# ip direccion
print(f"{socket.gethostbyname(socket.gethostname()) }")

# ---------------------------------------------------------------------------------------------
# validate ip address
# ---------------------------------------------------------------------------------------------

ip_addresses = ("192.168.0.1","127.0.0.1","192.168.1.257","1.0x2.3.4","2001:0db8:85a3:0000:0000:8a2e:0370:7334")

def valid_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def valid_ip4_addr(ip: str) -> bool:
    try:
        socket.inet_pton(socket.AF_INET, ip)
    except socket.error:
        return False

for ip in ip_addresses:
    print(f"{ip:<40} | {str(valid_ip(ip)):<5} | {str(valid_ip4_addr(ip))}")