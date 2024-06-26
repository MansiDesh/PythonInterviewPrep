string = "Python is 1234"
import re

charac = re.findall("[a-zA-Z]", string)
print(len(charac))
digits = re.findall("[0-9]", string)
print(len(digits))
spaces = re.findall("[ \n]", string)
print(len(spaces))
