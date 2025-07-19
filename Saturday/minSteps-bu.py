import math
def msbu(n,dp):
    # base case
    dp[1]=0
    # now we will form othr cases
    for i in range(2, n + 1):
        min_steps = dp[i - 1] + 1
        if (i% 3 == 0): # op-1
            min_steps = min(min_steps, dp[i // 3] + 1)
        if (i%2==0): # op-2
            min_steps = min(min_steps, dp[i // 2] + 1)
            
        dp[i] = min_steps 
        
        print (n,dp)

    return min_steps

# passing parameters.
n=10
dp = [0]*(n+1)
print(msbu(n,dp))