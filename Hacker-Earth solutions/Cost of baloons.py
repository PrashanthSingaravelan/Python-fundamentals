## Problem --> https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/

def cost(list1,green_cost,purple_cost):
    final_cost = green_cost_final = purple_cost_final = 0    
    for i,j in list1:
            green_cost_final  = green_cost_final   + (green_cost * i)
            purple_cost_final = purple_cost_final + (purple_cost * j)
    final_cost = (green_cost_final + purple_cost_final)
    return final_cost


t=int(input("Enter the number of test cases : "))
for i in range(t):
    final_min_cost = []
    green_cost,purple_cost = input("Enter the color of green and purple baloon : ").split()
    green_cost  = int(green_cost)
    purple_cost = int(purple_cost)
    
    n=int(input("Enter the number of students : "))
    
    # List of tuples input
    list1 = list(tuple(map(int,input().split())) for i in range(n))
    final_min_cost.append(cost(list1,green_cost,purple_cost))

    # Reversing the list of tuples
    list1 = [i[::-1] for i in list1]

    final_min_cost.append(cost(list1,green_cost,purple_cost))

    ## Finding the minimum cost
    print(min(final_min_cost)) 