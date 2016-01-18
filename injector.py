from spinnman.messages.eieio.eieio_header                                   import EIEIOHeader
from spinnman.messages.eieio.eieio_message                                  import EIEIOMessage
from spinnman.messages.eieio.eieio_type_param                               import EIEIOTypeParam
from spinnman.messages.eieio.eieio_prefix_type                              import EIEIOPrefixType
from spinnman.connections.udp_packet_connections.reverse_iptag_connection   import ReverseIPTagConnection

udp_connection = ReverseIPTagConnection(remote_host="192.168.240.253", remote_port=12345)
header  = EIEIOHeader( type_param = EIEIOTypeParam.KEY_16_BIT, count_param = 1 )
message = EIEIOMessage( eieio_header = header, data = bytearray() )
message.write_key(0)
udp_connection.send_eieio_message(message)
