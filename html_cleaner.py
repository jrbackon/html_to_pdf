import os

directory = input("What is the path of the folder containing the .html files you would like to clean? ")

# This function removes html line breaks or images that don't convert well to pdf   
def rem_ablrule(source):
    image_line = "<hr>" # this line identifies the code to be removed
    flag = False
    with open(source, 'r+', encoding='utf8', errors='ignore') as f: # it's important to specify the encoding or certain characters won't show up correctly when you write the new file
        page = f.readlines()
        f.seek(0) # this returns the script to the beginning of the file as the file will be overwritten with every line except those matching image_line
        for line in page: # this for loop checks each line in the file, if it finds a match with image_line it doesn't write that line to a new file
            if image_line in line:
                flag = True # This flag is used to output a message later
            else:
                f.write(line)
        f.truncate() # this ensures there is nothing written to the file after the for loop completes.
    if flag == True:
        print(source)
        return(print("Line break images removed" + "\n"))
    else:
        print(source)
        return(print("No line breaks in file."))
    
for root, subdirectories, files in os.walk(directory): # this for loop walks through all directories in the specified folder, and runs the ablrule function on all .html files
    for file in files:
        source = os.path.join(root, file)
        if ".html" in source:
            rem_ablrule(source)