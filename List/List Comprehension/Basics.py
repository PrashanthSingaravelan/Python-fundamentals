# List Comprehension

#To square a number in a given range

for items in range(0,10):
    #print(items*items) # At last 9*9=81

#Using List Comprehension
mylist=[item*item for item in range(0,10)]
print(mylist)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#Squaring all the even numbers using if
mylist1=[x*x  for x in range(0,10) if(x%2)==0]
#print(mylist1)

#Squaring all the even number using if and else
mylist2=[y if y%2==0 else 'Odd' for y in range(0,10)]
#print(mylist2)  # [0, 'Odd', 2, 'Odd', 4, 'Odd', 6, 'Odd', 8, 'Odd']
