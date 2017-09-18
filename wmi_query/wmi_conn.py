#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
#
# This file was created usinw.g example the python library impacket.
# Impacket project: https://github.com/CoreSecurity/impacket
#


from impacket.dcerpc.v5.dcom import wmi
from impacket.dcerpc.v5.dtypes import NULL
from impacket.dcerpc.v5.dcomrt import DCOMConnection


def wmi_conn(address, username, password, domain, namespace, query):
    _dcom = DCOMConnection(address, username, password, domain, oxidResolver=True, doKerberos=False, kdcHost=address)
    _interface = _dcom.CoCreateInstanceEx(wmi.CLSID_WbemLevel1Login, wmi.IID_IWbemLevel1Login)
    _web_level1_login = wmi.IWbemLevel1Login(_interface)
    _iwb_nt_login = _web_level1_login.NTLMLogin(namespace, NULL, NULL)
    _iwb_class_object = _iwb_nt_login.ExecQuery(query)

    return _iwb_class_object
