#! /bin/python3
import os

directory = input("What is the path of the folder containing the .html files you would like to clean? ")

def rem_chunk(source):
    begin_table = """ cellpadding="0" """
    end = "<hr"
    end_table = "</table>"
    cap_hr = "<HR>"
    link = "<a href="
    begin_block = "<blockquote>"
    end_block = "</blockquote>"
    cpyrgt = "Babson College All Rights Reserved"
    stamp = "<!--webbot bot="

    flag = False
    with open(source, 'r+', encoding='utf8', errors='ignore') as f:
        page = f.readlines()
        f.seek(0) 
        # this returns the script to the beginning of the file as the file will be overwritten with every line except those matching image_line
        for line in page:
            if begin_table in line or begin_block in line:
                flag = True
            elif end in line or end_block in line or end_table in line:
                flag = False

            if flag == False:
                f.write(line)
            else:
                pass

        f.seek(0)
        for line in page:
            if end in line or cap_hr in line or link in line or cpyrgt in line or stamp in line or end_table in line:
                pass
            else:
               f.write(line) 
        f.truncate() # this ensures there is nothing written to the file after the for loop completes.

for root, subdirectories, files in os.walk(directory): # this for loop walks through all directories in the specified folder, and runs the ablrule function on all .html files
    for file in files:
        source = os.path.join(root, file)
        if ".html" in source:
            rem_chunk(source)
            