A={1,2,3,4}
B={3,4,5,6}

print("The union elements are:",A|B) # print(A.union(B))

print("The intersection elements:",A.intersection(B)) #print(A & B)

# Difference
print("The difference between the sets are:",A-B) # A.difference(B)

# Symmetric difference : A-B union B-A
print("The symmetric differences are:",A^B)
print(A.symmetric_difference(B))