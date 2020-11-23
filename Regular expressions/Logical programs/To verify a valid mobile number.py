n=input("Enter your mobile number: ")

import re    # [^0]     => Not start with 0
if re.search('[^0][0-9]{9}',n):
# Or can be in this form if re.search(‘[1-9][0-9]{9}',n):

    print("Valid mobile number")  # [^0]     => 1st digit not start with 0
else:                             # [0-9]{9} => From 2nd to 10th i.e 9 numbers can be 0 to 9
    print("Not a valid number")