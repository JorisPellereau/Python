# 

import sys
from uart_max7219_ctrl_class import *

# sys.argv[1] : Pattern selection
# sys.argv[2] : start_ptr
# sys.argv[3] : msg_length
# sys.argv[4] : scroller_tempo


# INIT UART
uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)


# INIT SCROLLER RAM
uart_rpi.init_scroll_ram()


start_ptr = int(sys.argv[2])
msg_length = int(sys.argv[3])
DATA_TEMPO = int(sys.argv[4], 16)

# == Pattern selection ==
current_pattern = uart_rpi.pattern_list[int(sys.argv[1])]*4



#pattern_scroller_data = uart_rpi.matrix_2_data_list(matrix_array)

#print(pattern_scroller_data)
#print("len(pattern_scroller_data) : %d" %(len(pattern_scroller_data)) )

# == LOAD Pattern ==
uart_rpi.load_pattern_scroller(start_ptr, 255, current_pattern)

# == LOAD SCROLLER Tempo ==
#print("DATA_TEMPO : %d - 0x%x" %(DATA_TEMPO, DATA_TEMPO) )
#uart_rpi.run_load_scroller_tempo(DATA_TEMPO)

# == RUN Pattern Scroller ==
uart_rpi.run_pattern_scroller(start_ptr, msg_length)

# Close UART
uart_rpi.close_uart()
