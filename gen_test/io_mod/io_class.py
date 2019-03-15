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
    # print port declaration or port list
    def print_dec_pl(self, last, size_f = 0, param_f = False, size_space_e = 0, size_name_e = 0, size_s = 0, param_s = False, two_dim = False, dec_pl = 0, tab_size = 4, size_dir_e = 0, size_type_e = 0):
        return str( "{:s}{:<{}s}{:<{}s}{:<{}s}{:s}[{:<{}s} : 0]{:s}{:<{}s}{:s}\n"
                    .format (
                                " " * ( tab_size ),
                                ( "inout" if ( self.direction == "inout" ) else ( "input" if ( ( self.direction == "input" ) ^ (self.master == "slave") ) else "output" ) ) if dec_pl == 1 else "",
                                size_dir_e if dec_pl == 1 else 0,
                                self.type, 
                                size_type_e,
                                "" if two_dim == False else ( ( "[" + ( ( str( int( self.width_s ) - 1 ) ) if str( self.width_s ).isdigit() else ( self.width_s + "-1" ) ) ) if ( str(self.width_s) != "" ) else "   " ),
                                0 if ( two_dim == False ) else ( size_s + ( 2 if param_s else 0 ) + ( 1 if two_dim else 0 ) ),
                                "" if ( two_dim == False ) else (" : 0]" if ( str(self.width_s) != "" ) else "    " + (" " if param_s else "")),
                                ( str( int( self.width_f ) - 1 ) ) if str( self.width_f ).isdigit() else ( self.width_f + "-1" ),
                                size_f + (2 if param_f else 0),
                                " " * size_space_e,
                                self.name + ( ("" if last else ",") if dec_pl == 1 else ";" ),
                                size_name_e,
                                self.comment
                            )
                )
    # print connect with the same
    def print_con(self, last, connecting_name, size_name_e = 0, tab_size = 4):
        return str( "{:s}{:<{}s}( {:<{}s}){:s}{:s}"  
                    .format (
                                " " * ( tab_size * 2 ),
                                "." + self.name, 
                                size_name_e,
                                connecting_name,
                                size_name_e,
                                "   " if last else ",  ",
                                self.comment
                            )
                    )
