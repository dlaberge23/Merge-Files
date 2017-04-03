import os
import glob
from tkFileDialog import askdirectory


def merge_files(file_folder, param):

    saved_path = os.getcwd()
    print ("Your current directory: "+ saved_path)

    print ("Moving to: "+ file_folder)
    os.chdir(file_folder)

    file_list = glob.glob('*'+param)
    print file_list
    header_saved = False
    with open('merged_files.csv','wb') as fout:
        for filename in file_list:
            with open(filename) as fin:
                header = next(fin)
                if not header_saved:
                    fout.write(header)
                    header_saved = True
                for line in fin:
                    fout.write(line)

def define_parameter():
    """Choose the parameter to limit the file merge with"""
    parameter = raw_input("Merge parameters? (include '.')> ")
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
