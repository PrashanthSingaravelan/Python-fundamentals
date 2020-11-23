# dict.fromkeys(sequence,values)
# sequence --> This is the list of values which would be used for dictionary keys preparation.
# values   --> This is optional, if provided then value would be set to this value if not NULL

sample_dict = dict()
sequence = ['Name','Age','Gender']
print('By default the dictionary values are None : ',dict.fromkeys(sequence)) # By default None

value = 24
print('The dictionary values are set to 24 : ',dict.fromkeys(sequence,value))