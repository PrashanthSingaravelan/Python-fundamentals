n=input("Pls enter your name and e-mail address with domain name: ")

import re
p=re.compile("\w+@\w+.\w+")
print("Your valid email-id: ")
print(*re.findall(p,n))