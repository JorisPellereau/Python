
import os
import sys
import csv
import re


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



    def create_init_rom_str_var(self, o_file_path, data_list, mem_data_width, mem_depth, mk_file_name, mk_file_path, default_data = 0x00000000):
        """
        This function allows to create a file with will contains a Makefile variable used in order to initialized a generic parameter of an entity (Array)
        """
        data_array = []
        data_format = "{0:0" + str(mem_data_width) + "b}"

        # Initialized the array
        for i in range(0, mem_depth):
            data_array.append(data_format.format(default_data))
        

        # Update the usefull data
        # Get the addr of the data and set it
        # i[0] == Addr
        # i[1] == data
        for i in data_list:
            data_array[i[0]] = data_format.format(int(i[1], 16))


        # Add double quote for each data
        for i in range(0, len(data_array)):
            #data_array[i] =  "\\" + "\"" + data_array[i] + "\\" + "\""
            data_array[i] =  "B\\\"{0}\\\"".format(data_array[i])

        # Add "," between each data
        data_array = ",".join(data_array)

        # Add A prefix and parenthesis
        #       data_array =  "\"" + "{" + data_array + "}" + "\""
        #        data_array = "\"set_parameter -entity zipcpu_axi4_lite_core -name G_ROM_INIT A(\\\"B\\\"1111111111111111\\\"\\\")\""
        data_array = "\"set_parameter -entity zipcpu_axi4_lite_core -name G_ROM_INIT A({0})\"".format(data_array) # PREK OK !!
#       data_array = "\"set_parameter -entity i_zipcpu_axi4_lite_core_0 -name G_ROM_INIT 8\""

        #"\\\"A(" + data_array + ")" + "\\\""

        with open (mk_file_path + "/" + mk_file_name + ".mk", 'w') as writer:
            writer.write("{0} = {1}".format("INIT_ROM_" + mk_file_name.upper(), data_array))
        


    def warn_error_to_csv(self, file_in, csv_file_out):
        """
        Search for Warning or Error and write in into a csv file
        """
        
        idx_cnt = 0
        csv_info_list = [] # CSV Info list to add in the CSV file
        
        # Open files and get lines into list
        with open (file_in, 'r') as reader:
            lines_list = reader.readlines()

        # Regex Pattern
        pattern = '^Warn|^Critical|^[ ]*Warn'

        # Read Each Line
        for i, line_str in enumerate(lines_list):
            result = re.search(pattern, line_str)

            # If the result is different from None -> Get infos
            if(result != None):
                csv_info_list.append([idx_cnt, i, line_str[:-1]]) # Write the index number, the line of the error/warn and the line without the \n
                idx_cnt += 1 # Inc the counter



        # Write csv file
        with open (csv_file_out, 'w', newline = '') as f:
            #writer = csv.writer(f)

            fieldnames = ['Index', 'Lines', 'Warning or Error', 'Comments'] # Set the Header
            writer     = csv.writer(f)
            writer.writerow(fieldnames) # Write the header

            # For each index of the csv info list
            for i in csv_info_list:
                writer.writerow(i)


        print("warn_error_to_csv done. Output file : %s" %(csv_file_out))
        print("Error/Warning number : %d" %(idx_cnt))


    def extract_info_from_rpt_table(self, table_txt):
        """
        Extract information from table in report
        """

        # Extraire les en-têtes et les lignes du tableau
        # Skip the index 0
        headers_line = table_text.split('\n')[1]
        collumns     = table_text.split('\n')[3]
        data_lines   = table_text.split('\n')[5:-2]

        # Extraire les en-têtes
        headers = [header.strip() for header in headers_line.split(';') if header.strip()]

        # Get Collumns info
        column_info = [col.strip() for col in collumns.split(';') if col.strip()]

        # Extraire les lignes de données
        data_list = []
        for i in data_lines:
            data_list.append([tmp.strip() for tmp in i.split(';') if tmp.strip()])

        # Créer un DataFrame pandas avec les données extraites
        df = pd.DataFrame(data_list, columns=column_info)

        return df


    def extract_rpt_toc(self, rpt_lines):
        """
        Extract RPT Table of Content
        """

        toc_list    = [] # List of TOC
        toc_pattern = re.compile(r'^\s+[0-9]*[.]') # TOC Pattern

        for i in rpt_lines:
            match = pattern.search(line)
            if match:
                toc_list.append(i) # Add to the list the content of the line
            else:
                None


        nb_char_to_remove = len(str(len(toc_list)))
        # Remove useless content number
        for i, value in enumerate(toc_list):
            toc_list[i] = toc_list[1][nb_char_to_remov:]
        
