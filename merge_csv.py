import os
import glob
from tkFileDialog import askdirectory


def merge_files(file_folder, param):
    #to return after merging files
    saved_path = os.getcwd()
    print ("Your current directory: "+ saved_path)
    #move to folder to be merged
    print ("Moving to: "+ file_folder)
    os.chdir(file_folder)
    #read files with the parameter
    file_list = glob.glob('*'+param+'*')
    #add a confirmation to merge? print list for now
    print file_list

    #variable needed to save header once, for files with same headers
    header_saved = False
    with open('merged_files.'+param,'wb') as file_out:
        for filename in file_list:
            with open(filename) as file_in:
                header = next(file_in)
                if not header_saved:
                    file_out.write(header)
                    header_saved = True
                for line in file_in:
                    file_out.write(line)

    #Add option to run again?

def define_parameter():
    """Choose the extension to limit the file merge with"""
    parameter = raw_input("Merge parameters? (don't include '.')> ")
    return parameter

def choose_folder():
    """GUI folder chooser"""
    print ("Choose a folder with files to merge")
    folder_name = askdirectory()
    return folder_name

parameter = define_parameter()
print (parameter)

folder = choose_folder()
print (folder)

merge_files(folder, parameter)
