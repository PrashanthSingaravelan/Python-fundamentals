# Set => [ ] It is used to create our own character set
# [A-Z] =>  '-' is a metacharacter set when used in [ ] (customer character set)

import re
string1="Chandler,Joey,Ross,Monica,Pheebs"
print(re.findall("[A-Z]",string1)) # ['C', 'J', 'R', 'M', 'P']

print(re.findall("[A-Z,]",string1)) # Includes all the capital letter and commas
# ['C', ',' , 'J' , ',' , 'R' , ',' , 'M' , ',' , 'P']

print(re.findall("[A-Za-z,..]","Hey,I am fine....")) # Includes A-Z ; a-z; comma and fulstop
# ['H', 'e', 'y', ',', 'I', 'a', 'm', 'f', 'i', 'n', 'e', '.', '.', '.', '.']

#  In set [ ]
# Regular expression meta character => normal character only
# Python meta character             => python meta character only
# period (.)     => Normal fullstop
# Quantifier (?) => Normal question mark
# \s => \s only matches whitespaces

print(re.findall("[A-za-z?,\s,]","Hi, How are you Prashanth?"))
# ['H', 'i' , ',' , ' ', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', ' ', 'P', 'r', 'a', 's', 'h', 'a', 'n', 't', 'h', '?']
