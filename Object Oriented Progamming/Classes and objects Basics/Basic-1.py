class Computer:
    def config(self):
        print("i5 8th gen,Ram=8GB, SSD=128Gb")

# 1st method
a=5
obj1=Computer
obj1.config(a)

# 2nd method
Computer.config(obj1)

