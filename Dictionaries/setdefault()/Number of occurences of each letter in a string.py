import pprint
str1="Hello everyone. I am very glad to inform you about this new Google Pixel"
dict1={}
for i in str1:            # Eg: Take e ("Hello everyone") 3 e's
    dict1.setdefault(i,0) # 1) e:0  2) e:0 => Already exist as 1 so returns 1
    dict1[i]=dict1[i] + 1 # 1) e:1  2) 1+1 = 2
pprint.pprint(dict1)
print(pprint.pformat(dict1))

# pprint.pprint() helpful when dictionary itself contains a nested lists/dictionaries