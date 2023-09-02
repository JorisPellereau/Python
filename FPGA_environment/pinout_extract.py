import os
import csv
import sys

csv_file    = sys.argv[1]
output_file = sys.argv[2]

set_pin_location_list = [] # List of the Set pin location
set_io_standard_list  = [] # List of Set IO Standard
set_pull_up_list      = [] # List of Set PULL UP
set_drive_list        = [] # List of DRIVE/STRENGTH

global_config_list = [] # List of Global Parameters

outputs_lines = [] # Output Lines
with open(csv_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ';')

    for i, row in enumerate(csvreader):

        # Skip the first line
        if(i > 0):
            info = row[0].split(',')
            port_name  = info[0]
            direction  = info[1]
            location   = info[2]
            bank       = info[3]
            standard   = info[4]
            pull_up    = info[5]
            drive      = info[6]
            terminason = info[7]
            set_pin_location_list.append("set_location_assigment PIN_{0} -to {1}".format(location, port_name))
            set_io_standard_list.append("set_instance_assigment -name IO_STANDARD {0} -to {1}".format(standard, port_name))

            # Add a pull up only if /= NA
            if(pull_up != "NA"):
                set_pull_up_list.append("set_instance_assigment -name WEAK_PULL_UP_RESISTOR {0} -to {1}".format(pull_up, port_name))

            # Add output DRIVE STRENGTH only for outputs
            if(direction == "out" or "OUT"):
                set_drive_list.append("set_instance_assigment -name CURRENT_STRENGTH_NEW {0} to {1}".format(drive, port_name))


global_config_list.append("set_global_assignment -name CRC_ERROR_CHECKING OFF")
global_config_list.append("set_global_assignment -name crc_error_open_drain off")
global_config_list.append("set_global_assignment -name ERROR_CHECK_FREQUENCY_DIVISOR 16")


# == CREATE FILE ==

outputs_lines.append("# Set Pin Location")
outputs_lines = outputs_lines + set_pin_location_list
outputs_lines.append("\n# Set IO STANDARD")
outputs_lines += set_io_standard_list
outputs_lines.append("\n# Set PULL UP")
outputs_lines += set_pull_up_list
outputs_lines.append("\n# Set DRIVE")
outputs_lines += set_drive_list
outputs_lines.append("\n# Set Global Configuration")
outputs_lines += global_config_list

f = open(output_file, "w")
f.writelines("\n".join(outputs_lines))
f.close()
# =================
