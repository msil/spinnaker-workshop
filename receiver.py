from spinnman.connections.udp_packet_connections.stripped_iptag_connection import StrippedIPTagConnection
from spinnman.constants import TRAFFIC_TYPE
import time
from pprint import pprint

packet_grabber = StrippedIPTagConnection(local_port=18250)

def packet_callback( packet ):
    pprint(packet)

packet_grabber.register_callback( packet_callback, TRAFFIC_TYPE.EIEIO_DATA)
time.sleep(50)
