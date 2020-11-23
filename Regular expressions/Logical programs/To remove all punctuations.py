str1='''Hello! everyone Good Evening and a warm welcome to all.
  How are you? How is your job,personal life? and all sorts of stuff.'''
import re
print(*re.findall("\w+",str1))