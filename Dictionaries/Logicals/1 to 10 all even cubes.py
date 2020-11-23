dict1={i:i**3 for i in range(1,10) if i%2==0}
print(dict1)  # {2: 8, 4: 64, 6: 216, 8: 512}

print(*sorted(dict1.items())) # (2, 8) (4, 64) (6, 216) (8, 512)