#!/usr/bin/env python3

from .io_class import io

class interface(io):
    def __init__(self, slave_ports, name, suffix, comment=""):
        self.ports  = slave_ports
        self.name   = name
        self.suffix = suffix
        self.comment = comment
