__PARAM__
gpio_w = `NF_GPIO_WIDTH
R_S = `R_S
B_S = `B_S
D_S = `D_S
__PORTS__
clk_reset.if ,       , _f   ,         ,        , slave  ,clock and reset
clk_reset.if ,       , _m   ,         ,        , slave  ,clock and reset
ahb.if       , gpio_ , _i_0 ,         , slave  , slave  ,AHB slave side 0
ahb.if       , pwm_  , _i_1 ,         , slave  , slave  ,AHB slave side 1
ahb.if       , ram_  , _i_2 ,         , slave  , slave  ,AHB slave side 2
ahb.if       , none_ , _i_3 ,         , slave  , slave  ,AHB slave side 3
ahb.if       , none_ , _i_4 ,         , slave  , slave  ,AHB slave side 4
ahb.if       , none_ , _i_5 ,         , slave  , slave  ,AHB slave side 5
ahb.if       , none_ , _i_6 ,         , slave  , slave  ,AHB slave side 6
ahb.if       , none_ , _i_7 , 2       , slave  , slave  ,AHB slave side 7
ahb.if       , arr_  , _s   , slave_c , slave  , slave  ,AHB slave side
gpio.if      ,       , _a   ,         ,        , master ,GPIO side
gpio.if      ,       , _b   ,         ,        , master ,GPIO side
gpio.if      ,       , _c   ,         ,        , master ,GPIO side
sdram.if     ,       , _s   ,         ,        , master ,SDRAM side