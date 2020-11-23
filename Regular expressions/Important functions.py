import re
string1="It is a Good Day"
# 1) join()
print(re.findall("\S",string1))
 # ['I', 't', 'i', 's', 'a', 'G', 'o', 'o', 'd', 'D', 'a', 'y']

print(re.findall("\S+",string1))
  # ['It', 'is', 'a', 'Good', 'Day']

print(" ".join(re.findall("\S+",string1))) # (OR) print(*re.findall("\S+",string1))
  # It is a Good Day

# 2) group()
string3="Ross your are very disgusting"
print(re.search("\S+\s+\S+\s+\S+\s+\S+\s+\S+",string3))
# <re.Match object; span=(0, 29), match='Ross your are very disgusting'>

print(re.search("\S+\s+\S+\s+\S+\s+\S+\s+\S+",string3).group())
# Ross your are very disgusting