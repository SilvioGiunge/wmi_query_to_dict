#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-


import argparse


def set_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u", dest="user", action="store",
        help="User to connect on the machine."
        )
    parser.add_argument(
        "-p", dest="password", action="store",
        help="Password of the user to connect on the machine."
        )
    parser.add_argument(
        "-ip", dest="host", action="store",
        help="IP of the Host to get wmi queries. Eg: 192.168.1.1"
        )
    parser.add_argument(
        "-del", dest="delimiter", action="store", default="\|",
        help="Delimiter for queries. Default: |"
        )
    parser.add_argument(
        "-d", dest="domain", action="store",
        help="Delimiter for queries. Default: |"
        )
    parser.add_argument(
        "-n", dest="namespace", action="store", default="ROOT/cimv2",
        help="Namespace for classes. Default: ROOT/cimv2"
        )
    parser.add_argument(
        "-q", dest="query", action="store",
        help="Query to consult wmi databases. Eg: 'SELECT * FROM Win32_process'"
        )

    return parser.parse_args()
