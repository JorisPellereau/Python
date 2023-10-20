import re
import os
import sys
import subprocess

# Dissasemble File to list
def dissasemble_lins_list_to_mem_list(lines):

    # Loop on lines and get lines and data
    # Pattern for a 32 bits memory format - \w
    pattern = '[0-9a-zA-Z]*:\t[0-9a-zA-Z]{2,} [0-9a-zA-Z]{2,} [0-9a-zA-Z]{2,} [0-9a-zA-Z]{2,}'
    result = None
    str_list = []
    for i,line_str in enumerate(lines):
        result = re.search(pattern, line_str)
        if(result != None):
            str_list.append(result.group(0))


    # Remove :\t between addr and data
    str_split_list = []
    for i, line_str in enumerate(str_list):
        str_split_list.append(line_str.split(":\t"))

    # Remove space between data
    for i, line_str in enumerate(str_split_list):
        str_split_list[i][1] = str_split_list[i][1][:2] + str_split_list[i][1][3:5] + str_split_list[i][1][6:8] + str_split_list[i][1][9:11]

    return str_split_list


# Convert Addr (0, 4, 8, C) into (0, 1, 2, 3) etc
def mem_list_to_phy_mem_list(mem_list):
    phy_mem_list = []

    for i, data in enumerate(mem_list):
        phy_mem_list.append([(int(data[0], 16) >> 2), data[1]])
    return phy_mem_list
# 


# Main Scripts

# test             = sys.argv[1] # Get the test name
# zip_as_path      = sys.argv[2]
# zip_objdump_path = sys.argv[3] 
# scn_path         = sys.argv[4]
# as_file_path     = sys.argv[5]

def main_asm_to_memory(test, zip_tools_path, scn_path, o_file_path):
    zip_as      = zip_tools_path + "/zip-as"
    zip_objdump = zip_tools_path + "/zip-objdump"
    o_file           = o_file_path + "/" + test + ".o"
    dissasemble_file = o_file_path + "/" + test + "_dissasemble.txt"

    # Run ASM Scripts
    subprocess.call([zip_as, scn_path + "/" + test + ".s", "-o", o_file]) # Compile the asm scripts

    # Run OBJDump Script and get outputs into a str
    diss_str = subprocess.check_output([zip_objdump, "-S", "-D", "-g", o_file], text=True) # Dissable the script and genarate the temporary file
    lines_list = diss_str.split("\n")

    mem_data_list = dissasemble_lins_list_to_mem_list(lines_list) # Get the Addr and its data
   
    phy_mem_list = mem_list_to_phy_mem_list(mem_data_list)
    return phy_mem_list


