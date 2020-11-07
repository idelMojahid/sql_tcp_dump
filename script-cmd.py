import sys
import getopt
import functions

# Get host and port from argv
host = ''
port = ''
options, remainder = getopt.getopt(sys.argv[1:], 'h:p', ['host=', 'port='])
for opt, arg in options:
    if opt in ('-h', '--host'):
        host = arg
    elif opt in ('-p', '--port'):
        port = arg

functions.insert_attack(host, port)
