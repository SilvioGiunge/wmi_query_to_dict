#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-


import re
import sys
from subprocess import check_output
from collections import defaultdict


class wmi_query(object):

    def __init__(self, opts):
        print opts
        self.user = opts['user']
        self.password = opts['password']
        self.host = opts['host']
        self.domain = opts['domain']
        self.delimiter = opts['delimiter']
        self.namespace = opts['namespace']
        self.query = opts['query']
        self.wmic = "/usr/local/bin/wmic -U {}/{}%{} --namespace {} --delimiter {} //{} '{}'".format(
                self.domain.upper(), self.user, self.password, self.namespace, self.delimiter, self.host, self.query)
        self.pattern = re.compile(r"CLASS:\ ")
        self.data_dict = defaultdict()

    def check_wmi_data(self, wmi_data):
        if(len(wmi_data) % 3 != 0 or not self.pattern.match(wmi_data[0])):
            print "Error founded on wmi output data. Exiting...\n"
            sys.exit(0)
        else:
            return re.sub("", wmi_data[0])

    def get_wmi_data(self):
        _wmi_data = filter(None, check_output([self.wmic], shell=True).split('\n'))
        _dict_name = self.check_wmi_data(_wmi_data)
        _process_data = [zip(_wmi_data[x].split('|'), _wmi_data[x+1].split('|'))
                         for x, y in enumerate(_wmi_data) if x in range(1, len(_wmi_data), 3)]
        self.data_dict[_dict_name] = defaultdict(lambda: False)
        _cont = 0
        for data in _process_data:
            self.data_dict[_dict_name][_cont] = defaultdict(lambda: False)
            for item in data:
                self.data_dict[_dict_name][_cont][item[0]] = item[0]
            _cont = _cont + 1

    def wmi_dict(self):
        return self.data_dict
