x1=int(input())
v1=int(input())

x2=int(input())
v2=int(input())

sum1=x1+v1
sum2=x2+v2


if(x2>x1) and (v2>v1):
    print("NO")
else:
    for i in range(10):
      if(sum1==sum2):
          print("YES")
          break
      else:
          sum1=sum1+v1
          sum2=sum2+v2
       


        