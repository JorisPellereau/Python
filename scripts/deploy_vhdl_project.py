# This script deploys repository architecture for a new VHDL project

import os
import sys
import subprocess


# ARGS
project_dir_path = sys.argv[1]
project_name     = sys.argv[2]


import deploy_vhdl_project_class

deploy = deploy_vhdl_project_class.deploy_vhdl_project_class(project_name) # Init the class


# Check if directory already exists
if(os.path.exists(project_dir_path) == False):

    print("Info: Directory %s does not exists, creating it ..." %(project_dir_path))
    subprocess.call(["mkdir", project_dir_path]) # Create Main Directory
    subprocess.call(["mkdir", project_dir_path + "/scripts"]) # Create Scripts Directory
    f = open(project_dir_path + "/scripts/Makefile", "w")
    f.write(deploy.makefile_template)
    f.close()

    print("Info: Creation done !")

# Else do nothinf and print an error
else:
    print("Error: %s already exists !" %(project_dir_path))
    print("Info: Abort creation !")
