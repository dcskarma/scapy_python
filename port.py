#!/usr/bin/env python
try:
   from scapy.all import *
   import argparse
except:
    print("you dont have a scapy module install scapy by : pip install scapy")

parser = argparse.ArgumentParser(description='discovey the port by scapy')
parser.add_argument('-i','--ip', type=str, required=True, help='type ip of your target')
parser.add_argument('-p','--port', type=int,required=True, help='type port number')
args = parser.parse_args()
ip = args.ip
port = args.port

header=IP(dst=ip)/TCP(dport=port, flags="S")
ans,uns=sr(header,timeout=5)

for i in ans:
     print(ans)

for i in uns:
    print (uns)
