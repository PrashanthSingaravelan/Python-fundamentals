# Using \D and \d
import re
n=input("Enter your shedule: ")

p=re.compile('\d') # \d=[0-9]
print(p)
print(p.findall(n))

q=re.compile('\d+') # \d+ will match a group of [0-9], group of one or greater size
print(q.findall(n))

r=re.compile('\D+') # \D Non digit character
print(r.findall(n))
