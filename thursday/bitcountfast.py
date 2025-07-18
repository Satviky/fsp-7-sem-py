# find the number of set bits in a number n
# for n = 63 = 0011 1111, output will be 6
def countSetBits(n):
    count = 0
    while n:
        n = n & (n-1)
        count = count +1
    return count

n = 63
print(f"For n = {n}, number of set bits = {countSetBits(n)}")