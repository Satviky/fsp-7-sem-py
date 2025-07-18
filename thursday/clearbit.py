def crItoJ(n,i,j):
    mask1 = (-1)<< (i+j-1)
    mask2 = ~((-1) << j)
    mask3 = mask1 | mask2
    return n & mask3

n=63 # 16= 0001 0000
i=4
j=2
print(f"n={n} and res= {crItoJ(n,i,j)}")
