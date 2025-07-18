def getBit(n,i):
    mask = 1 << i
    return 1 if (n & mask) else 0

n=25
p=4
print(f"Bit in the place {p} in {n} is {getBit(n,p)}")


p=2
print(f"Bit in the place {p} in {n} is {getBit(n,p)}")