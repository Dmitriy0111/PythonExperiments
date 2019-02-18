__PARAM__
gpio_w = `NF_GPIO_WIDTH
__PORTS__
clk_reset.if , h ,    , , h          , slave  ,clock and reset
ahb.if       ,   , _s , , GPIO-slave , slave  ,AHB GPIO slave side
gpio.if      ,   ,    , ,            , master ,GPIO side