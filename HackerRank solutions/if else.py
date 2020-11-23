def func1(n):
    if n%2!=0:  # Odd
        print("Weird")

    if n%2==0:  # Even
      if n in range(6 ,21):
        print("Weird")
      if n in range(2,6):
        print("Not Weird")
      if n in range(21,101):
        print("Not Weird")
        
n=int(input())
func1(n)