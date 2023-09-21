
import os
import sys
import csv


class intel_tools_class:
    """
    This class contains methods used for the utilization of Quartus software from Intel
    """
    #    def __init__(self):

    def create_project(self, family, revision, project_name):
        """
        """
        outputs_lines = []
        outputs_lines.append("project_new -family {0} -revision {1} {2}".format(family, revision, project_name))
        outputs_lines.append("export_assignments")
        outputs_lines.append("project_close")
        return outputs_lines

    def set_project_config(self, family, device, top_level_entity):
        """
        This methods add project configuration TCL command to a list of string.
        """

        outputs_lines = []

        outputs_lines.append("\n# Set Project Configuration")
        
        outputs_lines.append("set_global_assignment -name FAMILY {0}".format(family))
        outputs_lines.append("set_global_assignment -name DEVICE {0}".format(device))
        outputs_lines.append("set_global_assignment -name TOP_LEVEL_ENTITY {0}".format(top_level_entity))
        return outputs_lines
    

    # Possible Standard parameter :
    # 2.5 V
    # 3.3-V LVTTL
    # 3.3-V LVCMOS
    def pinout_extract_config(self, csv_file):
        """
        This function extract information from an input csv file.
        It returns a list of string which contain pinout parameters.

        :param csv_file: The CSV file to read
        :type csv_file: string

        :return: The list of command
        :rtype: list[str]
        """
        
        set_pin_location_list = [] # List of the Set pin location
        set_io_standard_list  = [] # List of Set IO Standard
        set_pull_up_list      = [] # List of Set PULL UP
        set_drive_list        = [] # List of DRIVE/STRENGTH
        set_slew_rate_list    = [] # List of SLEW RATE

        outputs_lines = [] # Output Lines
        with open(csv_file, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ';')

            #print("csvreader : ")
            #print(dir(csvreader))
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
                    slew_rate  = info[7]
                    terminason = info[8]

                    # Set Pin Location
                    set_pin_location_list.append("set_location_assignment PIN_{0} -to {1}".format(location, port_name))

                    # Set IO Standard
                    set_io_standard_list.append("set_instance_assignment -name IO_STANDARD \"{0}\" -to {1}".format(standard, port_name))

                    # Add a pull up only if /= NA
                    if(pull_up != "NA"):
                        set_pull_up_list.append("set_instance_assignment -name WEAK_PULL_UP_RESISTOR {0} -to {1}".format(pull_up, port_name))
                    # Add output DRIVE STRENGTH only for outputs    
                    if( (direction.lower() == "out" or direction.lower() == "inout") and drive != "NA"):
                        set_drive_list.append("set_instance_assignment -name CURRENT_STRENGTH_NEW {0} -to {1}".format(drive, port_name))

                    # Add SLEW Rate. Only for outputs
                    if(direction.lower() == "out" or direction.lower() == "inout"):
                        set_slew_rate_list.append("set_instance_assignment -name SLEW_RATE {0} -to {1}".format(slew_rate, port_name))

        outputs_lines.append("# Set Pin Location")
        outputs_lines = outputs_lines + set_pin_location_list
        outputs_lines.append("\n# Set IO STANDARD")
        outputs_lines += set_io_standard_list
        outputs_lines.append("\n# Set PULL UP")
        outputs_lines += set_pull_up_list
        outputs_lines.append("\n# Set DRIVE")
        outputs_lines += set_drive_list
        outputs_lines.append("\n# Set SLEW RATE")
        outputs_lines += set_slew_rate_list
        

        return outputs_lines


    def set_global_param(self,
                         CRC_ERROR_CHECKING            = 'OFF',
                         crc_error_open_drain          = 'off',
                         ERROR_CHECK_FREQUENCY_DIVISOR = 16
    ):
        """
        It returns a list of string containing global configuration
        """

        outputs_lines = []

        outputs_lines.append("\n# Set Global Configuration")
        outputs_lines.append("set_global_assignment -name CRC_ERROR_CHECKING {0}".format(CRC_ERROR_CHECKING))
        outputs_lines.append("set_global_assignment -name crc_error_open_drain {0}".format(crc_error_open_drain))
        outputs_lines.append("set_global_assignment -name ERROR_CHECK_FREQUENCY_DIVISOR {0}".format(ERROR_CHECK_FREQUENCY_DIVISOR))
        return outputs_lines

    def set_sdc_file(self, sdc_file):
        """
        It returns a string that contains the line that specify the .sdc file to use in the .qsf files
        """
        outputs_lines = []

        outputs_lines.append("\n# Set SDC FILE")
        outputs_lines.append("set_global_assignment -name SDC_FILE {0}".format(sdc_file))
        return outputs_lines
        

    def create_project_file(self, family, revision, project_name, file_name):
        """
        """

        outputs_lines = self.create_project(family, revision, project_name)
        with open (file_name, 'w') as writer:
            writer.writelines('\n'.join(outputs_lines))

        print("create_project_file done.")


    def create_fit_warn_error_report(self):
        """
        Create a csv file that contains warning and error from FIT
        """
        None

    def set_custom_cmd(self, custom_cmd):
        outputs_lines = []
        outputs_lines.append("\n# CUSTOM Commands")

        # Add a single commands
        if(type(custom_cmd) == str):
            outputs_lines.append(custom_cmd)
            
        elif(type(custom_cmd) == list):
            for i in custom_cmd:
                outputs_lines.append(i)

        return outputs_lines

    def create_setup_file(self, project_name, csv_file, file_name, sdc_file, custom_cmd):
        """
        """

        outputs_lines = []
        outputs_lines.append("project_new {0} -overwrite".format(project_name)) # Overwrite the project

        # Get Pinouts Commands
        pinout_lines = self.pinout_extract_config(csv_file)
        outputs_lines += pinout_lines

        # Get SDC File Command
        outputs_lines += self.set_sdc_file(sdc_file)

        # Get GLOBAL Commands
        # TBD

        # Custom Command 
        outputs_lines += self.set_custom_cmd(custom_cmd)

        # Export and Close
        outputs_lines.append("\n")
        outputs_lines.append("export_assignments")
        outputs_lines.append("project_close")
        
        with open (file_name, 'w') as writer:
            writer.writelines('\n'.join(outputs_lines))

        print("create_setup_file done.")
