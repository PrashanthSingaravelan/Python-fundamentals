import re
# ^ => First word of a string
# $ => Last word of a string
pattern= '^a...s$'
test_string=input("Enter your string ") # The method returns a match object
result=re.findall(pattern,test_string) # if the search is successful. If not, it returns None.
if result:
   print("Search Successful")
else:
   print("Search unsuccessful")


