# wmi-query
### Get wmi class object from msrpc
#### Version: 0.1.3

The script wmi-query make a query and print on the screen the wmi class object.
Both keys and values will be printed for each object returned by the query.

## USAGE:
Get wmi classes objects. Use -h to get help!

```
optional arguments:
  -h, --help    show this help message and exit
  -u USER       User to connect on the machine.
  -p PASSWORD   Password of the user to connect on the machine.
  -a ADDRESS    IP of the Host to get wmi queries. Eg: 192.168.1.1
  -d DOMAIN     Domain to check. Default: WORKGROUP.
  -n NAMESPACE  Namespace for classes. Default: ROOT/cimv2
  -q QUERY      Query to consult wmi databases. Eg: 'SELECT * FROM Win32_process'
```

## Install
```
%> python setup.py install
%> pip wmi-query install
```
### [\[PyPi\]](https://pypi.python.org/pypi/wmi-query "wmi-query on PyPi")

## Requeriment
.*Lib impacket
