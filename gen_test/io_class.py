#!/usr/bin/env python3

class io():
    def __init__(self, name, type, width_f, direction, comment, master, width_s = ""):
        self.name       = name
        self.type       = type
        self.width_f    = width_f
        self.direction  = direction
        self.comment    = comment
        self.master     = master
        self.width_s    = width_s
    # print port declaration
    def print_dec(self, last, size1 = 0, param1 = False, size2 = 0, max2 = 0, size_s = 0, param_s = False, two_dim = False):
        return str( "    {:<8s}{:<8s}{:<{}s}{:s}[{:<{}s} : 0]{:s}{:<{}s}{:s}"
                    .format (
                                "inout" if ( self.direction == "inout" ) else ( "input" if ( ( self.direction == "input" ) ^ (self.master == "slave") ) else "output" ),
                                self.type, 
                                "" if two_dim == False else ( ( "[" + ( ( str( int( self.width_s ) - 1 ) ) if str( self.width_s ).isdigit() else ( self.width_s + "-1" ) ) ) if ( str(self.width_s) != "" ) else "   " ),
                                0 if ( two_dim == False ) else ( size_s + ( 2 if param_s else 0 ) + ( 1 if two_dim else 0 ) ),
                                "" if ( two_dim == False ) else (" : 0]" if ( str(self.width_s) != "" ) else "     "),
                                ( str( int( self.width_f ) - 1 ) ) if str( self.width_f ).isdigit() else ( self.width_f + "-1" ),
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
                                (str(int(self.width_f)-1)) if str(self.width_f).isdigit() else self.width_f + "-1", 
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
