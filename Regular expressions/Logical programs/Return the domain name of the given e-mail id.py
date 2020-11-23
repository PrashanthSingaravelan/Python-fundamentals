import re
string1="prashanth_singar@hotmail.com,prashanthsing24@gmail.com,prashanth@yahoo.com"
print(re.findall("\w+",string1))
# ['prashanth_singar', 'hotmail', 'com', 'prashanthsing24', 'gmail', 'com', 'prashanth', 'yahoo', 'com']

print(re.findall("@\w+",string1))
# As dot(.) is not included in \w+
# ['@hotmail', '@gmail', '@yahoo']

print(*re.findall("@\w+.\w+",string1))
# @hotmail.com @gmail.com @yahoo.com

# To print only the extensions
# (\w+) => Will be more focussed and printed
print(*re.findall("@\w+(.\w+)",string1))
# .com .com .com
