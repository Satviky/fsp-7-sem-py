import math
def mstd(n,dp):
    if(n==1): return 0
    if (dp[n]!=0): return dp[n]

    op1=op2=op3 = math.inf
    if (n%3==0): op1 = mstd(n//3,dp) +1
    elif (n%2==0): op2 = mstd(n//2,dp) +1
    else: op3=mstd(n-1,dp) +1
    ans=min(op1,op2,op3)
    print(n,dp)
    return ans

n=10
dp = [0]*(n+1)
print(mstd(n,dp))