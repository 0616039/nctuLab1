#!/usr/bin/env python

from random import *
from scapy.all import *
from time import *

# Set source IP address and destination interface (Task 4.)
<<<<<<< HEAD
dst_iface = 'h2-eth0'
src_ip = '10.0.1.1'
=======

>>>>>>> 0102c067b44a2f7ea2085ada7a98e68292dc765e

# Store the receiving secret
id = ''
received = []


'''
Handle the received packet
'''
def packetHandler(packet):
    # Use global variable
    global id, received

    # Show the receiving packet
    packet.show()

    # Filtering packet
    if TCP in packet and packet['IP'].src == src_ip:
        if packet['TCP'].seq == 2: 
            print '[INFO] Receive packet with customized protocol'
            id = str(packet['Raw'])[-6:]
        elif packet['TCP'].seq == 3: 
            print '[INFO] Receive packet with secret payload'
            received.append(packet['Raw'])


'''
Main function
'''
def main():
    # Sniff packets on destination interface (Task 4.)
    print '[INFO] Sniff on %s' % dst_iface
<<<<<<< HEAD
    packets = sniff(iface = dst_iface, prn = lambda x: packetHandler(x))

    # Dump the sniffed packet into PCAP file (Task 4.)
    print '[INFO] Write into PCAP file'   
    filename = './out/lab1_0' + id + '.pcap'
    wrpcap(filename, packets)
=======
    

    # Dump the sniffed packet into PCAP file (Task 4.)
    print '[INFO] Write into PCAP file'   
>>>>>>> 0102c067b44a2f7ea2085ada7a98e68292dc765e


    # Write the receiving secret into file
    with open('./out/recv_secret.txt', 'w') as file:
        for line in received:
            file.write('%s' % line)
    
    # Finishing receiving in a duration
    print '[INFO] Finish receiving packets in a duration'


if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 0102c067b44a2f7ea2085ada7a98e68292dc765e
