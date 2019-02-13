from io_constants import M_S
from io_constants import Dir
from io_constants import IO_type

class io():
    def __init__(self, name, type, width, direction, master, comment):
        self.name       = name
        self.type       = type
        self.width      = width
        self.direction  = direction
        self.master     = master
        self.comment    = comment
    def print_io(self, last, size1 = 0, param1 = False, size2 = 0, max2 = 0):
        return str("    %-6s  %-5s   [%-s%s : 0]%s%s%s%s" %(
                                                                        "input" if ( ( self.direction == Dir.input ) ^ (self.master == M_S.slave) ) else "output",
                                                                        self.type.name, 
                                                                        (int(self.width)-1) if str(self.width).isdigit() else self.width + "-1",
                                                                        " " * ( size1 - len( str( int(self.width)-1 ) if str(self.width).isdigit() else self.width) + ( 2 if str(self.width).isdigit() & param1 else 0 ) ),
                                                                        " " * size2,
                                                                        self.name + ("" if last else ","),
                                                                        " " * (max2 - len(self.name) - (1 if last == 0 else 0)),
                                                                        self.comment
                                                                    )
                )
    def print_dec(self, size1 = 0, param1 = False, size2 = 0, max2 = 0):
        print   ("    %-5s   [%-s%s : 0]%s%-s%s    %s"      %(
                                                                    self.type.name, 
                                                                    (int(self.width)-1) if str(self.width).isdigit() else self.width + "-1", 
                                                                    " " * ( size1 - len( str( int(self.width)-1 ) if str(self.width).isdigit() else self.width) + ( 2 if str(self.width).isdigit() & param1 else 0 ) ),
                                                                    " " * size2,
                                                                    self.name + ";", 
                                                                    " " * (max2 - len(self.name) + 1 ),
                                                                    self.comment
                                                                )
                )
    def connect_0(self, connecting_name):
        return str("        .%-23s( %-14s)," %(self.name, connecting_name))
    def connect(self, connecting_name, i):
        return str("        .%-23s( %-9s [%d] )," %(self.name, connecting_name, i))
