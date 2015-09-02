Ting: TCP Ping Utility
======================

Ting is a pure python implementation of tcp ping. For each interval period, a TCP socket is attempted to be opened
to the destination host and port. If successful, we then close the connection and wait till the next interval.

For each interval, we report success or failure.

Installation
------------
Ting can be installed either using pip or manually, by running setup.py

Usage
-----
```python
usage: ting [-h] [-i INTERVAL] [-t TIMEOUT] [-v] host port

Send a tcp syn packet to a host/port to see if a new connection can be made
every given interval

positional arguments:
  host                  host to tcp ping
  port                  tcp port on host to tcp ping

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        Time interval between tcp pings in seconds
  -t TIMEOUT, --timeout TIMEOUT
                        Time to wait for a tcp syn/ack from the destination
                        host in seconds
  -v, --verbose         Enable verbose output
```