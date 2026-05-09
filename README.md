# TCP SYN Flood Simulation using Scapy

A localhost-based TCP SYN Flood simulation built using Python and Scapy to study denial-of-service behavior and TCP handshakes.

## Concepts Used
- TCP three-way handshake
- SYN packets
- Half-open connections
- Backlog queue

## Tools Used
- Python
- Scapy
- Linux
- Wireshark

## Features
- Randomized source IP spoofing
- Randomized source ports
- SYN packet crafting
- Packet-level traffic analysis

## Packet Capture Evidence
Traffic was captured and analyzed using Wireshark/tcpdump to observe:
- ICMP Echo Requests/Replies
- DNS traffic
- TCP SYN packets

## Disclaimer
This project was performed strictly on localhost (127.0.0.1) for educational purposes.
