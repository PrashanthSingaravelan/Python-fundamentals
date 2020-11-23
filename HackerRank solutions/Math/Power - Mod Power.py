import math
a = int(input())
b = int(input())
m = int(input())

if m and b>=0:
   print(pow(a,b))     # a to the power b (3 to the power 4) -> 81
   print(pow(a,b,m))   # (a to the power b) -> (ans%m) -> 81%5 -> 1
