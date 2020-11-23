import re
print(re.search("c","abcde")) #<re.Match object; span=(2, 3), match='c'>

# Using start()=Starting index and end()=last index
print(re.search("c","abcde").start()) #2
print(re.search("c","abcde").end())   #3

print(re.search("c","abcde").group()) # c
print(re.search("n.+","abchnd ghd jal").group()) #nd ghd jal

