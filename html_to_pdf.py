import os, pdfkit

directory = input("What is the path of the folder containing the .html files you would like to convert to .pdf? ")

def pdf2html(source, destination):
    try: # the pdfkit library tends to throw an IOError even though it converts the file successfully. Not sure why, but using a try / except block gets around it.
        pdfkit.from_file(source, destination)
    except IOError:
        pass

count = 0
for root, subdirectories, files in os.walk(directory): # this for loop walks through the given directory and looks for .html files.
    for file in files:
        if ".html" in file:
            source = os.path.join(root, file) # this is just the name of the file in the given directory
            destination = os.path.join(root, file)[:-5] + ".pdf" # this line uses the filename in source and appends the end to be .pdf
            pdf2html(source, destination)
            count += 1

print(str(count) + " files converted successfully.")