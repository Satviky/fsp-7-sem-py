import math
def mincoinTopDown(n, coins, t, dp):
    if (n ==0): return 0
    if (fp[n]!= 0): return dp[n]

    ans= math.inf
    for i in range (t):
        if(n-coins[i] >= 0):
            subprob= mincoinTopDown(n - coins[i], t, dp)
            ans = min(ans,subprob + 1)
    dp[n] = ans
    return dp[n]

N=15; coins=[1,7,10]
t=len(coins)
dp=[0 for i in range(n+1)]
print(mincoinTopDown(m,coins,t,dp))