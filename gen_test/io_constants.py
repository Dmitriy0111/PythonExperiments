#!/usr/bin/env python3

from enum import Enum

class Dir(Enum):
    input = 0
    output = 1
    inout = 2

class M_S(Enum):
    slave = 0
    master = 1

class IO_type(Enum):
    logic = 0
    wire = 1
    reg  = 2
