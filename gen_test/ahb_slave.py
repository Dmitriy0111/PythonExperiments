# Complex class
from enum         import Enum
from io_class     import io
from io_constants import M_S
from io_constants import Dir
from io_interface import interface
from io_module    import module
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

clk_reset_ports =   [
                        io("clk"    , "logic" , 1 , Dir.output , M_S.slave , "// clk "    ),
                        io("resetn" , "logic" , 1 , Dir.output , M_S.slave , "// resetn " )
                    ]
ahb_common_ports =  [
                        io("haddr"  , "logic" , 32 , Dir.output , M_S.slave , "// AHB - Slave HADDR "      ),
                        io("hwdata" , "logic" , 32 , Dir.output , M_S.slave , "// AHB - Slave HWDATA "     ),
                        io("hrdata" , "logic" , 32 , Dir.input  , M_S.slave , "// AHB - Slave HRDATA "     ),
                        io("hwrite" , "logic" , 1  , Dir.output , M_S.slave , "// AHB - Slave HWRITE "     ),
                        io("htrans" , "logic" , 2  , Dir.output , M_S.slave , "// AHB - Slave HTRANS "     ),
                        io("hsize"  , "logic" , 3  , Dir.output , M_S.slave , "// AHB - Slave HSIZE "      ),
                        io("hburst" , "logic" , 3  , Dir.output , M_S.slave , "// AHB - Slave HBURST "     ),
                        io("hresp"  , "logic" , 2  , Dir.input  , M_S.slave , "// AHB - Slave HRESP "      ),
                        io("hready" , "logic" , 1  , Dir.input  , M_S.slave , "// AHB - Slave HREADYOUT "  ),
                        io("hsel"   , "logic" , 1  , Dir.output , M_S.slave , "// AHB - Slave HSEL"        )
                    ]
gpio_common_ports = [
                        io("gpio_i" , "logic" , "gpio_w" , Dir.input  , M_S.master , "// GPIO input"     , True  ),
                        io("gpio_o" , "logic" , "gpio_w" , Dir.output , M_S.master , "// GPIO output"    , True  ),
                        io("gpio_d" , "logic" , "gpio_w" , Dir.output , M_S.master , "// GPIO direction" , True  )
                    ]
pwm_common_ports =  [
                        io("pwm" , "logic" , 1 , Dir.output , M_S.master , "// PWM output" )
                    ]

if_0_subname   = "_gpio"
if_0_suffix    = "_0"
if_0_clk_reset = copy.deepcopy(clk_reset_ports)

if_1_subname = "_gpio"
if_1_suffix  = "_0"
if_1_ahb     = copy.deepcopy(ahb_common_ports)

if_2_subname = "_gpio"
if_2_suffix  = "_0"
if_2_gpio    = copy.deepcopy(gpio_common_ports)

j=0
for port in ahb_common_ports:
    if_1_ahb[j].name = ahb_common_ports[j].name + "_s"
    j=j+1

if_1 =  [
            interface(if_0_clk_reset , "nf_ahb" + if_0_subname , if_0_suffix , "clock and reset" ),
            interface(if_1_ahb       , "nf_ahb" + if_1_subname , if_1_suffix , "AHB slave side"  ),
            interface(if_2_gpio      , "nf_ahb" + if_2_subname , if_2_suffix , "GPIO side"       ),
        ]

        
param = ["gpio_w = `NF_GPIO_WIDTH"]

nf_ahb_gpio_0 = module(if_1,param)

slave_module_subname_1 = "_gpio"
slave_suffix_1 = "_0"
slave_module_subname_2 = "_gpio"
slave_suffix_2 = "_1"
slave_module_subname_3 = "_pwm"
slave_suffix_3 = ""
master_subname  = "_m"
master_suffix  = ""

slave_1_ports = copy.deepcopy(ahb_common_ports)
slave_2_ports = copy.deepcopy(ahb_common_ports)
slave_3_ports = copy.deepcopy(ahb_common_ports)
master_ports  = copy.deepcopy(ahb_common_ports)

j=0
for ahb_port in ahb_common_ports:
    slave_1_ports[j].name = ahb_common_ports[j].name + "_s"
    slave_2_ports[j].name = ahb_common_ports[j].name + "_s"
    slave_3_ports[j].name = ahb_common_ports[j].name + "_s"
    master_ports[j].name = ahb_common_ports[j].name 
    master_ports[j].master = M_S.master
    j=j+1


AHB_slave_1 = interface(slave_1_ports, "nf_ahb"+slave_module_subname_1,slave_suffix_1)
AHB_slave_2 = interface(slave_2_ports, "nf_ahb"+slave_module_subname_2,slave_suffix_2)
AHB_slave_3 = interface(slave_2_ports, "nf_ahb"+slave_module_subname_3,slave_suffix_3)
AHB_Master  = interface(master_ports, "nf_ahb"+master_subname,master_suffix)

AHB_Master.print_dec()
AHB_slave_1.print_dec()
AHB_slave_2.print_dec()
AHB_slave_3.print_dec()

connect([AHB_slave_1,AHB_slave_2,AHB_slave_3],AHB_Master)

nf_ahb_gpio_0.print()
nf_ahb_gpio_0.connect()
nf_ahb_gpio_0.module_dec()
