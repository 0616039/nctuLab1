#!/usr/bin/env python

from scapy.all import *

'''
Define your own protocol
'''
class Protocol(Packet):
    # Set the name of protcol (Task 2.)
<<<<<<< HEAD
    name = 'Student'

    # Define the fields in protocol (Task 2.)
    fields_desc = [ 
        StrField('index','0'),
        StrField('dept', 'cs', fmt='H', remain = 0),
        IntEnumField('gender',2,{
		1: 'female',
		2: 'male'
	}),

	StrField('id', '000000', fmt = 'H', remain = 0),
=======
    name = ''

    # Define the fields in protocol (Task 2.)
    fields_desc = [ 
        
>>>>>>> 0102c067b44a2f7ea2085ada7a98e68292dc765e
    ]

'''
Add customized protocol into IP layer
'''
bind_layers(TCP, Protocol, frag = 0, proto = 99)
conf.stats_classic_protocols += [Protocol]
<<<<<<< HEAD
conf.stats_dot11_protocols += [Protocol]

=======
conf.stats_dot11_protocols += [Protocol]
>>>>>>> 0102c067b44a2f7ea2085ada7a98e68292dc765e
