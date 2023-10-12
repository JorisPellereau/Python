import re
import os
import sys

file_in = sys.argv[1]

# Open file and get lines into a list
with open(file_in, 'r') as file_read:
    lines = file_read.readlines()
    

# Loop on lines and get lines and data
# Pattern for a 32 bits memory format
pattern = '^[0-9a-zA-Z]*:\t[0-9a-zA-Z]{2,} [0-9a-zA-Z]{2,} [0-9a-zA-Z]{2,} [0-9a-zA-Z]{2,}'
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

print(str_split_list)
