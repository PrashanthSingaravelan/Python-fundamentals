# PAN number=<AAAAA8888A>
import re
n=input("Enter your PAN number:")
if len(n)<10 and len(n)>10:
    print("Your PAN length is mismatched")
    print("Invalid PAN")
    exit
elif re.search("[^a-z A-Z 0-9]",n):
    print("Not valid")
    exit
elif re.search("[0-9]",n[0:5]): # First five should be A-Z and not 0-9
    print("Not valid")
    exit
elif re.search("[A-Z]",n[5:9]): # Five to nine should be 0-9 and not A-Z
    print("Not valid")
    exit
elif re.search("[0-9]",n[-1]): # Last character should be a number
    print("Not valid")
    exit
else:
    print("Your PAN {} is valid".format(n))