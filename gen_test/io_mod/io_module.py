#!/usr/bin/env python3

from .io_interface import interface

class module(interface):
    def __init__(self, name, interfaces, params = "", tab_size = 3):
        self.name       = name
        self.interfaces = interfaces
        self.params     = params
        self.tab_size   = tab_size
    def find_max_lenght(self):
        size_f    = 0
        size_s    = 0
        param_f   = False
        param_s   = False
        two_dim   = False
        size_name = 0
        size_dir  = 0
        size_type = 0
        for interface_ in self.interfaces:
            for port in interface_.ports:
                size_f  = len( str(int(port.width_f) - 1) if str(port.width_f).isdigit() else str(port.width_f) ) if size_f < len(str(int(port.width_f) - 1) if str(port.width_f).isdigit() else str(port.width_f)) else size_f
                size_s  = len( str(int(port.width_s) - 1) if str(port.width_s).isdigit() else str(port.width_s) ) if size_s < len(str(int(port.width_s) - 1) if str(port.width_s).isdigit() else str(port.width_s)) else size_s
                param_f = True if ( str( port.width_f ).isdigit() == False ) | ( param_f == True ) else False
                param_s = True if ( ( str( port.width_s ).isdigit() == False ) & ( str( port.width_s ) != "" ) ) | ( param_s == True ) else False
                two_dim = True if ( ( str( port.width_s ) != "" ) | ( two_dim == True ) ) else False
                size_name = len( port.name ) if len( port.name ) > size_name else size_name
                size_dir  = len( port.direction ) if len( port.direction ) > size_dir else size_dir
                size_type = len( port.type ) if len( port.type ) > size_type else size_type
        return size_f , param_f , size_name, size_s, param_s, two_dim, size_dir, size_type
    def calibrate_dec_pl(self, size_f , param_f, size_name, size_s, param_s, two_dim, size_dir  = 0, size_type = 0):

        size_name_e  = 0
        size_dir_e   = 0
        size_type_e  = 0
        while size_name_e - (self.tab_size - 0) < size_name:
            size_name_e += self.tab_size
        while size_dir_e - (self.tab_size - 0) < size_dir:
            size_dir_e += self.tab_size
        while size_type_e - (self.tab_size - 0) < size_type:
            size_type_e += self.tab_size

        size_space   = size_dir_e + size_type_e + size_f + size_s + ( 2 if param_f else 0 ) + ( 2 if param_s & two_dim else 0 ) + (6 if two_dim else 0)
        size_space_e = 0
        while size_space_e - (self.tab_size - 0) < size_space:
            size_space_e += self.tab_size
        size_space_e = size_space_e - size_space

        return size_space, size_space_e, size_name_e, size_dir_e, size_type_e
    # print port list
    def print_pl(self):
        size_f , param_f, size_name, size_s, param_s, two_dim, size_dir, size_type = self.find_max_lenght()
        size_space, size_space_e, size_name_e, size_dir_e, size_type_e = self.calibrate_dec_pl(size_f , param_f, size_name, size_s, param_s, two_dim, size_dir, size_type)

        file_name = open(self.name+"_pl"+".sv","w")

        for interface_ in self.interfaces:
            if interface_.comment != "":
                file_name.write( str( " " * ( self.tab_size ) +  "// " + interface_.comment + "\n") )
            for port in interface_.ports:
                file_name.write(port.print_dec_pl( 0, size_f, param_f, size_space_e, size_name_e, size_s, param_s, two_dim, 0, self.tab_size, size_dir_e, size_type_e ))

        file_name.close()

    def connect(self):
        size_f , param_f, size_name, size_s, param_s, two_dim, size_dir, size_type = self.find_max_lenght()
        size_space, size_space_e, size_name_e, size_dir_e, size_type_e = self.calibrate_dec_pl(size_f , param_f, size_name, size_s, param_s, two_dim)
        
        count = 0
        for interface_ in self.interfaces:
            count += len(interface_.ports)
        file_name = open(self.name+"_con"+".sv","w")
        file_name.write ( str   ( "{:s}// Creating one {:s}\n".format   (
                                                                            " " * ( self.tab_size ),
                                                                            self.interfaces[0].name+self.interfaces[0].suffix+("_0" if self.interfaces[0].suffix == "" else "") 
                                                                        ) 
                                ) 
                        )
        file_name.write ( str   ( "{:s}{:s}\n" .format  (
                                                            " " * ( self.tab_size ),
                                                            self.interfaces[0].name
                                                        ) 
                                ) 
                        )

        if len(self.params) != 0:
            file_name.write( "{:s}#(\n".format  ( " " * ( self.tab_size ) ) )
            param_len = [0,0]
            param_len[0] = max( [len(row[0]) for row in self.params] )
            param_len[1] = max( [len(row[1]) for row in self.params] )
            
            for j in range(len(self.params)):
                file_name.write ( str( "{:s}.{:<{}s} ( {:<{}s}){:s}".format   (
                                                                                " " * ( self.tab_size * 2 ),
                                                                                self.params[j][0],
                                                                                param_len[0],
                                                                                self.params[j][1],
                                                                                param_len[1],
                                                                                "" if len( [row[0] for row in self.params] ) - 1 == j else ","
                                                                            )     
                                        ) +"\n" 
                                )
            file_name.write( "{:s})\n".format  ( " " * ( self.tab_size ) ) )

        file_name.write( str( "{:s}{:s}\n" .format( " " * ( self.tab_size ) , self.interfaces[0].name+"_0") ) )
        file_name.write( "{:s}(\n".format  ( " " * ( self.tab_size ) ) )
        i = 0
        for interface_ in self.interfaces:
            if interface_.comment != "":
                file_name.write( str( "{:s}// {:s}\n".format( " " * ( self.tab_size * 2 ) , interface_.comment ) ) )
            for port in interface_.ports:
                i += 1
                file_name.write( port.print_con(0 if i != count else 1, port.name,size_name_e, self.tab_size) +"\n" )
        file_name.write( "{:s});\n".format  ( " " * ( self.tab_size ) ) )
        file_name.close()
    # print module declaration
    def module_dec(self):
        size_f , param_f, size_name, size_s, param_s, two_dim, size_dir, size_type = self.find_max_lenght() 
        size_space, size_space_e, size_name_e, size_dir_e, size_type_e = self.calibrate_dec_pl(size_f , param_f, size_name, size_s, param_s, two_dim, size_dir, size_type)
        print( size_space_e + size_space + 7 )

        count = 0
        for interface_ in self.interfaces:
            count += len(interface_.ports)

        file_name = open(self.name+"_dec"+".sv","w")
        file_name.write( str("module {:s}\n".format(self.interfaces[0].name) ) )
        if len(self.params) != 0:
            file_name.write( "#(\n" )
            param_len = 0
            for param in self.params:
                param_len = len(param[0]) if len(param[0]) > param_len else param_len
            
            for j in range(len(self.params)):
                file_name.write ( str( "{:s}parameter{:s}{:<{}s} = {:s}{:s}".format (
                                                                                        " " * self.tab_size,
                                                                                        " " * (7 + size_space_e + size_space - 10),
                                                                                        self.params[j][0],
                                                                                        param_len,
                                                                                        self.params[j][1],
                                                                                        "" if len( [row[0] for row in self.params] ) - 1 == j else ","
                                                                                    )     
                                     ) +"\n" 
                                )
            file_name.write( ")(\n" )
        else:
            file_name.write( "(\n" )
        i = 0
        for interface_ in self.interfaces:
            if interface_.comment != "":
                file_name.write( str("{:s}// {:s}\n".format( " " * self.tab_size, interface_.comment ) ) )
            for port in interface_.ports:
                i += 1
                file_name.write(port.print_dec_pl(0 if i != count else 1, size_f, param_f, size_space_e,size_name_e,size_s,param_s,two_dim,1,self.tab_size,size_dir_e,size_type_e) )
                
        file_name.write( ");\n" )
        file_name.write( "\n" )
        file_name.write( str("endmodule : {:s}\n".format(self.interfaces[0].name) ) )
        file_name.close()
