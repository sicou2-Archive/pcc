#Author: BCL
#Date: 22Mar2020
#Title: Stripping Names
#About: This removes the white space from a string variable. 

#stripping names

target_name = "  \n\n\t\tbrata uron  \n\n\n"

print(f"{target_name.rstrip()}")
print(f'{target_name.lstrip()}')
print(f'{target_name.strip()}')