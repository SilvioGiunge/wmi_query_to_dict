#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-


from wmi_query_to_dict import wmi_parse
from wmi_query_to_dict import wmi_query


def main():
    wmi = wmi_query.wmi_query(opts=_opts)
    wmi.run()
    for x in wmi.data_dict[wmi.name()]:
        print "\n\t{}\n".format(wmi.name())
        for y in wmi.get_item_keys():
            print " {}:\t{}".format(y, wmi.data_dict[wmi.name()][x][y])
    print "\n"


if __name__ == "__main__":
    _opts = vars(wmi_parse.set_parser())
    main()
