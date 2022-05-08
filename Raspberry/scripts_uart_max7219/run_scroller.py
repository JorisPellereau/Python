# 

import sys
from uart_max7219_ctrl_class import *

# INIT UART
uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)


# INIT SCROLLER RAM
uart_rpi.init_scroll_ram()





# Close UART
uart_rpi.close_uart()
