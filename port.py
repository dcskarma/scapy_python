#!/usr/bin/env python
from scapy.all import *

ip = "192.168.10.1"
port = 445
header=IP(dst=ip)/TCP(dport=port, flags="S")
ans,uns=sr(header,timeout=5)

ans.summary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA",prn=lambda s,r: r.sprintf("%TCP.sport% is open")) 

