# 1) List Comprehension
my_list1=["34","90","93","29","67"]
my_list1=[int(i) for i in my_list1]
print(my_list1)

# 2) map()
my_list2=["15","43","78","63"]
my_list2=list(map(int,my_list2))
print(my_list2)