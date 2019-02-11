from jinja2 import Template

template = Template('''/*
*  File            :   {{MODULE_NAME}}.sv
*  Autor           :   {{AUTOR}}
*  Data            :   {{DATA}}
*  Language        :   SystemVerilog
*  Description     :   {{COMMENT}}
*  Copyright(c)    :   {{COP_DATA}} {{AUTOR}}
*/

`include "../../inc/nf_settings.svh"
`include "../../inc/nf_ahb.svh"

module {{MODULE_NAME}}
#(
    parameter                                   slave_c = `SLAVE_COUNT
)(
    input   logic   [slave_c-1 : 0]             hsel_ff,    // hsel after flip-flop
    // slave side
    input   logic   [slave_c-1 : 0][31 : 0]     hrdata_s,   // AHB read data slaves 
    input   logic   [slave_c-1 : 0][1  : 0]     hresp_s,    // AHB response slaves
    input   logic   [slave_c-1 : 0][0  : 0]     hready_s,   // AHB ready slaves
    // master side
    output  logic                  [31 : 0]     hrdata,     // AHB read data master 
    output  logic                  [1  : 0]     hresp,      // AHB response master
    output  logic                  [0  : 0]     hready      // AHB ready master
);

    always_comb
    begin
        hrdata  = '0; 
        hresp   = `AHB_HRESP_ERROR; 
        hready  = '1;
        casex( hsel_ff )
{%- for slaves in SLAVE_N %}
            {{SLAVE_C}}'b{{'?'*(SLAVE_C-slaves-1)}}{{10**slaves}}  : begin hrdata = hrdata_s[{{slaves}}] ; hresp = hresp_s[{{slaves}}] ; hready = hready_s[{{slaves}}] ;   end
{%- endfor %}
            default : ;
        endcase
    end

endmodule : {{MODULE_NAME}}

''')

module_name = "nf_ahb_mux"
slave_number = 3

result = template.render(
    MODULE_NAME = "nf_ahb_mux",
    AUTOR = "Vlasov D.V.",
    DATA = "2018.01.28",
    COMMENT = "This is AHB multiplexer module",
    COP_DATA = "2018 - 2019",
    SLAVE_C = slave_number,
    SLAVE_N = range(slave_number)
)

out_file = open(module_name+".sv",'w')

out_file.write(result)
