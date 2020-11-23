# Enumerate operator

# To know the index position and their element
index_count=0
for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count+=1

# Using enumerate operator

# Printing the actual index values
word='abcde'
for item in enumerate(word,0):
    print(item)

#Printing the virual index values
for item1,item2 in enumerate (word,100):
    print(item1,item2)

