def input(list1):
    even=[list1[i] for i in range(0,len(list1)) if i%2==0]
    odd =[list1[i] for i in range(0,len(list1)) if i%2!=0]
    print("even",even)
    print("odd",odd)

list1=[44,31,90]
input(list1)