# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#########My code starts here######################################################

import pandas as pd
import numpy as np
import os
import file_process

############## Below lines load given files into dataframes

temp_df1 = file_process.Read_file("D:\Harish kemkar\projcomp\File1.xlsx")
#print(temp_df1.head(5))

temp_df2 = file_process.Read_file("D:\Harish kemkar\projcomp\File2.xlsx")
#print(temp_df2.head(5))

temp_df3 = file_process.Read_file("D:\Harish kemkar\projcomp\File3.xlsx")
#print(temp_df3.head(5))

####################################################################################

file_process.comp_2_df(temp_df1,temp_df2)

