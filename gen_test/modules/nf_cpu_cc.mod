__PARAM__
__PORTS__
clk_reset.if     , ,     ,             , slave  ,clock and reset
simple_memory.if , , _i  , instruction , slave  ,instruction memory (IF)
simple_memory.if , , _dm , data        , slave  ,data memory and other's
simple_memory.if , , _cc , cc_data     , master ,cross connect data