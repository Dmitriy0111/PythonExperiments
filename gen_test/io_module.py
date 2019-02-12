from io_interface import interface

class module(interface):
    def __init__(self, interfaces, params = ""):
        self.interfaces = interfaces
        self.params     = params
    def print(self):
        for interface_ in self.interfaces:
            interface_.print_dec()
    def connect(self):
        print("    // Creating one %s" %(self.interfaces[0].name+self.interfaces[0].suffix+("_0" if self.interfaces[0].suffix == "" else "")))
        print("    %s %s" %(self.interfaces[0].name, self.interfaces[0].name+"_0"))
        print("    (")
        for interface_ in self.interfaces:
            print("        // %s" %interface_.name)
            for port in interface_.ports:
                print(port.connect_0(port.name))
        print("    );")
    def module_dec(self):
        count = 0
        for interface_ in self.interfaces:
            count += len(interface_.ports)
        i = 0
        print("module %s" %(self.interfaces[0].name))
        if len(self.params) != 0:
            print("#(")
            for param in self.params:
                print("    parameter                           %s" %param)
            print(")(")
        else:
            print("(")
        for interface_ in self.interfaces:
            print("    // %s" %interface_.comment)
            for port in interface_.ports:
                i = i + 1
                print(port.print_io(0 if i != count else 1))
        print(");")
        print("")
        print("endmodule : %s" %(self.interfaces[0].name))
