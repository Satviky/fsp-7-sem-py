def setBit(n,i):
    return n ^ (1<<i)
        

n=25 # 16= 0001 0000
p=4
print(f"n={n} and res= {setBit(n,p)}")
