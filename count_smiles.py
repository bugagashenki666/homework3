import re

regex = r"[;:]-*([)(\[\]])\1*"
s = input()
r = re.compile(regex)
result = len(r.findall(s))
print(result)