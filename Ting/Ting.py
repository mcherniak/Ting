#!/usr/bin/python
import socket
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description='Somestuff')
    parser.add_argument(
        '--host', type=str, help="Host", required=True)
    parser.add_argument(
        'port', help="some stuff", type=str)
    args = parser.parse_args()
    return args


def ting(sockets):
    for sock in sockets:
        print '{} {}'.format(sock[4][0], sock[4][1])
        if check_socket(sock[4][0], sock[4][1]):
            print True
    print False


def check_socket(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((host, int(port)))
        if sock:
            connected = True
        sock.shutdown(2)
        sock.close()
        return connected
    except socket.gaierror as e:
        print "caught: {}".format(e)
        return False
    except socket.error as e:
        print "caught: {}".format(e)
        return False


def main():
    args = get_args()
    sockets = socket.getaddrinfo(args.host, args.port)
    ting(sockets)

if __name__ == '__main__':
    main()
