import re
string1="Apple,Orange,Banana;Pineapple"
print(re.sub(r'[,;]',' ',string1)) # Removes all the , and ; Then puts over a blank space

# Apple Orange Banana Pineapple