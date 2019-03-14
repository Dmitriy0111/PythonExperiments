#!/usr/bin/env python3
from enum           import Enum
from io_class       import io
from io_interface   import interface
from io_module      import io_module
from os             import listdir
from os.path        import isfile, join
import os
import sys

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

# project dirs
modules_dir = "../gen_test/modules"
interfaces_dir = "../gen_test/interfaces"
output_dir = "../gen_test/out/"
# create output directory
os.makedirs(output_dir, exist_ok=True)
# read file names in module folder
module_f = [f for f in listdir(modules_dir) if isfile(join(modules_dir, f))]

module_list_dict = []
module_dict = []
mod_param = []
mod_small_comment = []

for module_f_ in module_f:
    file = open( modules_dir + "/" + module_f_ , 'r' )
    while True:
        help_s = file.readline()
        if help_s == "" :
            break
        if help_s.count("__PARAM__") :
            while True:
                help_s = file.readline()
                if help_s.count("__PORTS__") :
                    break
                mod_param.append( help_s.replace("\n", "") )
            break
    while True:
        help_s = file.readline()
        if help_s == "" :
            break
        help_s = help_s.rsplit(",")
        module_dict.append  ( 
                                {
                                    'if_name' : help_s[0],                  # interface name
                                    'preffix' : help_s[1].replace(" ",""),  # interface preffix
                                    'suffix'  : help_s[2].replace(" ",""),  # interface suffix
                                    'm_dim'   : help_s[6].replace("\n",""), # multidemential ports
                                    'm_s'     : help_s[5].replace(" ",""),  # master / slave
                                    'comment' : help_s[3].replace(" ","")   # comment
                                }
                            )
        mod_small_comment.append(help_s[4].replace(" ",""))
    module_list_dict.append (
                                {
                                    'mod_name'  : module_f_.replace(".mod",""), # module name
                                    'mods_if'   : module_dict[:],               # module interfaces
                                    'mod_sc'    : mod_small_comment[:],         # module small comment
                                    'mod_param' : mod_param[:]                  # module parameters
                                }
                            )
    file.close()
    module_dict.clear()
    mod_param.clear()
    mod_small_comment.clear()

interface_f = [f for f in listdir(interfaces_dir) if isfile(join(interfaces_dir, f))]

for module_list_dict_ in module_list_dict:
    mod_ifs_ = []
    mod_if_common = []
    for module_ in module_list_dict_['mods_if']:
        for interface_f_ in interface_f:
            if_ = []
            if module_['if_name'].count(interface_f_):
                file = open(interfaces_dir + "/" + interface_f_,'r')
                pars = file.readline()
                while True: 
                    pars = file.readline()
                    if pars == "":
                        break
                    pars = pars.rsplit(",")
                    type_io = pars[1].replace(" ","")
                    dir_io  = pars[3].replace(" ","")
                    M_S_io  = module_['m_s'].replace(" ", "")
                    if_.append  (
                                    io  (
                                            pars[0].replace(" ",""),
                                            type_io,pars[2].replace(" ",""),
                                            dir_io, 
                                            pars[4].replace("\n",""),
                                            M_S_io,
                                            module_['comment']
                                        )
                                )
                file.close()
                mod_ifs_.append(if_[:])
    j = 0
    for mod_ifs__ in mod_ifs_:
        mod_if_common.append    (
                                    interface   (
                                                    mod_ifs__,
                                                    module_list_dict_['mod_name'],
                                                    "",
                                                    module_list_dict_['mods_if'][j]['m_dim']
                                                )
                                )
        for ports in mod_ifs__:
            preffix = module_list_dict_['mods_if'][j]['preffix']
            suffix  = module_list_dict_['mods_if'][j]['suffix']
            ports.name = preffix + ports.name + suffix
            ports.comment=ports.comment.replace("{{}}",module_list_dict_['mod_sc'][j])
        j += 1

    nf_ahb_gpio_0_ = io_module(output_dir+module_list_dict_['mod_name'],mod_if_common,module_list_dict_['mod_param'])
    # generate files
    # module declaration
    if dec:
        nf_ahb_gpio_0_.module_dec()
    # port declaration
    if pl:
        nf_ahb_gpio_0_.print_pl()
    # module connection
    if con:
        nf_ahb_gpio_0_.connect()

