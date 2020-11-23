def evenupodddown(list2):
    # Input using list comprehension
    even = [list2[i] for i in range(len(list2)) if i%2==0]
    odd  = [list2[i] for i in range(len(list2)) if i%2!=0]
    print(sorted(even)+sorted(odd,reverse=True))

# Input from the user
list1=[]
n=input("Enter the values : ")
list1=n.split()
list2=list(map(int,list1))
evenupodddown(list2)