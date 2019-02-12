from io_constants import M_S
from io_constants import Dir

class io():
    def __init__(self, name, type, width, direction, master, comment, param = False):
        self.name       = name
        self.type       = type
        self.width      = width
        self.direction  = direction
        self.master     = master
        self.comment    = comment
        self.param      = param
    def print_io(self, last):
        return str("    %-6s  %-5s   [%-2s : 0]    %-16s    %s" %(
                                                                        "input" if ( ( self.direction == Dir.input ) ^ (self.master == M_S.slave) ) else "output",
                                                                        self.type, 
                                                                        (self.width-1) if self.param == False else self.width + "-1", 
                                                                        self.name + ("" if last else ","), 
                                                                        self.comment
                                                                    )
                )
    def print_dec(self):
        print   ("    %-5s   [%-2s : 0]    %-16s    %s"      %(
                                                                    self.type, 
                                                                    (self.width-1) if self.param == False else self.width + "-1", 
                                                                    self.name + ";", 
                                                                    self.comment
                                                                )
                )
    def connect_0(self, connecting_name):
        return str("        .%-23s( %-14s)," %(self.name, connecting_name))
    def connect(self, connecting_name, i):
        return str("        .%-23s( %-9s [%d] )," %(self.name, connecting_name, i))
