def crItoJ(n,i,b):
    mask1 = ~(1<<i)
    mask2 = b<<i
    n=n & mask1
    n=n| mask2
    return n

n=63 # 16= 0001 0000
i=4
b=0
print(f"n={n} and res= {crItoJ(n,i,b)}")
