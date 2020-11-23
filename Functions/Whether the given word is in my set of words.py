# Normal Function
def Special_Dish2(name):
    if 'Dosa' in name:
        return True
    else:
        return False


n=input("Enter your Favourite Dish:")
result1=Special_Dish2(n)
print(result1)

# Reducing the function as a bool method
def Special_Dish2(name2):
     return 'Dosa' in name2

m=input("Enter your Favourite Dish:")
result2=Special_Dish2(m)
print(result2)

