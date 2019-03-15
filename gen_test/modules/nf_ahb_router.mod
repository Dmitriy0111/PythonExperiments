__PARAM__
slave_c ,`SLAVE_COUNT
__PORTS__
clk_reset.if , h ,    ,         , h          , slave  ,clock and reset
ahb.if       ,   ,    ,         , Master     , slave  ,Master side
ahb.if       ,   , _s , slave_c , Slave      , master ,Slaves side