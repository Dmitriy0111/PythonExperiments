#!/usr/bin/env python3

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
        return str( "    {:<8s}{:<8s}[{:<{}s} : 0]{:s}{:<{}s}{:s}"
                    .format (
                                "inout" if ( self.direction == "inout" ) else ( "input" if ( ( self.direction == "input" ) ^ (self.master == "slave") ) else "output" ),
                                self.type, 
                                (str(int(self.width)-1)) if str(self.width).isdigit() else (self.width + "-1"),
                                size1 + (2 if param1 else 0),
                                " " * size2,
                                self.name + ("" if last else ","),
                                max2,
                                self.comment
                            )
                )
    # print port
    def print_p(self, size1 = 0, param1 = False, size2 = 0, max2 = 0):
        return str( "    {:<8s}[{:<{}s} : 0]{:s}{:<{}s}    {:s}\n"
                    .format(
                                self.type, 
                                (str(int(self.width)-1)) if str(self.width).isdigit() else self.width + "-1", 
                                size1 + (2 if param1 else 0),
                                " " * size2,
                                self.name + ";", 
                                max2,
                                self.comment
                            )
                )
    # print connect with the same
    def print_con(self, last, connecting_name, size1 = 0):
        return str( "        {:<{}s}( {:<{}s}){:s}"  
                    .format (
                                "." + self.name, 
                                size1,
                                connecting_name,
                                size1,
                                "" if last else ","
                            )
                    )
    def connect(self, connecting_name, i):
        return str("        .%-23s( %-9s [%d] )," %(self.name, connecting_name, i))
