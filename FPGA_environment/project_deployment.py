# This script allows to deploy a new FPGA/RTL project
# The folder organization is the same

import os
import sys
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Deploy a new FPGA project. It creates the folder repository for a new project.')

# Project Name Argument
parser.add_argument('project_name',
                    action='store',
                    nargs=1,
                    type=str, 
                    help='The project Name to create (Top folder name)'
)


parser.add_argument('project_path', 
                    action='store',
                    nargs=1,
                    type=str, 
                    help='The project PATH to create the project'
)

parser.add_argument('--template',
                    nargs=1,
                    action='store',
                    help='Use the Makefile template'
)

args = parser.parse_args()
print(args.project_name, args.project_path, args.template)


# Create the project full path
project = args.project_path[0] + "/" + args.project_name[0]

# Check if directory already exists
if(os.path.exists(project) == False):
      
    print("Info: Directory %s does not exists, creating it ..." %(project))
    subprocess.call(["mkdir", project])                         # Create Main Directory
    subprocess.call(["mkdir", project + "/scripts"])            # Create scripts Directory
    subprocess.call(["mkdir", project + "/sources"])            # Create sources Directory
    subprocess.call(["mkdir", project + "/tb_sources"])         # Create tb_sources Directory
    subprocess.call(["mkdir", project + "/scenarios"])          # Create scenarios Directory
    subprocess.call(["mkdir", project + "/do_files"])           # Create sources Do files Directory
    subprocess.call(["mkdir", project + "/do_files/run_files"]) # Create Run do Files Directory
    subprocess.call(["mkdir", project + "/do_files/waves"])     # Create Waves Directory

    # Create the Makefile

    # Create the Makefile from Template
    if(args.template != None):
        f = open(args.template[0] + "/Makefile_template", "r") # Read the template
        makefile_tmp = f.readlines() # Get lines of the template into a list        
        f.close() # Close the file
        makefile_tmp = "".join([i for i in makefile_tmp]) # Transform the list[str] into a single str

        f = open(project + "/scripts/Makefile", "w") # Create the Makefile
        f.write(makefile_tmp.format(args.project_name[0]))
        f.close()
    else:
        print("No Template use - No Makefile Created")
    

    print("Info: Creation done !")

# Else do nothinf and print an error
else:
    print("Error: %s already exists !" %(project))
    print("Info: Abort creation !")

