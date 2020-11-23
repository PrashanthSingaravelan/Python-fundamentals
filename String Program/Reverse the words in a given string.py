# input --> I am good
# output -> good am I

str1  = input("Enter a sentence : ")
list1 = str1.split(" ")
list1.reverse()
print("Reverse of words in a given sentence : {}".format(' '.join(list1)))