from scapy.utils import RawPcapReader
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP

testcap = open('arzex.pcap', 'rb')
print('Opening {}...'.format(testcap))

client = '192.168.1.137:57080'
server = '152.19.134.43:80'

(client_ip, client_port) = client.split(':')
(server_ip, server_port) = server.split(':')

count = 0
interesting_packet_count = 0

for (pkt_data, pkt_metadata,) in RawPcapReader(testcap):
    count += 1
    ether_pkt = Ether(pkt_data)
    if 'type' not in ether_pkt.fields:
        # LLC frames will have 'len' instead of 'type'.
        # We disregard those
        continue

    if ether_pkt.type != 0x0800:
        # disregard non-IPv4 packets
        continue

    ip_pkt = ether_pkt[IP]
    print(ip_pkt.src)

    if ip_pkt.proto != 6:
        # Ignore non-TCP packet
        continue

    if (ip_pkt.src != server_ip) and (ip_pkt.src != client_ip):
        # Uninteresting source IP address
        continue
    
    if (ip_pkt.dst != server_ip) and (ip_pkt.dst != client_ip):
        # Uninteresting destination IP address
        continue

    tcp_pkt = ip_pkt[TCP]
    
    if (tcp_pkt.sport != int(server_port)) and \
        (tcp_pkt.sport != int(client_port)):
        # Uninteresting source TCP port
        continue
    
    if (tcp_pkt.dport != int(server_port)) and \
        (tcp_pkt.dport != int(client_port)):
        # Uninteresting destination TCP port
        continue

    interesting_packet_count += 1


print('{} contains {} packets ({} interesting)'.
        format(testcap, count, interesting_packet_count))

