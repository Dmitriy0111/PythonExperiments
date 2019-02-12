from io_class import io

class interface(io):
    def __init__(self, slave_ports, name, suffix, comment=""):
        self.ports  = slave_ports
        self.name   = name
        self.suffix = suffix
        self.comment = comment
    def print_info(self):
        print(self.name)
        count = 0
        last = 0
        for port in self.ports:
            count = count + 1
            last = 1 if count == len(self.ports) else 0
            port.print_info(last)
    def print_dec(self):
        print("    // " + self.name)
        for port in self.ports:
            port.print_dec()
