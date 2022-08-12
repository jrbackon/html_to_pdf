import os

directory = "/Volumes/GoogleDrive/My Drive/Security/FER/FER1998/FER1998/fusionmxdev.babson.edu/entrep/fer/papers98"

def rem_ablrule(source):
    image_line = "<hr>"
    flag = False
    with open(source, 'r+', encoding='utf8', errors='ignore') as f:
        page = f.readlines()
        f.seek(0)
        for line in page:
            if image_line in line:
                flag = True
            else:
                f.write(line)
        f.truncate()
    if flag == True:
        print(source)
        return(print("Line break images removed" + "\n"))
    else:
        print(source)
        return(print("No line breaks in file."))
    
for root, subdirectories, files in os.walk(directory):
    for file in files:
        source = os.path.join(root, file)
        if ".html" in source:
            rem_ablrule(source)