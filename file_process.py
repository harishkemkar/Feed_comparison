
import pandas as pd

def first_function():
    print("I am first function from file_process")


def Read_file(file_path): ## this fucntion should take file path as input and return dataframe as output
    print("Function for reading file")
    df = pd.read_excel(file_path, engine='openpyxl')
    print("File read done and loaded in dataframe")
    return df;

def string_func( str1 ):
    print(str1)
    return

def comp_2_df(df1 ,df2 ):
    column_name1 = list(df1.columns)

    column_name2 = list(df2.columns)
    print("Below are the column names for both dataframes")
    print(column_name1)
    print(column_name2)

    if (column_name1 == column_name2):
        print("     ")
        print("Column name and sequence of column are exact match")
    else:
        print("     ")
        print("column name or sequence of column do not match ")

    print("     ")
    print("No of rows in sheet 1  ")
    print(df1.shape[0])

    print("     ")
    print("No of rows in sheet 2  ")
    print(df2.shape[0])

    return


