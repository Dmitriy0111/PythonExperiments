from io_interface import interface

class module(interface):
    def __init__(self, interfaces, params = ""):
        self.interfaces = interfaces
        self.params     = params
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
        for interface_ in self.interfaces:
            interface_.print_dec(size1, param1, size2, max2)
    def connect(self):
        print("    // Creating one %s" %(self.interfaces[0].name+self.interfaces[0].suffix+("_0" if self.interfaces[0].suffix == "" else "")))
        print("    %s %s" %(self.interfaces[0].name, self.interfaces[0].name+"_0"))
        print("    (")
        for interface_ in self.interfaces:
            print("        // %s" %interface_.comment)
            for port in interface_.ports:
                print(port.connect_0(port.name))
        print("    );")
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
        print("module %s" %(self.interfaces[0].name))
        if len(self.params) != 0:
            print("#(")
            for param in self.params:
                i = i + 1
                print("    parameter%s%s%s" %(
                                                " " * (7 + size2_ + size2),
                                                param,
                                                "" if len(self.params) == i else ","
                                            )
                    )
            print(")(")
        else:
            print("(")
        i = 0
        for interface_ in self.interfaces:
            print("    // %s" %interface_.comment)
            for port in interface_.ports:
                i = i + 1
                print(port.print_io(0 if i != count else 1, size1, param1, size2_,max2_))
        print(");")
        print("")
        print("endmodule : %s" %(self.interfaces[0].name))
