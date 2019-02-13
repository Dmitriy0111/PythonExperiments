# Complex class
from enum           import Enum
from io_class       import io
from io_constants   import M_S
from io_constants   import Dir
from io_constants   import IO_type
from io_interface   import interface
from io_module      import module
from os             import listdir
from os.path        import isfile, join
import copy

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

    
module_if = [ 
                [ "clk_reset.if" , "_s"   , "clock and reset"  ],
                [ "clk_reset.if" , ""     , "clock and reset"  ], 
                [ "ahb.if"       , "_m_0" , "AHB master side"  ], 
                [ "ahb.if"       , "_m_1" , "AHB master side"  ], 
                [ "ahb.if"       , "_m_2" , "AHB master side"  ], 
                [ "ahb.if"       , "_m_3" , "AHB master side"  ], 
                [ "ahb.if"       , "_m_4" , "AHB master side"  ], 
                [ "ahb.if"       , "_m_5" , "AHB master side"  ], 
                [ "ahb.if"       , "_m_6" , "AHB master side"  ], 
                [ "ahb.if"       , "_m_7" , "AHB master side"  ], 
                [ "gpio.if"      , ""     , "GPIO side"        ], 
                [ "pwm.if"       , ""     , "PWM side"         ]
            ]

files = [f for f in listdir("../gen_test/interfaces") if isfile(join("../gen_test/interfaces", f))]
i = 0
j = 0
file_list = []

if__ = []
if__complete = []


for module_ifs in module_if:
    for f in files:
        if module_ifs[0].count(f):
            file_list.append( open("../gen_test/interfaces/" + module_ifs[0],'r') )
        i = i + 1

for file in file_list:
    pars = file.readline()
    while True: 
        pars = file.readline()
        if pars == "":
            break
        pars = pars.rsplit(",")
        type_io = pars[1].replace(" ","")
        type_io = IO_type.logic if type_io == "logic" else ( IO_type.wire if type_io == "wire" else ( ( IO_type.reg if type_io == "reg" else "error")))
        dir_io  = pars[3].replace(" ","")
        dir_io  = Dir.output if dir_io == "output" else ( Dir.input if dir_io == "input" else "error")
        M_S_io  = pars[4].replace(" ","")
        M_S_io  = M_S.master if M_S_io == "master" else ( M_S.slave if M_S_io == "slave" else "error")
        if__.append(io(pars[0].replace(" ",""),type_io,pars[2].replace(" ",""),dir_io,M_S_io, pars[5].replace("\n","")))
    if__complete.append(copy.deepcopy(if__))
    if__.clear()

if_1_ = []

if_subname = "gpio"
if_suffix  = ""

j = 0
for if__complete_ in if__complete:
    if_1_.append(interface(if__complete_ , "nf_ahb_" + if_subname , if_suffix , module_if[j][2] ))
    j = j + 1

j = 0
for if_1_p in if__complete:
    for ports in if_1_p:
        ports.name = ports.name + module_if[j][1]
    j = j + 1

param_ = ["gpio_w = `NF_GPIO_WIDTH", "pwm_width = 8" ]

nf_ahb_gpio_0_ = module(if_1_,param_)

nf_ahb_gpio_0_.print()
nf_ahb_gpio_0_.connect()
nf_ahb_gpio_0_.module_dec()
