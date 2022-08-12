import re
pat = "/(.*?)\.html"

url = []
fusion = "https://fusionmxdev.babson.edu/entrep/fer/papers98/index98/index98.html"

with open("F:/My Drive/Security/FER/1998.txt", "r") as f:
    for line in f:
        if '.html' in line:
            match = re.search(pat, line)
            print(match.group())
            url.append(str(match.group()))

with open("F:/My Drive/Security/FER/1998Url.txt", "w") as file:
    for i in url:
        file.write(fusion + i + "\n")