from spinnman.transceiver import create_transceiver_from_hostname

from spinnman.data.file_data_reader import FileDataReader as SpinnmanFileDataReader 

from spynnaker.pyNN.spynnaker_comms_functions import SpynnakerCommsFunctions 
 
import pickle 

txrx = create_transceiver_from_hostname(hostname="192.168.240.253", discover=False)

txrx.ensure_board_is_ready(int(3)) 

txrx.discover_connections() 
 
application_data_file_reader = SpinnmanFileDataReader("192.168.240.253_appData_0_0_5.dat")
txrx.write_memory(0, 0, 1879048192, application_data_file_reader, 128)
txrx.write_memory(0, 0, 3842011888, 1879048192)
application_data_file_reader = SpinnmanFileDataReader("192.168.240.253_appData_0_0_1.dat")
txrx.write_memory(0, 0, 1879048320, application_data_file_reader, 132)
txrx.write_memory(0, 0, 3842011376, 1879048320)
application_data_file_reader = SpinnmanFileDataReader("192.168.240.253_appData_0_0_2.dat")
txrx.write_memory(0, 0, 1879048452, application_data_file_reader, 124)
txrx.write_memory(0, 0, 3842011504, 1879048452)
application_data_file_reader = SpinnmanFileDataReader("192.168.240.253_appData_0_0_3.dat")
txrx.write_memory(0, 0, 1879048576, application_data_file_reader, 116)
txrx.write_memory(0, 0, 3842011632, 1879048576)
application_data_file_reader = SpinnmanFileDataReader("192.168.240.253_appData_0_0_4.dat")
txrx.write_memory(0, 0, 1879048692, application_data_file_reader, 10712)
txrx.write_memory(0, 0, 3842011760, 1879048692)
router_table = pickle.load(open("picked_routing_table_for_0_0", "rb"))
txrx.load_multicast_routes(router_table.x, router_table.y, router_table.multicast_routing_entries, app_id=30)
executable_targets = pickle.load(open("picked_executables_mappings", "rb"))
core_subset = executable_targets["/home/micky/src/spinnaker/venv/lib/python2.7/site-packages/spynnaker/pyNN/model_binaries/live_packet_gather.aplx"]
file_reader = SpinnmanFileDataReader("/home/micky/src/spinnaker/venv/lib/python2.7/site-packages/spynnaker/pyNN/model_binaries/live_packet_gather.aplx")
txrx.execute_flood(core_subset, file_reader, 30, 11024)
core_subset = executable_targets["/home/micky/src/spinnaker/venv/lib/python2.7/site-packages/spynnaker/pyNN/model_binaries/spike_source_array.aplx"]
file_reader = SpinnmanFileDataReader("/home/micky/src/spinnaker/venv/lib/python2.7/site-packages/spynnaker/pyNN/model_binaries/spike_source_array.aplx")
txrx.execute_flood(core_subset, file_reader, 30, 10352)
core_subset = executable_targets["/home/micky/src/spinnaker/venv/lib/python2.7/site-packages/spynnaker/pyNN/model_binaries/IF_curr_exp.aplx"]
file_reader = SpinnmanFileDataReader("/home/micky/src/spinnaker/venv/lib/python2.7/site-packages/spynnaker/pyNN/model_binaries/IF_curr_exp.aplx")
txrx.execute_flood(core_subset, file_reader, 30, 14508)
core_subset = executable_targets["/home/micky/src/spinnaker/venv/lib/python2.7/site-packages/spynnaker/pyNN/model_binaries/delay_extension.aplx"]
file_reader = SpinnmanFileDataReader("/home/micky/src/spinnaker/venv/lib/python2.7/site-packages/spynnaker/pyNN/model_binaries/delay_extension.aplx")
txrx.execute_flood(core_subset, file_reader, 30, 10628)
executable_targets = pickle.load(open("picked_executable_targets", "rb"))
spinnaker_comms = SpynnakerCommsFunctions(None, None)
spinnaker_comms._setup_interfaces("192.168.240.253")
spinnaker_comms._start_execution_on_machine(executable_targets, 30, 500)
