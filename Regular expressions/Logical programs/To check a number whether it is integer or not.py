import re
register= input("Enter the values:")

if re.search("^\-?[1-9][0-9]*$",register): # \=> To overcome its default meaning in regex's
   print("Matched")      # ?=> Can be -integer or +integer (0 or 1 occurence)
else:                    # *=> Number can be single digit or mutidigit (1 or more occurence)
   print("Not Matched")


