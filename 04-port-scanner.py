#!/bin/python3

import socket
import sys

HOST = sys.argv[1] if len(sys.argv) >= 2 else ""
PORTS = [
    21,
    22,
    23,
    53,
    67,
    68,
    69,
    80,
    110,
    139,
    143,
    145,
    161,
    443,
]


def ip_is_valid(ip: str):
    octets = list(map(lambda item: int(item), ip.split(".")))
    return len(octets) == 4 and all(octet >= 0 and octet <= 255 for octet in octets)


if ip_is_valid(HOST):
    print("-" * 128)
    print(f"Scanning IP address {HOST}...")
    print("-" * 128)

    socket.setdefaulttimeout(1)

    for PORT in PORTS:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        response = s.connect_ex((HOST, PORT))
        print(f"Port {PORT}: {'Open' if response == 0 else 'Closed'}")
        s.close()

    print("-" * 128)
else:
    print("Invalid IP address.")
