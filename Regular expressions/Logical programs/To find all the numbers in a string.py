# Input : abcd11gdf15hnnn678hh4
# Output: 11 15 678 4
# Input : 1abcd133hhe0
# Output: 1 133 0

import re
n=input("Pls enter you string:") # Pras24ha2001nt4

# * removes all the list formats like [] , and " "

print(*re.findall("[0-9]+",n)) # 24 2001 4

print(*re.findall("[0-9]",n)) # 2 4 2 0 0 1 4
