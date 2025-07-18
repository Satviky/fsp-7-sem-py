def setBit(n,i):
    return n | (1 << i)
        


n=25 # 16+8+1
p=2
print(f"n={n} and res= {setBit(n,p)}")
