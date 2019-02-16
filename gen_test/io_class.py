#!/usr/bin/env python3

from io_constants import M_S
from io_constants import Dir
from io_constants import IO_type

class io():
    def __init__(self, name, type, width, direction, comment, master):
        self.name       = name
        self.type       = type
        self.width      = width
        self.direction  = direction
        self.comment    = comment
        self.master     = master
    # print port declaration
    def print_dec(self, last, size1 = 0, param1 = False, size2 = 0, max2 = 0):
        return str("    %-6s  %-5s   [%-s%s : 0]%s%s%s%s" %(
                                                                        "inout" if ( self.direction == Dir.inout ) else ( "input" if ( ( self.direction == Dir.input ) ^ (self.master == M_S.slave) ) else "output" ),
                                                                        self.type.name, 
                                                                        (int(self.width)-1) if str(self.width).isdigit() else self.width + "-1",
                                                                        " " * ( size1 - len( str( int(self.width)-1 ) if str(self.width).isdigit() else self.width) + ( 2 if str(self.width).isdigit() & param1 else 0 ) ),
                                                                        " " * size2,
                                                                        self.name + ("" if last else ","),
                                                                        " " * (max2 - len(self.name) - (1 if last == 0 else 0)),
                                                                        self.comment
                                                                    )
                )
    # print port
    def print_p(self, size1 = 0, param1 = False, size2 = 0, max2 = 0):
        return str("    %-5s   [%-s%s : 0]%s%-s%s    %s\n"      %(
                                                                    self.type.name, 
                                                                    (int(self.width)-1) if str(self.width).isdigit() else self.width + "-1", 
                                                                    " " * ( size1 - len( str( int(self.width)-1 ) if str(self.width).isdigit() else self.width) + ( 2 if str(self.width).isdigit() & param1 else 0 ) ),
                                                                    " " * size2,
                                                                    self.name + ";", 
                                                                    " " * (max2 - len(self.name) + 1 ),
                                                                    self.comment
                                                                )
                )
    # print connect with the same
    def print_con(self, last, connecting_name, size1 = 0):
        return str  ("        .%-s%s( %-s%s)%s"  %(
                                                    self.name, 
                                                    " " * ( size1 - len(self.name)),
                                                    connecting_name,
                                                    " " * ( size1 - len(connecting_name) ),
                                                    "" if last else ","
                                                )
                    )
    def connect(self, connecting_name, i):
        return str("        .%-23s( %-9s [%d] )," %(self.name, connecting_name, i))
