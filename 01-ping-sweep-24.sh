!/bin/bash

subnet=$1

if [ -z "$subnet" ]; then
    echo "Error: Please enter an IP address"
else
    for i in $(seq 1 255); do
        ip="${subnet}.${i}"
        ping $ip -c 1 | grep "64 bytes from $ip" | cut -d ":" -f 1 | cut -d " " -f 4 &
    done
fi
