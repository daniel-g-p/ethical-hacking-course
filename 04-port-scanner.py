#!/bin/python3

import socket
import sys

IP = sys.argv[1] if len(sys.argv) >= 2 else ""


def ip_is_valid(ip: str):
    octets = list(map(lambda item: int(item), ip.split(".")))
    return len(octets) == 4 and all(octet >= 0 and octet <= 255 for octet in octets)


if ip_is_valid(IP):
    print("-" * 64)
    print(f"Scanning IP address {IP}")
    print("-" * 64)
else:
    print("Invalid IP address.")
