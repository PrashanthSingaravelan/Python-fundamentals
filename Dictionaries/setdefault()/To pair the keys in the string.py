import pprint
DATA_SOURCE = (('key1', 'value1'),
               ('key1', 'value2'),
               ('key2', 'value3'),
               ('key2', 'value4'),
               ('key2', 'value5'),)

newdata = {}
for k, v in DATA_SOURCE:
# If values already there it appends it
    newdata.setdefault(k, []).append(v) # Output=>{'key1': ['value1', 'value2'], 'key2': ['value3', 'value4', 'value5']}

# Values already there so doesn't accept the new one
    # newdata.setdefault(k,v)  Output=>{'key1': 'value1', 'key2': 'value3'}
pprint.pprint(newdata)