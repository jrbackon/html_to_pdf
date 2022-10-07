import re
pat = "[A-Za-z0-9]+/[A-Za-z0-9]+\.htm"

url = []
fusion = "https://fusionmxdev.babson.edu/entrep/fer/papers97/index97.htm"

with open("F:/My Drive/Security/FER/1997.txt", "r") as f:
    for line in f:
        if '.htm' in line:
            match = re.search(pat, line)
            print(match.group())
            url.append(str(match.group()))

with open("F:/My Drive/Security/FER/1997Url.txt", "w") as file:
    for i in url:
        file.write(fusion[:-11] + i + "\n")