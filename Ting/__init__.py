#!/usr/bin/python
import socket
from argparse import ArgumentParser
from time import sleep

__author__ = "Mikhail Cherniak <mikcherniak@gmail.com>, Peter Hill <>"
__contributors__ = ["Mikhail Cherniak", "Peter Hill"]
__version__ = "1.0.0"
__maintainer__ = ["Mikhail Cherniak", "Peter Hill"]


def create_parser():
    """
    :return: ArgumentParser()
    """
    parser = ArgumentParser(
        description='Send a tcp syn packet to a host/port to see if '
                    'a new connection can be made every given interval'
    )
    parser.add_argument(
        '-i',
        '--interval',
        type=float,
        default=1,
        help='Time interval between tcp pings in seconds'
    )
    parser.add_argument(
        '-t',
        '--timeout',
        type=float,
        default=1,
        help='Time to wait for a tcp syn/ack from '
             'the destination host in seconds'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    parser.add_argument(
        'host',
        type=str,
        help='host to tcp ping'
    )
    parser.add_argument(
        'port',
        type=int,
        help='tcp port on host to tcp ping'
    )
    return parser.parse_args()


ARGS = create_parser()


def main():
    try:
        sockets = socket.getaddrinfo(ARGS.host, ARGS.port,
                                     socket.AF_INET, socket.SOCK_STREAM)
        while True:
            ting(sockets)
            sleep(ARGS.interval)
    except (KeyboardInterrupt, SystemExit):
        pass
    except socket.gaierror:
        print('{} - unable to resolve host'.format(ARGS.host))


def ting(sockets):
    """
    :param sockets:
    :return: bool
    """
    for sock in sockets:
        if check_socket(sock[4][0], sock[4][1], sock[0]):
            print("{} - {}:{} - OPEN".format(ARGS.host,
                                             sock[4][0], sock[4][1]))
        else:
            print("{} - {}:{} - CLOSED".format(ARGS.host,
                                               sock[4][0], sock[4][1]))


def check_socket(host, port, proto):
    """
    :param host: str
    :param port: str
    :param proto: socket.socket
    :return: bool
    """
    try:
        connected = False
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
    except socket.gaierror:
        return False
    except socket.error:
        return False
    except Exception as e:
        print(e)
