from argparse import ArgumentParser

PARSER = ArgumentParser(
    description='Send a tcp syn packet to a host/port to see if a new connection can be made every given interval'
)
PARSER.add_argument(
    '-i',
    '--interval',
    type=float,
    default=1,
    help='Time interval between tcp pings in seconds'
)
PARSER.add_argument(
    '-t',
    '--timeout',
    type=float,
    default=0.9,
    help='Time to wait for a tcp syn/ack from the destination host in seconds'
)
PARSER.add_argument(
    '-v',
    '--verbose',
    action='store_true',
    help='Enable verbose output'
)
PARSER.add_argument(
    'host',
    type=str,
    help='host to tcp ping'
)
PARSER.add_argument(
    'port',
    type=int,
    help='tcp port on host to tcp ping'
)

PARSER.print_help()
