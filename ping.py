#!/usr/bin/env python
try:
    from scapy.all import *
    import sys
except:
    sys.exit ("[!]Install scapy with pip")

ip = sys.argv[1]

icmp = IP(dst=ip)/ICMP()
ans = sr1(icmp, timeout=4)

if ans == None:
    print("host is down")
else:
    print ("host is up")

ans.show()
