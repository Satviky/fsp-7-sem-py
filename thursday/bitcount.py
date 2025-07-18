# find the number of set bits in a number n
# for n = 63 = 0011 1111, output will be 6
def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

n = 63
print(f"For n = {n}, number of set bits = {countSetBits(n)}")