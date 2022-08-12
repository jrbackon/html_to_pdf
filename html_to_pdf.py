import os, pdfkit

directory = "/Volumes/GoogleDrive/My Drive/Security/FER/FER1998/FER1998/fusionmxdev.babson.edu/entrep/fer/papers98"
def pdf2html(source, destination):
    try:
        pdfkit.from_file(source, destination)
    except IOError:
        pass

count = 0
for root, subdirectories, files in os.walk(directory):
    for file in files:
        if ".html" in file:
            source = os.path.join(root, file)
            destination = os.path.join(root, file)[:-5] + ".pdf"
            pdf2html(source, destination)
            count += 1

print(str(count) + " files converted successfully.")