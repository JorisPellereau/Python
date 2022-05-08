# Run a static pattern


import sys
from uart_max7219_ctrl_class import *

# Init UART
uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)


# Init STATIC RAM
uart_rpi.init_static_ram()


matrix_array = np.array(matrix)

#print(matrix_array)

static_pattern_data = uart_rpi.matrix_2_static_pattern(matrix_array)

print("static_pattern_data : %s" %(static_pattern_data) )

print("len(static_pattern_data) : %d" %(len(static_pattern_data)) )
    
uart_rpi.load_pattern_static(start_ptr, static_pattern_data)

uart_rpi.close_uart()
