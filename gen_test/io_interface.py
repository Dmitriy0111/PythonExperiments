#!/usr/bin/env python3

from io_class import io

class interface(io):
    def __init__(self, slave_ports, name, suffix, comment=""):
        self.ports  = slave_ports
        self.name   = name
        self.suffix = suffix
        self.comment = comment
    # print port list
    def print_pl(self, file_name, size1 = 0, param1 = False, size2 = 0, max2 = 0):
        if self.comment != "":
            file_name.write( str("    // " + self.comment + "\n") )
        for port in self.ports:
            file_name.write( port.print_p( size1, param1, size2, max2 ) )
