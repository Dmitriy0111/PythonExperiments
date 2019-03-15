__PARAM__
pwm_width ,8
__PORTS__
clk_reset.if , h    ,    , , h         , slave  ,clock and reset
ahb.if       ,      , _s , , PWM-slave , slave  ,AHB PWM slave side
clk_reset.if , pwm_ ,    , , PWM_      , slave  ,PWM side
pwm.if       ,      ,    , ,           , master ,