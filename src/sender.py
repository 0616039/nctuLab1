#!/usr/bin/env python

import argparse
from scapy.all import *

# Import protocol
from Protocol import Protocol

# Set source and destination IP address (Task 3.)
<<<<<<< HEAD
src_ip = '10.0.1.1'
dst_ip = '10.0.1.2'

# Set source and destination port (Task 3.)
src_port = 1024
dst_port = 80
=======


# Set source and destination port (Task 3.)

>>>>>>> 0102c067b44a2f7ea2085ada7a98e68292dc765e


'''
Main function
'''
def main():
    # Define IP header (Task 3.)
<<<<<<< HEAD
    ip =IP(src = src_ip, dst = dst_ip)

    # Define customized header (Task 3.)
    my_id = '0616039'
    my_dept = 'cs'
    my_gender = 1
=======
    ip = IP()

    # Define customized header (Task 3.)
    my_id = ''
    my_dept = ''
    my_gender = ''
>>>>>>> 0102c067b44a2f7ea2085ada7a98e68292dc765e
    student = Protocol(id = my_id, dept = my_dept, gender = my_gender)

    # Read file and store into list
    count = 0
    secret = []
    tmp = ''.join(reversed(my_id))
    with open('./data/secret.txt', 'r') as file:
        for line in file:
            line = tmp[count % 7] + line
            secret.append(line)
            count += 1

    # Send packets
    for i in range(0, len(secret)):
        # TCP connection - SYN / SYN-ACK
        tcp_syn = TCP(sport = src_port, dport = dst_port, flags = 'S', seq = 0)
        packet = ip / tcp_syn
        tcp_syn_ack = sr1(packet)
        print '[INFO] Send SYN and receive SYN-ACK'
        tcp_syn_ack.show()

        # TCP connection - ACK (Task 3.)
<<<<<<< HEAD
        ack = tcp_syn_ack.seq + 1
	tcp_ack = TCP(sport = src_port, dport = dst_port, flags = 'A', seq = 1, ack =ack)
	send(packet)
	print '[INFO] Send ACK'

        # Send packet with customized header (Task 3.)
	ack = tcp_ack.seq + 1
	tcp = TCP(sport = src_port, dport = dst_port, flags = '', seq = 2, ack = ack)
	packet = ip / tcp / student
	send(packet)
        print '[INFO] Send packet with customized header'

        # Send packet with secret payload (Task 3.)
	ack = tcp.seq + 1
	tcp =TCP(sport = src_port, dport = dst_port, flags = '', seq = 3, ack =ack)
	payload = Raw(secret[i])
	packet = ip / tcp / payload
	send(packet) 
=======
        print '[INFO] Send ACK'

        # Send packet with customized header (Task 3.)
        print '[INFO] Send packet with customized header'

        # Send packet with secret payload (Task 3.)
>>>>>>> 0102c067b44a2f7ea2085ada7a98e68292dc765e
        print '[INFO] Send packet with secret payload'

        
if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 0102c067b44a2f7ea2085ada7a98e68292dc765e
