# \w=alphanumeric characters including "_"
# \W=non alphanumeric character

import re
print(re.findall("\w","The best_!>")) #  Will go until _ and ignores !>
# Output => ['T', 'h', 'e', 'b', 'e', 's', 't', '_']

print(re.search("\w\w\w\w\w\w","The_best").group())
# Output => # The_be

print(re.findall("\W","The best_!>")) #  backspace is also included in \W
# Output => [' ', '!', '>']

n=input("Enter your shedule: ")

p=re.compile('\w') # \w= Alphanumeric characters
print(p.findall(n))

q=re.compile('\w+') # \w+= Alphanumeric characters in groups
print(q.findall(n))

r=re.compile('\W+') # \W= Non alphanumeric characters
print(r.findall(n))