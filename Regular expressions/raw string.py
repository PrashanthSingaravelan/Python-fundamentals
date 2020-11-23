import re
p=re.search('n','\n')  #'\n' is a special character 
print(p) # none

q=re.search('n','\\n') #'\\n' This will get rid of the special character meaning 
print(q) # treats as normal n

# r will treat the complete string as raw string 
# Applying r to the regex doesn't affect its meaning ie r'\n'='\n'
# because regex itself has its own spcial characters -> meta characters
# for the regex  r'\n'='\n'

r=re.search(r'\n','\n\n\n\n\n\n\n\n\n\n\n')
print(r) # <re.Match object; span=(0, 1), match='\n'>

# Applying r to the string really affect its meaning
# and treat them as a normal raw string

s=re.search(r'\n', r'\n\n\n\n\n\n\n\n\n\n\n' )
print(s) # None
