# Run a static pattern

import sys
from uart_max7219_ctrl_class import *

# sys.argv[1] : Pattern selection
# sys.argv[2] : start_ptr
# sys.argv[3] : stop_ptr

# Init UART
uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)


# Init STATIC RAM
uart_rpi.init_static_ram()


# == Pattern selection ==
current_pattern = uart_rpi.pattern_list[int(sys.argv[1])]
#pattern_data = uart_rpi.macros_uart_display_ctrl_class.pattern_to_uart_static_data_list(current_pattern)
pattern_data = uart_rpi.max7219_utils.sort_mem_list(data_list = current_pattern)

# == LOAD Pattern ==
uart_rpi.load_pattern_static(start_ptr = int(sys.argv[2]),
                             static_pattern_data = pattern_data)


# == RUN Pattern static ==
uart_rpi.run_pattern_static(start_ptr = int(sys.argv[2]),
                            last_ptr  = int(sys.argv[3]))
uart_rpi.close_uart()
