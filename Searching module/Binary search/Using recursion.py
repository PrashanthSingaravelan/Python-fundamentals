
def Binary_search(l,u,key):
    list=[2,8,19,90,100]
    if l==u:
      if list[l]==key:
          print("The exact match is found")
      else:
          print("The match is not found")
    else:
        mid=(l+u)//2
        if(list[mid]==key):
            print("The mid value and the key is same")
        if list[mid]>key:
            return Binary_search(mid+1,u,key)
        else:
            return Binary_search(l,mid-1,key)

l=0
u=4
key=90
a=Binary_search(l,u,key)
print(a)