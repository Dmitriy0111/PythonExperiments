# import
from enum           import Enum
from io_class       import io
from io_constants   import M_S
from io_constants   import Dir
from io_constants   import IO_type
from io_interface   import interface
from io_module      import io_module
from os             import listdir
from os.path        import isfile, join
import os
import sys
import copy

dec = 0
pl  = 0
con = 0
# read script params
for param in sys.argv:
    if param == "dec":
        dec = 1
    if param == "pl":
        pl = 1
    if param == "con":
        con = 1

def connect(AHB_list, AHB_master):
    print("    // Creating one %s" %(AHB_master.name+AHB_master.suffix+("_0" if AHB_master.suffix == "" else "")))
    print("    %s %s" %(AHB_master.name, AHB_master.name+"_0"))
    print("    (")
    for port in AHB_master.ports:
        print(port.connect_0(port.name))
    print("    );")
    s=0
    for AHB_list_ in AHB_list:
        print("    // Creating one %s" %(AHB_list_.name+AHB_list_.suffix+("_0" if AHB_list_.suffix == "" else "")))
        print("    %s %s" %(AHB_list_.name, AHB_list_.name+AHB_list_.suffix+("_0" if AHB_list_.suffix == "" else "")))
        print("    (")
        i=0
        for port in AHB_list_.ports:
            print(port.connect(AHB_master.ports[i].name,s))
            i = i + 1
        s = s + 1
        print("    );")
# project dirs
modules_dir = "../gen_test/modules"
interfaces_dir = "../gen_test/interfaces"
output_dir = "../gen_test/out/"
# create output directory
os.makedirs(output_dir, exist_ok=True)
# read file names in module folder
module_f = [f for f in listdir(modules_dir) if isfile(join(modules_dir, f))]

j = 0

module_list = []
module = []

for module_f_ in module_f:
    file = open( modules_dir + "/" + module_f_ , 'r' )
    while True:
        help_s = file.readline()
        if help_s == "" :
            break
        help_s = help_s.rsplit(",")
        module.append( [help_s[0],help_s[1].replace(" ",""),help_s[2].replace("\n","")] )
    module_list.append([module_f_.replace(".mod",""),copy.deepcopy(module)])
    file.close()
    module.clear()
# read interface names in interface folder
interface_f = [f for f in listdir(interfaces_dir) if isfile(join(interfaces_dir, f))]

for module_list_ in module_list:
    mod_ifs_ = []
    mod_if_common = []
    for module_ in module_list_[1]:
        for interface_f_ in interface_f:
            if_ = []
            if module_[0].count(interface_f_):
                file = open(interfaces_dir + "/" + interface_f_,'r')
                pars = file.readline()
                while True: 
                    pars = file.readline()
                    if pars == "":
                        break
                    pars = pars.rsplit(",")
                    type_io = pars[1].replace(" ","")
                    type_io = IO_type.logic if type_io == "logic" else ( IO_type.wire if type_io == "wire" else ( ( IO_type.reg if type_io == "reg" else "error")))
                    dir_io  = pars[3].replace(" ","")
                    dir_io  = Dir.output if dir_io == "output" else ( Dir.input if dir_io == "input" else ( Dir.inout if dir_io == "inout" else "error"))
                    M_S_io  = pars[4].replace(" ","")
                    M_S_io  = M_S.master if M_S_io == "master" else ( M_S.slave if M_S_io == "slave" else "error")
                    if_.append(io(pars[0].replace(" ",""),type_io,pars[2].replace(" ",""),dir_io,M_S_io, pars[5].replace("\n","")))
                file.close()
                mod_ifs_.append(copy.deepcopy(if_))
    j = 0
    for mod_ifs__ in mod_ifs_:
        mod_if_common.append(interface(mod_ifs__ , module_list_[0] , "" ,  module_list_[1][j][2] ))
        j = j + 1
    j = 0
    for mod_ifs__ in mod_ifs_:
        for ports in mod_ifs__:
            ports.name = ports.name + module_list_[1][j][1]
        j = j + 1

    param_ = ["gpio_w = `NF_GPIO_WIDTH", "pwm_width = 8" ]

    nf_ahb_gpio_0_ = io_module(output_dir+module_list_[0],mod_if_common,param_)
    #generate files
    if dec:
        nf_ahb_gpio_0_.module_dec()
    if pl:
        nf_ahb_gpio_0_.print()
    if con:
        nf_ahb_gpio_0_.connect()
