 # Quantifiers
# 1)  '+'   = 1 or more [Greedy quantifier]
# 2)  '?'   = 0 or 1
# 3)'{n,m}' = n to m repititions 
# 4)  '*'   = 0 or more


import re

# 1) '+' = 1 or more; Greedy quantifier=Instead of getting least amount, it will get most
#    amount.It will go untill it hit something that is not inluded in that specific regex
print(re.search("\w+","abcdef bgch")) # Goes upto f. But space not included so it is false
print(re.search("\w+\W+\w+","abcdef jijoof popd").group())
# \w+ => abcdef , W+ => blank space , w+ =>jijoof. Notincluded=> <space>popd

# 2) '?' = 0 or 1 [May or may not be]
print(re.search("\w+\W?\w+","anbcdefdefg").group()) # W?=> 0 occurence 
print(re.search("\w+\W?\w+","abcdef fuids").group())  #W? => 1 occurence

# 3)'{n,m}' = n to m repititions 
print(re.search("\w{3}","This is best").group())  # Only will take upto 3. Output => Thi
print(re.search("\w{1,4}","Chandler").group()) # From 1 to 4.              Output => Chan

print(re.search("\w{1,4}\W{0,4}\w+","Joey is naughty").group())

# Initial index. So Not necessary to specify the final index value
print(re.search("\w{1,}\W{0,}\w+","Joey is naughty").group())

# Final index. So Not necessary to specify the initial index value
print(re.search("\w{,4}\W{,4}\w+","Joey is naughty").group())

