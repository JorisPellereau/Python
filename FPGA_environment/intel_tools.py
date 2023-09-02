

import argparse
import intel_tools_class

parser = argparse.ArgumentParser(description='Creates TCL Quartus from Intel files')

intel_tools_class = intel_tools_class.intel_tools_class()

# Create Project File Argument
parser.add_argument('--create_project_file',
                    action='store',
                    nargs=4,
                    type=str, 
                    help='Create the TCL project file'
)

parser.add_argument('--create_setup_file',
                    action='store',
                    nargs=3,
                    type=str, 
                    help='Create the TCL setup file'
)

args = parser.parse_args()

#print(args.create_project_file)
#print(type(args.create_project_file))

print("args : %s" %(args))

if(args.create_project_file):
    intel_tools_class.create_project_file(family       = args.create_project_file[0],
                                          revision     = args.create_project_file[1],
                                          project_name = args.create_project_file[2],
                                          file_name    = args.create_project_file[3])

elif(args.create_setup_file):
    intel_tools_class.create_setup_file(project_name = args.create_setup_file[0],
                                        csv_file     = str(args.create_setup_file[1]),
                                        file_name    = args.create_setup_file[2])
