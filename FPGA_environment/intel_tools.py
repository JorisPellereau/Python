

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
                    nargs='*',
                    type=str, 
                    help='Create the TCL setup file'
)

args = parser.parse_args()

#print(args.create_project_file)
#print(type(args.create_project_file))


print("INTEL TOOLS Args : ")
print("args : %s" %(args))

# Create the PROJECT FILE
if(args.create_project_file):
    intel_tools_class.create_project_file(family       = args.create_project_file[0],
                                          revision     = args.create_project_file[1],
                                          project_name = args.create_project_file[2],
                                          file_name    = args.create_project_file[3])


# Create the SETUP FILE
elif(args.create_setup_file):

    # Custom Command is optionnal
    # Perform the selection
    if(len(args.create_setup_file)>=5):
        custom_cmd = args.create_setup_file[4]
        print("type(custom_cmd) : %s" %(type(custom_cmd)))
    else:
        custom_cmd = []
        
    intel_tools_class.create_setup_file(project_name = args.create_setup_file[0],
                                        csv_file     = str(args.create_setup_file[1]),
                                        file_name    = args.create_setup_file[2],
                                        sdc_file     = str(args.create_setup_file[3]),
                                        custom_cmd   = custom_cmd
                                        )
