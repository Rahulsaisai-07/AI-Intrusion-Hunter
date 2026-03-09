from scapy.all import *

def packet_detect(packet):
    if packet.haslayer(IP):
        print("Packet from:", packet[IP].src)

sniff(prn=packet_detect)
