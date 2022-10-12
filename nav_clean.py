#! /bin/python3
import os

directory = input("What is the path of the folder containing the .html files you would like to clean? ")

def rem_chunk(source):
    begin_table = """<table border="0" """
    end = "<hr"
    end_table = "</table>"
    begin_block = "<blockquote>"
    end_block = "</blockquote>"
    
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
        f.truncate()
    return None

def rem_line(source):
    end = "<hr"
    cap_hr = "<HR>"
    link = "<a href="
    cpyrgt = "Babson College All Rights Reserved"
    stamp = "<!--webbot bot="
    # end_table = "</table>"
    end_block = "</blockquote>"
    with open(source, 'r+', encoding='utf8', errors='ignore') as f:
        page = f.readlines()
        f.seek(0)
        for line in page:
            if end in line or cap_hr in line or link in line or cpyrgt in line or stamp in line or end_block in line:
                pass
            else:
               f.write(line) 
        f.truncate() # this ensures there is nothing written to the file after the for loop completes.
    return None

def remove_404(source):
    with open(source, "r", encoding='utf8', errors='ignore') as f:
        text = f.read()
        f.seek(0)
        if "404 - File or directory not found." in text:
            return True
        else:
            return False

def combine_files(source):
    with open(source + "combined.html", "a", encoding='utf8', errors='ignore') as new:
        with open(source, 'r', encoding='utf8', errors='ignore') as f:
            text = f.read()
            new.write(text)

for root, subdirectories, files in os.walk(directory):
    files.sort()
    for file in files:
        source = os.path.join(root, file)
        if ".html" in source:
            if remove_404(source) == True:
                os.remove(source)
            else:
                rem_chunk(source)
                rem_line(source)
                combine_files(source)
            