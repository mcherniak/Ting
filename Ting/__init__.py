#!/usr/bin/python
from argparse import ArgumentParser
import socket


__author__ = "Mikhail Cherniak <mikcherniak@gmail.com>, Peter Hill <>, Nathan Sutherland <nathan.sutherland@gmail.com"
__contributors__ = ["Mikhail Cherniak", "Peter Hill", "Nathan Sutherland"]
__version__ = "1.0.0"
__maintainer__ = ["Mikhail Cherniak", "Peter Hill"]


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
    default=1,
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

ARGS = PARSER.parse_args()


def main():
    sockets = socket.getaddrinfo(ARGS.host, ARGS.port, 0, socket.SOCK_STREAM)
    ting(sockets)


def ting(sockets):
    for sock in sockets:
        print '{} {}'.format(sock[4][0], sock[4][1])
        if check_socket(sock[4][0], sock[4][1], sock[0]):
            print True
        else:
            print False


def check_socket(host, port, proto):
    try:
        if proto == 30:
            sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(ARGS.timeout)
        sock.connect((host, int(port)))
        if sock:
            connected = True
        sock.shutdown(2)
        sock.close()
        return connected
    except socket.gaierror as e:
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        sock.settimeout(ARGS.timeout)
        print "gaierror caught: {}".format(e)
        return False
    except socket.error as e:
        print "error caught: {}".format(e)
        return False
