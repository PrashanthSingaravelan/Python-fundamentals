## dict.OrderedDict
# An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted.
# The only difference between dict() and OrderedDict() is that:
# OrderedDict preserves the order in which the keys are inserted. 
# A regular dict doesn’t track the insertion order, and iterating it gives the values in an arbitrary order. 
# By contrast, the order the items are inserted is remembered by OrderedDict.

## Db between Normal dictionary and Ordered Dictionary
from collections import OrderedDict
## Ordered Dictionary
ord_dict1 = OrderedDict()
ord_dict1['Prashanth'] = 24
ord_dict1['Mothish']   = 26
ord_dict1['Joe Biden'] = 284
ord_dict1['Kamala Harris'] = 150
print('Ordered Dictionary : ',ord_dict1)
for i,j in ord_dict1.items():
	print(i,j)

## Normal Dictionary
dict1 = {}
dict1['Prashanth'] = 24
dict1['Mothish']   = 26
dict1['Joe Biden'] = 284
dict1['Kamala Harris'] = 150
print('Normal Dictionary : ',dict1)
for i,j in dict1.items():
	print(i,j)
"""







