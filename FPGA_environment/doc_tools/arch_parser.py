# Architecture PArser
# Test

import os
import sys

#import gi
#gi.require_version('Pango', '1.0')
#gi.require_version('PangoCairo', '1.0')
#gi.require_version('Gtk', '3.0')
#gi.require_version('Wnck', '3.0')
#gi.require_version('Gst', '1.0')
#gi.require_version('AppIndicator3', '0.1')
#from gi.repository import Pango as pango#Gtk, GObject, Gdk, Wnck, GdkX11, Gst, AppIndicator3


# Path of HDL parse
hdl_parse_path = '/home/linux-jp/Documents/GitHub/hdlparse/hdlparse'
sys.path.append(hdl_parse_path)

import vhdl_parser as vhdl
#import hdlparse.verilog_parser as vlog

#from hdlparse.vhdl_parser import VhdlComponent

symbolator_path = '/home/linux-jp/Documents/GitHub/symbolator'
sys.path.append(symbolator_path)
import symbolator

vhdl_ex = vhdl.VhdlExtractor()
#vlog_ex = vlog.VerilogExtractor()


#print(dir(vhdl_ex))


# File Search
file_list = symbolator.file_search("/home/linux-jp/Documents/GitHub/VHDL_code")#/PR_115/sources/lib_zipcpu_axi4_lite_top")
print("\n\n## Files list : %s ##\n\n" %(file_list))

files_obj_dict = dict() # Dict Initialization
obj_dict = dict()
parse_vhdl_file_dict = dict()
# Loop on each files and search for object
for i in file_list:
    print(i)

    
    
    head, tail = os.path.split(i) # Extract the filename only
    
    obj_dict[tail] = vhdl_ex.extract_objects(fname = i,
                                             type_filter=None)

    parse_vhdl_file_dict[tail] = vhdl.parse_vhdl_file(fname = i) # Parse VHDL Files - no extract
    
    # Get lines from a file
    # /home/linux-jp/Documents/GitHub/VHDL_code/PR_115/sources/lib_zipcpu_axi4_lite_top/zipcpu_axi4_lite_core.vhd
    with open(i, "r") as file:
        lines = file.readlines()
        #print(type(lines))

    tmp_list = [] # Temporary List
    for j in lines:
        if(vhdl_ex.extract_objects_from_source(j) != []):
            tmp_list.append(vhdl_ex.extract_objects_from_source(j))

    # Append the list to the main dict
    
    files_obj_dict[tail] = tmp_list
        
print("Results : ")
#for i in tot:
#    print(i)

#for i in files_obj_dict.keys():
#    print("%s : %s" %(i, files_obj_dict[i]))

#print(files_obj_dict["/home/linux-jp/Documents/GitHub/VHDL_code/PR_115/sources/lib_zipcpu_axi4_lite_top/zipcpu_axi4_lite_core.vhd"])

#for i in files_obj_dict["/home/linux-jp/Documents/GitHub/VHDL_code/PR_115/sources/lib_zipcpu_axi4_lite_top/zipcpu_axi4_lite_core.vhd"]:
#    print("%s %s %s" %(i[0].kind, i[0].name, i[0].entity))

#vhdl_ex.extract_objects(fname = "/home/linux-jp/Documents/GitHub/VHDL_code/PR_115/sources/lib_zipcpu_axi4_lite_top/zipcpu_axi4_lite_core.vhd",
#                        type_filter = 'VhdlComponent')

#for i in obj_dict.keys():
#    print("%s : %s" %(i, obj_dict[i]))


# Use parse VHDL
for i in parse_vhdl_file_dict.keys():
    print("%s : %s" %(i, parse_vhdl_file_dict[i]))
