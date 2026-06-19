from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)
        print("-" * 40)

print("Capturing packets...")
sniff(prn=packet_callback, count=10)