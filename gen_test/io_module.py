from io_interface import interface

class io_module(interface):
    def __init__(self, name, interfaces, params = ""):
        self.name       = name
        self.interfaces = interfaces
        self.params     = params
    def find_max_lenght(self):
        max1 = 0
        max2 = 0
        param = False
        for interface_ in self.interfaces:
            for port in interface_.ports:
                max1 = len( str(int(port.width) - 1) if str(port.width).isdigit() else str(port.width) ) if max1 < len(str(int(port.width) - 1) if str(port.width).isdigit() else str(port.width)) else max1
                param = True if ( str(port.width).isdigit() == False ) | (param == True) else False
                max2 = len(port.name) if len(port.name) > max2 else max2
        return max1 , param , max2
    def print(self):
        size1 , param1, max2 = self.find_max_lenght() 
        size2 =  ( 2 if param1 else 0 )
        size2_ = 0
        max2_ = 0
        while size2_-1 < size2:
            size2_ = size2_ + 4
        size2_ = size2_ - size2
        while max2_-1 < max2:
            max2_ = max2_ + 4
        count = 0
        file_name = open(self.name+"_pl"+".sv","w")
        for interface_ in self.interfaces:
            interface_.print_dec(file_name, size1, param1, size2, max2)
        file_name.close()
    def connect(self):
        size1 , param1, max2 = self.find_max_lenght()
        max2 = max2 + 5
        file_name = open(self.name+"_con"+".sv","w")
        file_name.write( str( "    // Creating one %s" %(self.interfaces[0].name+self.interfaces[0].suffix+("_0" if self.interfaces[0].suffix == "" else "") ) )+"\n" )
        file_name.write( str( "    %s %s" %(self.interfaces[0].name, self.interfaces[0].name+"_0") )+"\n" )
        file_name.write( "    (" +"\n" )
        for interface_ in self.interfaces:
            file_name.write( str( "        // %s" %interface_.comment )+"\n" )
            for port in interface_.ports:
                file_name.write( port.connect_0(port.name,max2) +"\n" )
        file_name.write( "    );" +"\n" )
        file_name.close()
    def module_dec(self):
        size1 , param1, max2 = self.find_max_lenght() 
        size2 = size1 + 6 + ( 2 if param1 else 0 )
        size2_ = 0
        max2_ = 0
        while size2_-1 < size2:
            size2_ = size2_ + 4
        size2_ = size2_ - size2
        while max2_-1 < max2:
            max2_ = max2_ + 4
        count = 0

        for interface_ in self.interfaces:
            count += len(interface_.ports)
        i = 0
        file_name = open(self.name+"_dec"+".sv","w")
        file_name.write( str("module %s" %(self.interfaces[0].name) +"\n" ) )
        if len(self.params) != 0:
            file_name.write( "#(" +"\n" )
            for param in self.params:
                i = i + 1
                file_name.write ( str( "    parameter%s%s%s"  %(
                                                                    " " * (7 + size2_ + size2),
                                                                    param,
                                                                    "" if len(self.params) == i else ","
                                                                )     
                                    ) +"\n" 
                                )
            file_name.write( ")(" +"\n" )
        else:
            file_name.write( "(" +"\n" )
        i = 0
        for interface_ in self.interfaces:
            file_name.write( str("    // %s" %interface_.comment ) + "\n" )
            for port in interface_.ports:
                i = i + 1
                file_name.write(port.print_io(0 if i != count else 1, size1, param1, size2_,max2_) + "\n")
        file_name.write( ");" +"\n" )
        file_name.write( "" +"\n" )
        file_name.write( str("endmodule : %s" %(self.interfaces[0].name) ) + "\n" )
        file_name.close()
