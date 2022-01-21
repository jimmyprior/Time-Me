"""
Swaps the comments in the code to the timeme code in a temporary file. 
Runs the code in the temp file
"""


import os 
import tempfile
import subprocess
import shutil 
import shlex
import argparse

from timeme.globals import PACKAGE_NAME, INVOKE_NAME, COMMANDS, STATIC


def copy_folder(og_parent_directory, temp_directory):
    """
    copys the contents of the target folder to a temportary folder. 
    returns the path of the new temp folder containing all of the contents 
    """
    folder_path = os.path.join(temp_directory, PACKAGE_NAME)
    shutil.copytree(og_parent_directory, folder_path)
    return os.path.join(temp_directory, PACKAGE_NAME)
    
    
def get_line_spacing(og_line, new_line):
    """
    Takes old lines and modifies the new lines to have consistent indentation
    """
    prefix = og_line[:og_line.index("#")]
    return prefix + new_line
    
    
def modify_file(file_path):
    """
    will modify the file if timeme args are in there
    
    import time at the top of the file if not already theres
    #use args to parse the strings
    
    create varaibles with random name whenever new timeme args and create new TimeBlock class
    add start and stop whenever start and stop strings
    """
    #store names and the corrispondings variable names    
    with open(file_path, "r") as infile:
        original = infile.readlines()
        stripped = [line.strip() for line in original]
        changed = False
        
        for index, line in enumerate(stripped):
            
            if "#" + INVOKE_NAME.lower() not in line.lower():
                continue 
            
            parsed = shlex.split(line[1:])
            
            if COMMANDS.get(parsed[1]):
                #these commands need to be formatted to include the name 
                command = COMMANDS.get(parsed[1]).format(parsed[3]) #parsed 3 is timeme name
            
            elif STATIC.get(parsed[1]):
                command = STATIC.get(parsed[1])
            
            else:
                #command not recognized
                #raise exception
                continue 
                        
            changed = True
            original[index] = get_line_spacing(original[index], command)
            
        #if the file was changed import the stuff
        if changed:
            original.insert(0, STATIC["import"])
    
    
    with open(file_path, "w") as infile:
        infile.writelines(original)
    
    
def change_files_in_directory(directory):
    """
    Resursive fucntion that will fun on all of the folders in the tree and parse them accordingly 
    """
    for content in os.listdir(directory):
        content_path = os.path.join(directory, content)
        if os.path.isdir(content_path):
            change_files_in_directory(content_path)
        elif ".py" in content and ".pyc" not in content: #only python files
            #checking to see if i need to add time me to this file
            modify_file(content_path)
    
    
    
def main():
    """
    command line tool access. 
    provide the file using args 
    
    creates a tempory folder with a copy of the package and converts the time comments to code and runs 
    """
    parser = argparse.ArgumentParser(prog="timeme", description="Run program with timed comments")
    parser.add_argument("--file", dest="filepath")
    
    args = parser.parse_args()
    split_path = args.filepath.split("\\")
    entry_name = split_path.pop(-1)
    parent_path = "\\".join(split_path[:])

    with tempfile.TemporaryDirectory() as tmp:
        entry_dir = copy_folder(parent_path, tmp)
        #resp = subprocess.call(f"python {os.path.join(entry_dir, entry_name)}")
        change_files_in_directory(entry_dir)

        subprocess.check_call(f"python {os.path.join(entry_dir, entry_name)}")
          

