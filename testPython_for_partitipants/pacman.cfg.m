[Logging]
# ------
# Logging levels are as specified for the Python logging module.
# Listing a module below overrides the default logging level for that module
# and its children (unless they are also overridden).
#
# e.g., the following sample would set the default level to info, but display
# debug messages for pacman103.front.pynn, and only display warning messages
# for pacman.core
#
#     default = info
#     debug = front.pynn
#     info =
#     warning = core
#     error =
#     critical =
#
# The ```instantiate``` option determines whether front-ends set up loggers.
# If ```instantiate``` is True then users do not need to set up their own
# loggers.  If it is False, then users need to instantiate a logger at the top
# of each script, this is simply achieved by inserting the following lines at
# the top of the file.
#
#    include logging
#    logger = logging.basicConfig()
#
instantiate = True
default = info
debug =
info =
warning =
error =
critical =

[Reports]
# If reportsEnabeld is false, no text reports are written.
# writeTextSpecs: If True, produce text version of each Data Spec,
#                 in reports/dataSpec directory
# writeRouterReports: If True, each router file is written in
#                 text format to reports/routers
reportsEnabled = True
writeTextSpecs = False
writePartitionerReports = True
writePlacerReports = True
writeRouterReports = True
writeRouterInfoReport = True
writeRouterDatReport = False
writeTransceiverReport = True
writeProvanceData = True
outputTimesForSections = True
writeReloadSteps = True
# options are DEFAULT (hard coded location) or a file path
defaultReportFilePath = DEFAULT
# options are DEFAULT, TEMP, or a file path
#NOTE ***that for bespoke file paths, folders will not be automatically deleted***
defaultApplicationDataFilePath = DEFAULT
max_reports_kept = 10
max_application_binaries_kept = 10

[Simulation]
# Maximum spikes per second of any neuron (spike rate in Hertz)
spikes_per_second = 30

# The number of standard deviations from the mean to account for in
# the ring buffer
ring_buffer_sigma = 5

[Machine]
#-------
# Information about the target SpiNNaker board or machine:
# machineName: The name or IP address of the target board
# down_cores: Cores that are not working
# down_chips: Chips that are not working
# core_limit: The maximum number of cores to use on the board
# machineTimeStep: Internal time step in simulations in usecs)
# timeScaleFactor: Change this to slow down the simulation time
#                  relative to real time.
# appID:           Used by sark to identify the user's application.
machineName     = spinn-1
virtual_board = False
virutal_board_x_dimension = None
virutal_board_y_dimension = None
requires_wrap_arounds = None
# format is ,,:,,:
down_cores = None
down_chips = None
core_limit = 16
machineTimeStep = 1000
timeScaleFactor = None
appID = 30
tryReboot = True
version = 5

[Routing]
# ------
# AM: THIS NEEDS REVISITING
# algorithm: {BasicDijkstra}
algorithm = BasicDijkstra
generate_graphs = False
graphs_output_file = tmp
#directories to search for algorithums. list in order

[Placer]
#-------
# algorithm: {Radial, Basic}
algorithm = Radial

[Partitioner]
# algorithm: {Basic, PartitionAndPlace}
algorithm = PartitionAndPlace

[KeyAllocator]
# algorithm: {Basic, PyNN}
algorithm = PyNN

[SpecExecution]
#-------------
# specExecOnHost: If True, execute specs on host then download to SpiNNaker
#                 False not yet support, where specs are downloaded
#                 to SpiNNaker and then executed.
specExecOnHost = True

[MasterPopTable]
# algorithm: {2dArray, binaryTree, hashTable}
generator = 2dArray


[Recording]
#---------
# This controls the insertion of the Monitor into the graph
# If enabled, the Monitor will capture spikes, and forward them back to
# the configured host and port (defaults to 17893 on current machine)
send_live_spikes = False
record_spikes_on_sdram = True

# Uncomment the following to change from the defaults
live_spike_port = 17895
live_spike_host = localhost
live_spike_tag = 1

[Execute]
run_simulation = True
load = True
run = True

[Mode]
#mode = Production or Debug
mode = Production

[Threading]
dsg_threads = 5

[Database]
create_database = False
wait_on_confirmation = False
create_routing_info_to_neuron_id_mapping = False
